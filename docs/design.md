# Design

For governance, I will give you a simple data pipeline naming design and you can
this be the baseline for the next generation.

## Stream

```text
s_<system>_<frequency>
```

```text
s_cm_d
```

Monitoring:

- Able to know want data that this stream handle, it handles `cm` data source.
- Able to know workflow frequency, this run with `daily` frequency.
