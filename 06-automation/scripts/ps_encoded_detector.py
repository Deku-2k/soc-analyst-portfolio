"""Quick heuristic detector for suspicious PowerShell -EncodedCommand usage.
Usage:
    python ps_encoded_detector.py sample_logs.txt
Input format:
    One process command line per line.
"""
import sys, base64, re

def suspicious_b64(s):
    try:
        # loose check: strip non-b64 and try decode
        cleaned = re.sub(r'[^A-Za-z0-9+/=]', '', s)
        if len(cleaned) >= 40 and len(cleaned) % 4 == 0:
            base64.b64decode(cleaned, validate=False)
            return True
    except Exception:
        return False
    return False

def is_suspicious(cmd):
    if "-EncodedCommand" in cmd or "-enc " in cmd.lower():
        # find long tokens that look like base64
        tokens = re.findall(r'[A-Za-z0-9+/=]{40,}', cmd)
        for t in tokens:
            if suspicious_b64(t):
                return True
    return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Provide a log file with one command line per line.")
        sys.exit(1)
    suspicious = []
    with open(sys.argv[1], 'r', encoding='utf-8', errors='ignore') as f:
        for i, line in enumerate(f, 1):
            if is_suspicious(line.strip()):
                suspicious.append((i, line.strip()))
    for i, cmd in suspicious:
        print(f"[!] Line {i}: {cmd}")
    print(f"Total suspicious: {len(suspicious)}")
