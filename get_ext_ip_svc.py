## Detect the external IP address for latest and newly created services in k8s, namespace is part of cli args.

import subprocess
import json
import time
import argparse

timeout = 600 # 10 minute timeout
interval = 10 # 10 second interval

# Parse command line arguments
parser = argparse.ArgumentParser(description="Monitor newly created services in a namespace for their external IP addresses.")
parser.add_argument("namespace", help="The namespace to monitor for new services.")
args = parser.parse_args()

# Monitor the namespace for newly created services and their external IP addresses
start_time = time.time()
existing_services = set()
while time.time() - start_time < timeout:
    output = subprocess.check_output(["kubectl", "-n", args.namespace, "get", "svc", "-o", "json", "--sort-by", ".metadata.creationTimestamp"])
    svc_list = json.loads(output)["items"]
    for svc in svc_list:
        service_name = svc["metadata"]["name"]
        if service_name not in existing_services:
            existing_services.add(service_name)
            external_ip = svc["status"]["loadBalancer"].get("ingress", [{}])[0].get("ip")
            if external_ip:
                print(f"{service_name} external IP: {external_ip}")
                if len(existing_services) == len(svc_list):
                    # All existing services have been checked, exit
                    exit(0)
            else:
                print(f"Waiting for {service_name} external IP...")
    time.sleep(interval)

print(f"Timeout reached waiting for new services in {args.namespace} to get an external IP.")
exit(1)
