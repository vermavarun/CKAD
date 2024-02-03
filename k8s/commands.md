**POD**
- kubectl get po -A -o wide
- kubectl run nginx --image nginx
- kubectl describe po <pod_name>
- kubectl run redis --image=redis123 --dry-run=client -o yaml > redis.yaml
- kubectl get pod <pod_name> -o yaml > pod.yaml
- kubectl edit po nginx  # to edit image of pod vi editor will open
- kubectl run pod1 --image=nginx --port=80 --expose=true # because of expose a clusterip service also will be created with same name pod1 (in this case)

**Service**

**Deployment**
- kubectl create -f  k8s/pod-d.yaml # for new deployment
- kubectl apply -f k8s/pod-d.yaml # for edit deployment
- kubectl create deployment <depl_name> --image=nginx --replicas=3

**Replica Set**
- kubectl scale rs <rs_name> --replicas=5

**Ingress**
- controller + resources
