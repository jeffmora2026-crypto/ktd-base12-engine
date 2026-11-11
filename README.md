# KTD-Base12 Engine v12.5 (Edge AI Core)

Deterministic transactional core in base 12 for sovereign edge execution, featuring RK4 predictive dynamics, thermal impedance protection ($Z \ge 16.18$), and local SHA-256 ledger security.

## 🏛️ Architecture Overview

The KTD-Base12 engine breaks away from traditional centralized cloud star topologies, implementing a decentralized polyhedral (dodecahedral) edge model:
- **South Pole (Ingress):** Direct reception of transactional payloads (PayPal Sandbox JSON) via the gateway adapter.
- **Equator (Processing Core):** Active dispatcher executing geometric parity, RK4 predictive trajectory modeling, and transactional logic validation.
- **North Pole & 5-Vertex EtherChannel:** Aggregated trunk line routing validated transactions outward with zero network overhead.

## 📂 Core Modules

1. **`gateway_adapter.py`** - Central orchestrator managing South Pole ingress, core processing, and North Pole dispatch.
2. **`topological_classifier.py`** - Validates strict modular congruence of transactional frames using base 12 geometry ($\phi = 1.618$).
3. **`rk4_predictive_core.py`** - Models financial derivatives using Runge-Kutta 4th-order equations to anticipate risk vectors in real time.
4. **`thermal_breaker.py`** - Evaluates critical thresholds ($Z \ge 16.18$) to autonomously isolate anomalies before hardware saturation.
5. **`immutable_ledger.py`** - Guarantees forensic traceability via local SHA-256 encrypted block-chaining without external dependencies.
6. **`penta_channel.py`** - Manages the 5-vertex EtherChannel I/O bus for high-throughput data distribution.

## 🚀 Quick Start & Testing Instructions for Judges

Ensure you are in the root directory of the repository (with no nested folders) and run the primary gateway adapter:

```bash
python3 gateway_adapter.py
