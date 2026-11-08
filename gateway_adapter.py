# ==============================================================================
# KTD-BASE12-ENGINE – GATEWAY ADAPTER PIPELINE
# Unifies Base-12 Classifier, RK4, Thermal Breaker, and Forensic Ledger
# ==============================================================================

from dodecahedral_classifier import DodecahedralTransactionClassifier
from rk4_predictive_core import PredictiveTrajectoryEngine
from thermal_breaker import ThermalImpedanceBreaker
from immutable_ledger import ImmutableForensicLedger

class GatewayAdapterPipeline:
    """
    Unified pipeline processing external payment requests through the entire 
    Deterministic Transactional Kernel.
    """
    def __init__(self):
        self.classifier = DodecahedralTransactionClassifier()
        self.predictor = PredictiveTrajectoryEngine()
        self.breaker = ThermalImpedanceBreaker()
        self.ledger = ImmutableForensicLedger()

    def process_payment_request(self, tx_id: str, amount: float, origin: str, risk_history: list, vector_z: float) -> dict:
        # 1. Geometric validation and Base-12 parity
        classification = self.classifier.classify_transaction(tx_id, amount, origin)
        
        # 2. RK4 predictive trajectory evaluation
        trajectory = self.predictor.evaluate_transactional_trajectory(risk_history)
        
        # 3. Critical impedance thermal control
        impedance = self.breaker.evaluate_impedance(vector_z)
        
        # Consolidate kernel state
        global_status = "APPROVED_AT_EDGE"
        if impedance["kernel_state"] == "CRITICAL_CUTOFF_ACTIVATED" or classification["integrity_status"] == "ANOMALY_DETECTED":
            global_status = "REJECTED_FOR_SECURITY"

        # 4. Immutable forensic logging in local blockchain
        audited_event = {
            "tx_id": tx_id,
            "amount": amount,
            "global_status": global_status,
            "base12_signature": classification["base12_signature"],
            "trajectory_alert": trajectory["trajectory_alert"],
            "thermal_action": impedance["executed_action"]
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
        tx_id="GATEWAY_TX_LIVE_777",
        amount=500.00,
        origin="EDGE_WEBHOOK",
        risk_history=[0.2, 0.4, 0.6, 0.9],
        vector_z=10.5
    )
    print("[KTD-BASE12-ENGINE] Gateway Pipeline Executed Successfully:")
    for k, v in pipeline_result.items():
        print(f"  > {k}: {v}")
