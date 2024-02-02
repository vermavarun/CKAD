**POD**
- kubectl get po -A -o wide
- kubectl run nginx --image nginx
- kubectl describe po <pod_name>
- kubectl run redis --image=redis123 --dry-run=client -o yaml > redis.yaml
- kubectl get pod <pod_name> -o yaml > pod.yaml
- kubectl edit po nginx  # to edit image of pod vi editor will open

**Deployment**
- kubectl create -f  k8s/pod-d.yaml # for new deployment
- kubectl apply -f k8s/pod-d.yaml # for edit deployment
- kubectl create deployment <depl_name> --image=nginx --replicas=3

**Replica Set**
- kubectl scale rs <rs_name> --replicas=5

**Ingress**
- controller + resources
