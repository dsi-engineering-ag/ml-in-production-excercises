# Sustaino Graphana/Prometheus Queries

## Find all sustaino eligibility metrics

```
{ __name__=~"not_eligible|eligible" }
```

## Find my susteino eligibility metrics

``` 
{__name__=~"not_eligible_total|eligible_total",kubernetes_namespace="florian"}
``` 