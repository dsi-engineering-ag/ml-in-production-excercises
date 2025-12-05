# Sustaino Prometheus Queries

## Find metric in your namespace only

```
eligible_total{namespace="test"}
```

## Find all sustaino eligibility metrics

```
{ __name__=~"not_eligible_total|eligible_total" }
```

## Find my susteino eligibility metrics

```
{__name__=~"not_eligible_total|eligible_total",namespace="florian"}
```
