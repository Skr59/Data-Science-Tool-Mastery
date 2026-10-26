import sqlite3
from contextlib import closing
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = PROJECT_ROOT / "data" / "raw_data.csv"
DATABASE_PATH = PROJECT_ROOT / "data" / "database.db"
TABLE_NAME = "housing_data"


def main() -> None:
    if not CSV_PATH.is_file():
        raise FileNotFoundError(f"CSV dataset not found: {CSV_PATH}")
    if CSV_PATH.stat().st_size == 0:
        raise ValueError(f"CSV dataset is empty: {CSV_PATH}")

    data = pd.read_csv(CSV_PATH)
    if data.empty:
        raise ValueError(f"CSV dataset contains no rows: {CSV_PATH}")

    with closing(sqlite3.connect(DATABASE_PATH)) as connection:
        with connection:
            data.to_sql(TABLE_NAME, connection, if_exists="replace", index=False)
            stored_row_count = connection.execute(
                f"SELECT COUNT(*) FROM {TABLE_NAME}"
            ).fetchone()[0]
            if stored_row_count != len(data):
                raise RuntimeError(
                    f"Expected {len(data)} rows in {TABLE_NAME}, "
                    f"but found {stored_row_count}."
                )

            preview = pd.read_sql_query(
                f"SELECT * FROM {TABLE_NAME} LIMIT 5", connection
            )

    print(f"Loaded and verified {stored_row_count:,} rows in '{TABLE_NAME}'.")
    print(f"SQLite database: {DATABASE_PATH}")
    print("First five rows:")
    print(preview.to_string(index=False))


if __name__ == "__main__":
    main()
