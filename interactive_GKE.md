## GKE
Managed k8s by google is GKE. All fancy features where most of GCP services can be inter-tangled for cool solution

Step1:
```bash
#Authenticate and Authorize
gcloud container clusters get-credentials cluster-1 --zone=us-central1-c
#Fetching cluster endpoint and auth data.
#kubeconfig entry generated for cluster-1.
```

Additional tips:

# How to pause a running GKE cluster during homelab or self-learning use:

Follow these steps to pause the GKE cluster without deleting the entire cluster and resume when needed


![image](https://github.com/rajesh-sampathrajan/cka_in_8_weeks/assets/111441779/8b1b7f40-b793-4c3a-b3ac-1aab25dc65d2)

1. Edit the nodepool and decrease the node to 0 and save the changes 
2. In other words - its just resizing the GKE nodes.

![image](https://github.com/rajesh-sampathrajan/cka_in_8_weeks/assets/111441779/d583f7f6-801c-4c9b-8d1d-49d8c88a997e)
