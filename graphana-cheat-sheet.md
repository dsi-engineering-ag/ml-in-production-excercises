# Sustaino Graphana/Prometheus Queries

## Find all sustaino eligibility metrics

```
{ __name__=~"not_eligible_total|eligible_total" }
```

## Find my susteino eligibility metrics

``` 
{__name__=~"not_eligible_total|eligible_total",kubernetes_namespace="florian"}
``` 

## Find Rate Seldon API Requests 

```
rate(seldon_api_executor_client_requests_seconds_sum[5m])
```