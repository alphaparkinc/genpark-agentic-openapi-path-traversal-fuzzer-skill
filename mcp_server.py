import sys, json
from client import AgenticOpenapiPathTraversalFuzzerClient
sys.stdout.reconfigure(encoding='utf-8')

def handle_mcp():
    fuzzer = AgenticOpenapiPathTraversalFuzzerClient()
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps({"status": "ready", "skill": "genpark-agentic-openapi-path-traversal-fuzzer-skill"}))
        return
    req = json.loads(sys.stdin.read() or "{}")
    route = req.get("route", "/api/v1/files/{file_id}")
    param = req.get("param", "file_id")
    res = fuzzer.fuzz_route(route, param)
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    handle_mcp()
