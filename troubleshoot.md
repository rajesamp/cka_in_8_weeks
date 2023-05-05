## Troubleshooting tips
  * Lots of choice to use docker and kubernetes
  * One such and cool option is to use kind. [https://kind.sigs.k8s.io/"] KinD - Kubernetes in Docker!

Issue# 1:
  * kubectl get po -n kube-system
    The connection to the server localhost:8080 was refused - did you specify the right host or port?
  * Initial thinking is somehow kubectl isn't able to reach k8s api, which means configuarion might be missing
  # how to check the config availability?
    ```bash
    kubectl config view
    kubectl cluster-info
    
    if above commands either empty or no values assigned in config, copy admin.conf file to ~/.kube/config
    
    cp /etc/kubernetes/admin.conf ~/.kube/config
    ```
# Things to know:
* By default Kind creates a cluster named kind if you haven’t passed a cluster while creating the new one
* access control plane would be good choice
  ```bash
  docker exec -it kind-control-plane bash
  ```
* watch this space for more updates
