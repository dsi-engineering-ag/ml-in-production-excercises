# Setup

In order to be able to do the excercises, a kubernetes cluster is required.

## Prepare Cluster

- Create GKE standard cluster

## Prepare Gateway

### Install Envoy Gateway

```bash
kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.1.0/standard-install.yaml
```

```bash
# Add the Helm repo (if you haven't already)
helm install eg oci://docker.io/envoyproxy/gateway-helm \
  --version v1.2.0 \
  -n envoy-gateway-system \
  --create-namespace
```

```bash
kubectl wait --timeout=5m -n envoy-gateway-system deployment/envoy-gateway --for=condition=Available
```

### Create ML in Prod Gateway

```bash
kubectl apply -f setup/mlprod-gateway.yml
```

## Install Prometheus

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus prometheus-community/kube-prometheus-stack --create-namespace --namespace monitoring
```

## Configure scraping

```bash
k apply -f setup/monitoring-selector.yml
```

## Expose Prometheus

```bash
k apply -f setup/prometheus-ingress.yml
```

## TODO Excercise

Monitoring: update pod labels

```yaml
monitor: "true"
```

Update deployment exercises
