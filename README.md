# SQL Data Pipeline Project

## Project Overview
This project is a small-scale **data engineering pipeline** that generates, loads, and analyzes a synthetic dataset using Python and SQL. It demonstrates advanced SQL concepts, data modeling, and programmatic data generation.

The project includes:
- Python scripts to generate synthetic data.
- A relational schema with three tables: `users`, `products`, `orders`.
- Loading the data into a DuckDB database.
- 50+ SQL queries demonstrating joins, aggregations, window functions, CTEs, and subqueries.
- Analysis notebook with business insights.

---

## Folder Structure

SQL_pipeline_project/
│
├── scripts/ # Python scripts for data generation and loading
│ ├── generate_data.py
│ └── load_data.py
├── sql/ # SQL queries
│ └── analysis_queries.sql
├── notebooks/ # Jupyter notebook for analysis
│ └── analysis.ipynb
├── data/ # Generated CSV files (ignored by Git)
├── README.md # Project documentation
├── requirements.txt # Python dependencies
└── .gitignore # Files to ignore in Git


---

## Requirements
- Python 3.8+
- duckdb
- pandas
- faker
- jupyter

Install dependencies with:
```bash
pip install -r requirements.txt

1.Setup Instructions
Clone the repository
git clone https://github.com/Divyasrirowtu/SQL_pipeline_project.git
cd SQL_pipeline_project

2.Set up a virtual environment
python -m venv venv
source venv/Scripts/activate    # Windows

3.Install dependencies
pip install -r requirements.txt

4.Generate synthetic data
python scripts/generate_data.py


5.Load data into DuckDB
python scripts/load_data.py

5.Run SQL queries or analyze in the notebook
jupyter notebook

Notes
data/ folder and database files are ignored in GitHub via .gitignore
The project is fully reproducible from scratch.