from dodecahedral_classifier import DodecahedralTransactionClassifier
from rk4_predictive_core import PredictiveTrajectoryEngine
from thermal_breaker import ThermalImpedanceBreaker
from immutable_ledger import ImmutableForensicLedger

class GatewayAdapterPipeline:
    def __init__(self):
        self.classifier = DodecahedralTransactionClassifier()
        self.predictor = PredictiveTrajectoryEngine()
        self.breaker = ThermalImpedanceBreaker()
        self.ledger = ImmutableForensicLedger()

    def verify_paypal_sandbox_token(self, token: str) -> bool:
        if token and token.startswith("SANDBOX_TEST_"):
            return True
        return False

    def cross_validation_audit(self, amount: float, signature: int) -> bool:
        cross_check = (amount * 12) % 12
        return cross_check == 0 and signature % 2 == 0

    def process_payment_request(self, tx_id: str, amount: float, origin: str, risk_history: list, vector_z: float, sandbox_token: str) -> dict:
        sandbox_valid = self.verify_paypal_sandbox_token(sandbox_token)
        if not sandbox_valid and origin == "PAYPAL_SANDBOX_WEBHOOK":
            return {
                "transaction": tx_id,
                "final_status": "REJECTED_SANDBOX_AUTH_FAILED",
                "forensic_hash": "NULL",
                "block_index": 0
            }

        classification = self.classifier.classify_transaction(tx_id, amount, origin)
        audit_passed = self.cross_validation_audit(amount, classification["base12_signature"])
        if not audit_passed:
            classification["integrity_status"] = "ANOMALY_DETECTED"

        trajectory = self.predictor.evaluate_transactional_trajectory(risk_history)
        impedance = self.breaker.evaluate_impedance(vector_z)

        global_status = "APPROVED_AT_EDGE"
        if impedance["kernel_state"] == "CRITICAL_CUTOFF_ACTIVATED" or classification["integrity_status"] == "ANOMALY_DETECTED":
            global_status = "REJECTED_FOR_SECURITY"

        audited_event = {
            "tx_id": tx_id,
            "amount": amount,
            "global_status": global_status,
            "base12_signature": classification["base12_signature"],
            "trajectory_alert": trajectory["trajectory_alert"],
            "thermal_action": impedance["executed_action"],
            "sandbox_verified": sandbox_valid
        }
        forensic_block = self.ledger.register_event(audited_event)

        return {
            "transaction": tx_id,
            "final_status": global_status,
            "forensic_hash": forensic_block["hash"],
            "block_index": forensic_block["index"]
        }

if __name__ == "__main__":
    pipeline = GatewayAdapterPipeline()
    pipeline_result = pipeline.process_payment_request(
        tx_id="GATEWAY_TX_SANDBOX_001",
        amount=500.00,
        origin="PAYPAL_SANDBOX_WEBHOOK",
        risk_history=[0.2, 0.4, 0.6, 0.9],
        vector_z=10.5,
        sandbox_token="SANDBOX_TEST_TOKEN_999"
    )
    print("[KTD-BASE12-ENGINE] PayPal Sandbox Pipeline Executed Successfully:")
    for k, v in pipeline_result.items():
        print(f"  > {k}: {v}")
