# End-to-End MLOps Platform

## Problem
Train, deploy and monitor a customer churn model in a repeatable, automated workflow.

## Dataset and provenance

`data/raw/sample_churn.csv` is a small synthetic fixture. For a real example, obtain the [IBM Telco Customer Churn dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) and follow its dataset license/terms. Store private downloads under ignored `data/external/`, never commit raw customer data.

## Run the ETL demo

From this directory, `python src/main.py` validates IDs, numeric values and labels, deduplicates customer records and builds normalized churn features in `data/gold/churn_features.csv`. Use `--input` and `--output` to set alternative paths. Feature generation is deterministic and can be re-run safely.

Run checks with `python -m pytest -q tests`.

## Stack
Airflow, MLflow, Docker, FastAPI, GitHub Actions, Evidently

## Architecture
- Bronze / raw ingestion layer
- Silver / cleaned and validated data layer
- Gold / feature or serving layer
- Monitoring / validation and retraining feedback loop

## DE tasks
1. Ingest raw data with versioned file naming and timestamps.
2. Build idempotent and incremental transformations.
3. Add data quality checks and freshness alerts.
4. Create a reproducible run order using a Makefile or run script.
5. Store outputs in a warehouse, lake, or streaming sink with clear contracts.

## DS tasks
1. Run EDA and validate assumptions about seasonality, drift, and user behavior.
2. Benchmark a baseline model before trying a stronger approach.
3. Use proper time-based splits and avoid leakage.
4. Log experiments, tuning choices and key metrics.
5. Report limitations and next steps in a production-focused way.

## Deliverables
- Reproducible pipeline or app
- Tests for transformation and validation logic
- Dashboard, API, or report showing outputs
- Clear business summary with measurable impact

## Recommended repository structure
`	ext
end-to-end-mlops-platform/
+-- README.md
+-- requirements.txt
+-- Makefile
+-- .gitignore
+-- src/
+-- tests/
+-- notebooks/
+-- docs/
`

## Resume line
Built an automated training-to-serving MLOps pipeline with CI/CD, model registry and drift monitoring.
