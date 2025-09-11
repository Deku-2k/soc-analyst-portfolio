# Hunt — Encoded PowerShell

**Hypothesis**: Attackers abuse `-EncodedCommand` to execute payloads.  
**Method**: Query PS command-lines for long base64 strings; pivot to parent process and network egress.  
**Outcome**: 3 hosts; 1 benign admin tool; 2 suspicious events; detection created.
