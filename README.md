# Data Science Tool Mastery

## Objective
Demonstrate proficiency in industry-standard Data Science tools by building an end-to-end relational database and predictive modeling pipeline, moving beyond basic flat-file analysis to robust data engineering and machine learning workflows.

## Problem Statement
Traditional data science workflows often rely entirely on flat CSV files and ad-hoc scripts. This project implements a production-grade pipeline that ingests raw data into a local SQLite database, executes programmatic SQL queries for data retrieval, performs rigorous preprocessing, and trains a baseline Scikit-learn predictive model with structured reproducibility.

## Tool Stack
- **Python & Pandas / NumPy:** Data manipulation and feature engineering.
- **SQLite & SQL:** Relational database storage and programmatic querying.
- **Scikit-learn:** Preprocessing pipelines and baseline machine learning modeling.
- **Matplotlib & Seaborn:** Exploratory data analysis and evaluation visualization.
- **Git & GitHub:** Version control and portfolio project structure.

## Project Structure
```text
Data-Science-Tool-Mastery/
├── data/
│   ├── raw_data.csv            # Source dataset
│   └── database.db             # Local SQLite database
├── notebooks/
│   └── 01_exploratory_analysis.ipynb
├── src/
│   ├── database_loader.py      # SQLite ingestion and query script
│   └── model_pipeline.py       # Preprocessing and ML modeling script
├── reports/
│   └── figures/                # Saved visualizations
├── README.md
└── requirements.txt
```

## Setup & Reproducibility

1. Clone the repository and navigate to the project root.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Load and verify the CSV data in SQLite:

   ```bash
   python src/database_loader.py
   ```