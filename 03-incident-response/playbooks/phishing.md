# Playbook — Phishing Triage

## Goal
Efficiently triage and contain suspected phishing emails.

## Steps
1. **Collect**: Raw headers, URLs, attachments (hash first).  
2. **Analyze**: URL sandbox, VT hash lookup, DMARC/SPF checks.  
3. **Contain**: Retract emails, block IOCs, isolate endpoints if needed.  
4. **Eradicate/Recover**: Reset creds, reimage if malware executed.  
5. **Report**: Add to `reports/` with indicators and lessons.

## KPIs
- Time to containment
- % of users who reported
