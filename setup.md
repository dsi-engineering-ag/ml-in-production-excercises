# Prepare Kubernetes Cluster

## Install Seldon Core


1. Instal Ambassador

Update documentation: 
https://www.getambassador.io/docs/edge-stack/3.3/tutorials/getting-started


2. Install Seldon Core with Ambassador: https://docs.seldon.io/projects/seldon-core/en/latest/examples/seldon_core_setup.html


helm install seldon-core seldon-core-operator \
    --repo https://storage.googleapis.com/seldon-charts \
    --set usageMetrics.enabled=true \
    --set ambassador.enabled=true \
    --namespace seldon-system

3. Install Seldon Core Analytics

https://docs.seldon.io/projects/seldon-core/en/latest/analytics/analytics.html#installation

helm upgrade --install seldon-monitoring kube-prometheus \
    --version 6.9.5 \
    --set fullnameOverride=seldon-monitoring \
    --namespace seldon-monitoring \
    --repo https://charts.bitnami.com/bitnami

4. Create Ambassador Listener: setup/*.yml
5. Get Ambassador IP (Loadbalancer Service) and configure dsi DNS: mlproduction.dsiag.ch
6. Create Graphana Ingress and configure dsi DNS: monitoring.mlproduction.dsiag.ch