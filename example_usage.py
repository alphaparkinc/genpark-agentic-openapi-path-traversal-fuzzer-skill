from client import AgenticOpenapiPathTraversalFuzzerClient
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

def main():
    fuzzer = AgenticOpenapiPathTraversalFuzzerClient()
    print("=== AGENTIC OPENAPI PATH TRAVERSAL FUZZER ===")
    
    route = "/api/v1/documents/{filename}/download"
    res = fuzzer.fuzz_route(route, "filename")
    
    print(f"Target Route: {res['route_template']} (Param: {res['fuzzed_parameter']})")
    print(f"Generated {res['total_vectors_generated']} Path Traversal Fuzzing Probes:")
    print()
    
    for i, v in enumerate(res['traversal_vectors'][:5], 1):
        print(f"{i}. Pattern: {v['payload_pattern']}")
        print(f"   Injected URL: {v['injected_raw_path']}")
        print(f"   Encoded URL : {v['injected_encoded_path']}")
        print()

if __name__ == "__main__":
    main()
