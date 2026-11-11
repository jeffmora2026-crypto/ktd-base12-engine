# ==============================================================================
# PENTA CHANNEL – FULL-DUPLEX NORTH/SOUTH ROUTING DEALER
# ==============================================================================

import threading
import time

class PentaChannelDealer:
    """
    Bidirectional full-duplex input/output data dealer bridging North and South
    transactional clusters via pentagonal packet multiplexing.
    """
    def __init__(self):
        self.north_buffer = []
        self.south_buffer = []
        self._active = True

    def transmit_north_to_south(self, payload: dict):
        packet = {"route": "NORTH->SOUTH", "timestamp": time.time(), "data": payload}
        self.south_buffer.append(packet)
        print(f"[PENTA-CHANNEL] [NORTH OUTBOUND] Payload routed successfully: {payload['tx_id']}")

    def transmit_south_to_north(self, payload: dict):
        packet = {"route": "SOUTH->NORTH", "timestamp": time.time(), "data": payload}
        self.north_buffer.append(packet)
        print(f"[PENTA-CHANNEL] [SOUTH OUTBOUND] Payload routed successfully: {payload['tx_id']}")

    def start_duplex_loop(self):
        print("[PENTA-CHANNEL] Full-duplex dealer online and synchronizing North-South pipelines...")

if __name__ == "__main__":
    dealer = PentaChannelDealer()
    dealer.start_duplex_loop()
    
    # Simulating simultaneous duplex traffic
    dealer.transmit_north_to_south({"tx_id": "TX_NORTH_991", "val": 120.0})
    dealer.transmit_south_to_north({"tx_id": "TX_SOUTH_882", "val": 340.0})
