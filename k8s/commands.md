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
- kubectl logs {pod_name}

<hr>

**Service-Account**
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

<hr>


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

**Nodes**
- kubectl get nodes
- kubectl describe node node01
- kubectl taint nodes foo bar:NoSchedule-
- kubectl label node node01 color=blue
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

<hr>

**Miscellaneous**
- echo -n 'mysql' | base64 --decode
- kubectl api-resources -o wide
- kubectl exec {podname} -- {cmdname}
- kubectl explain pod.spec

<hr>
