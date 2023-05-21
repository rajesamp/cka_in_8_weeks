## Node Affinity challenge

# scenario:
* Need to deploy pod in controlplane
* What are possibilities and challenges during deploying the pod?
* Discussed in below terminal session playback

```
In the namespace named 012963bd , create a pod named az1-pod which uses the nginx:1.24.0 image. This pod should use node affinity, and prefer during scheduling to be placed on the node with the label availability-zone=zone1 with a weight of 80.

Also, have that same pod prefer to be scheduled to a node with the label availability-zone=zone2 with a weight of 20.

NOTE: Make sure the container remains in a running state
Ensure that the pod is scheduled to the controlplane node.
```

[![asciicast](https://asciinema.org/a/3R3MLOVd7GnnXe7cP6ghBrAin.svg)](https://asciinema.org/a/3R3MLOVd7GnnXe7cP6ghBrAin)

Challenge is solved:

![Screenshot 2023-05-20 at 10 52 07 PM](https://github.com/rajesh-sampathrajan/cka_in_8_weeks/assets/111441779/4f861b46-87ca-4e9e-a445-be82159177a7)
