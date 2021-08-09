# Prepare Kubernetes Cluster

## Install Seldon Core


1. Instal Ambassador: https://github.com/datawire/ambassador-docs/blob/master/docs/edge-stack/1.4/topics/install/install-ambassador-oss.md 
2. Install Seldon Core with Ambassador: https://docs.seldon.io/projects/seldon-core/en/latest/examples/seldon_core_setup.html

helm install seldon-core seldon-core-operator \
    --repo https://storage.googleapis.com/seldon-charts \
    --set usageMetrics.enabled=true \
    --set ambassador.enabled=true \
    --namespace seldon-system

3. Install Seldon Core Analytics

helm install seldon-core-analytics seldon-core-analytics \
   --repo https://storage.googleapis.com/seldon-charts \
   --namespace seldon-system


4. Get Ambassador IP and configure dsi DNS: mlproduction.dsiag.ch
5. Create Graphana Ingress and configure dsi DNS: monitoring.mlproduction.dsiag.ch