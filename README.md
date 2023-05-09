# minikube experimentation in k8s
- purpose: create apps, deploy via argocd, experiment with k8 config, learn stuff

## repo structure: (local dev, keep things simple)
- apps (contains applications with docker logic for pushing to local registry)
- system (contains k8 cluster-wide configuration configs)
- argocd? (should contain just argocd install and apps config yamls)

## repo structure: (for production, should look like?)
- apps (individual application repo's in github, ex: https://github.com/Dslate88/tf-aws-django-website)
- system? (this repo/approach likely ideal?)
- argocd (this repo/approach likely ideal, since argocd is running on the k8 cluster it serves it should be seen as core to its config?)

## getting started:
create/start cluster:
- `minikube start`

install argocd cli:
- `brew install argocd`

apply pre-requisite configs:
- `kubectl apply -f argo-namespace.yaml`

argocd installation non-ha
- `kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml`

### dev stuff to rememeber..
port-forwarding argocd-server:
kubectl port-forward svc/argocd-server -n argocd 8080:443
`https://localhost:8080` or `argocd login localhost:8080` for login

argocd-server un/pw (ui and cli):
- un: admin
- pw: `argocd admin initial-password -n argocd`

expose clusterIP service for an app: (todo app example)
- kubectl port-forward service/todo-app 8000:80
