**Arguments**
- Docker vs K8s
  - Entrypoint is override by command
  - CMD is override by args

<hr>

**POD**
- kubectl get po -A -o wide
- kubectl run nginx --image nginx
- kubectl describe po {pod_name}
- kubectl run redis --image=redis123 --dry-run=client -o yaml > redis.yaml
- kubectl get pod {pod_name} -o yaml > pod.yaml
- kubectl edit po nginx  # to edit image of pod vi editor will open
- kubectl run pod1 --image=nginx --port=80 --expose=true # because of expose a clusterip service also will be created with same name pod1 (in this case)
- kubectl logs {pod_name} -c {container-name}
- kubectl replace --force -f /tmp/kubectl-edit-***.yaml # to force replace the pod config
- kubectl get po -l env=dev # filter label

<hr>

**ServiceAccount**
- kubectl create serviceaccount {service_account_name}
- kubectl create token {service_account_name}
- <pre>
  spec:
    serviceAccountName: {some_name}
  </pre>
<hr>

**Taints & Tolerations**
- Taints

<hr>

**Config Map**
- v1
- ConfigMap
- kubectl create configmap {some_name} --from-literal=APP_COLOR=blue --from-literal=APP_MOD=prod
- kubectl create configmap {some_name} --from-file={path_of_file}
- envFrom:
  - configMapRef:
     name: app-config
- env:
  - name: APP_COLOR
    value-From:
        configMapKeyRef:
            name: app-config
            key: APP_COLOR
- volumes:
- name: app-config-volume
  configMap:
    name: app-config

<hr/>

**Rolling Updates**

- kubectl edit deploy {DeployName}

<hr/>

**Secrets**
- v1
- Secret
- Kubectl get secrets
- kubectl create secret generic db-secret --from-literal=DB_Host=host.com
- What are types of secrets?
  - Generic
  - Opaque
- envFrom:
    - secretRef:
        name: app-config
- env:
    - name: DB_Password
      valueFrom:
        secretKeyRef:
            name: app-secret
            key: DB_Password
- volume:
  - name: app-secret-volume
    secret:
        secretName: app-secret

<hr>

**Deployment**
- kubectl create -f  k8s/pod-d.yaml # for new deployment
- kubectl apply -f k8s/pod-d.yaml # for edit deployment
- kubectl create deployment {depl_name} --image=nginx --replicas=3
- kubectl set image {depl_name} {old-image} {new-image}


<hr>

**Replica Set**
- kubectl scale rs {rs_name} --replicas=5

<hr>

**Security**

-
  securityContext:
    runAsUser: 1000
    capabilities:
      add: ["MAC_ADMIN"]

<hr>

**Network-Policies**
- kubectl get netpol
-


<hr/>

**PersistantVolume**
- kubectl get netpol
- Can only be created via yaml


<hr/>

**Nodes**
- kubectl get nodes
- kubectl describe node node01
- kubectl taint nodes foo bar:NoSchedule-
- kubectl label node node01 color=blue
- kubectl top node # to check max used nodes. metrics server should be deployed first
- kubectl top pod
- <pre>
  tolerations:
    - key: spray
      value: mortein
      effect: NoSchedule
      operator: Equal
  </pre>
- <pre>
  nodeSelector:
    size: Large
  </pre>
- <pre>
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: size
            operator: In
            values:
            - Large
  </pre>
<hr>

**Resources**
-
  <pre>
  resources:
    requests:
      memory: "4Gi"
      cpu: 2
    limits:
      memory: "2Gi"
      cpu: 2
  </pre>

<hr>

**Ingress**
- controller + resources
- kubectl get ingress -A
- kubectl create ingress ingress-pay --rule="/pay=pay-service:8282"
- kubectl edit ingress ingress-pay
- kubectl get roles
- kubectl get rolebindings
-   annotations:
      nginx.ingress.kubernetes.io/rewrite-target: /

<hr>

**StorageClasses**
- kubectl get storageclasses

<hr>

**UserRoles**
- cat /etc/kubernetes/manifests/kube-apiserver.yaml
- ps -aux | grep authorization
- kubectl create role developer --verb=list,create,delete --resource=pods
- kubectl create rolebinding dev-user-binding --role=developer --user=dev-user

<hr>

**ClusterRolesAndBindings**
- kubectl get clusterroles
- kubectl get clusterrolebindings
- It is not bound to any namespace
- kubectl create clusterrole michelle-role --verb=get,list,watch --resource=nodes
- kubectl create clusterrolebinding michelle-role-binding --clusterrole=michelle-role --user=
michelle

<hr/>

**AdmissionController**
- kubectl exec -it kube-apiserver-controlplane -n kube-system -- kube-apiserver -h | grep 'enable-admission-plugins'
- Edit /etc/kubernetes/manifests/kube-apiserver.yaml and add NamespaceAutoProvision admission controller to --enable-admission-plugins list
- ps -ef | grep kube-apiserver | grep admission-plugins


<hr/>

**Miscellaneous**
- echo -n 'mysql' | base64 --decode
- kubectl api-resources -o wide
- kubectl exec {podname} -- {cmdname}
  - kubectl exec webapp -- cat /log/app.log
- kubectl explain pod.spec
- kubectl proxy 8001&

<hr/>

**KubeConfig**
- kubectl config get-contexts
- cat /root/.kube/config
-
<hr>

**Helm**
- helm --help
- helm search hub {PackageName}
- helm search repo {RepoName}
- helm pull --untar {PackageName}
- helm install {releaseName} {chartName}
- helm repo add {repoName} {repoPath}
<hr>

Questions?
- What are roles and rolebindings for service accounts
- How to set different context from different file # kubectl config
- How to check authorization modes


CHECK
- Service Accounts
- Ingress
- Roles
- Role Bindings
- kubectl-convert