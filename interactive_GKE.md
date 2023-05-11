## GKE
Managed k8s by google is GKE. All fancy features where most of GCP services can be inter-tangled for cool solution

Step1:
```bash
#Authenticate and Authorize
gcloud container clusters get-credentials cluster-1 --zone=us-central1-c
#Fetching cluster endpoint and auth data.
#kubeconfig entry generated for cluster-1.
```

