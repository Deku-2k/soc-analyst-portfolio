# Home Lab Blueprint

## Objective
Hands-on SOC practice with logs, alerts, and hunts.

## Minimal Stack
- **Wazuh** (agent + manager) for EDR-like visibility and rules
- **Zeek** for network metadata
- **Elastic Stack** (or Security Onion) for search & dashboards
- Optional: **Suricata** for IDS alerts

## Topology
- Host A (Windows 10/11) — Wazuh agent, attack simulation
- Host B (Ubuntu) — Attacker box (Kali or tools)
- Sensor — Zeek/Suricata tapping a mirror port
- SIEM — Elastic or Security Onion VM

## To Do
- [ ] Diagram the network
- [ ] Ingest test logs (e.g., Atomic Red Team)
- [ ] Baseline dashboards and alerts
- [ ] Document detections and gaps
