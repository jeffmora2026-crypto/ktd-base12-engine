# ==============================================================================
# KTD-BASE12-ENGINE – MODULE 4: IMMUTABLE FORENSIC LEDGER (SHA-256)
# Deterministic Transactional Kernel (Edge Core)
# ==============================================================================

import hashlib
import json
import time

class ImmutableForensicLedger:
    """
    Records every kernel validation or event into a local blockchain chain 
    via SHA-256, guaranteeing forensic traceability with zero network costs.
    """
    def __init__(self):
        self.chain = []
        self._create_genesis_block()

    def _create_genesis_block(self):
        genesis_block = {
            "index": 0,
            "timestamp": time.time(),
            "data": "GENESIS_BLOCK_KTD_BASE12",
            "previous_hash": "0" * 64,
            "hash": ""
        }
        genesis_block["hash"] = self._calculate_hash(genesis_block)
        self.chain.append(genesis_block)

    def _calculate_hash(self, block: dict) -> str:
        block_copy = block.copy()
        block_copy.pop("hash", None)
        block_string = json.dumps(block_copy, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def register_event(self, transaction_data: dict) -> dict:
        previous_block = self.chain[-1]
        new_block = {
            "index": len(self.chain),
            "timestamp": time.time(),
            "data": transaction_data,
            "previous_hash": previous_block["hash"]
        }
        new_block["hash"] = self._calculate_hash(new_block)
        self.chain.append(new_block)
        return new_block

if __name__ == "__main__":
    ledger = ImmutableForensicLedger()
    test_event = {
        "tx_id": "TX_EDGE_NODE_9988",
        "status": "VALID_AT_EDGE",
        "base12_signature": 6
    }
    generated_block = ledger.register_event(test_event)
    print("[KTD-BASE12-ENGINE] Immutable Forensic Record Generated:")
    print(f"  > Block Index: {generated_block['index']}")
    print(f"  > Current SHA-256 Hash: {generated_block['hash']}")
    print(f"  > Previous Hash: {generated_block['previous_hash']}")
