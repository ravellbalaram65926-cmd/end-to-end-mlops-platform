"""ETL demo: normalize churn data into a versionable model feature table."""

import argparse
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data" / "raw" / "sample_churn.csv"
DEFAULT_OUTPUT = ROOT / "data" / "gold" / "churn_features.csv"


def build_features(input_path: Path) -> list[dict[str, str]]:
    with input_path.open(newline="", encoding="utf-8") as source:
        rows = list(csv.DictReader(source))
    result = []
    seen = set()
    for row in rows:
        customer_id = row["customer_id"].strip()
        if not customer_id or customer_id in seen:
            continue
        seen.add(customer_id)
        tenure = int(row["tenure_months"])
        charges = float(row["monthly_charges"])
        churn = row["churn"].strip().lower()
        if tenure < 0 or charges < 0 or churn not in {"yes", "no"}:
            raise ValueError(f"Invalid source record for customer {customer_id}")
        row.update(
            {
                "customer_id": customer_id,
                "contract": row["contract"].strip().lower(),
                "monthly_charges": f"{charges:.2f}",
                "tenure_bucket": "new" if tenure < 6 else "established" if tenure < 24 else "loyal",
                "churn_label": str(int(churn == "yes")),
                "estimated_lifetime_charges": f"{tenure * charges:.2f}",
            }
        )
        result.append(row)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    rows = build_features(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as target:
        writer = csv.DictWriter(target, fieldnames=list(rows[0]) if rows else [])
        if rows:
            writer.writeheader()
            writer.writerows(rows)
    print(f"Built {len(rows)} churn feature rows at {args.output}")


if __name__ == "__main__":
    main()
