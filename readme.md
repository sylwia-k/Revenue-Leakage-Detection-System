Olist E-Commerce Data Analysis

Project Overview

This project analyzes the Brazilian Olist e-commerce dataset using PostgreSQL, SQL and Python.

The goal is to transform raw CSV data into business insights related to sales, customers, products, sellers, delivery performance and customer reviews.

Business Questions
The analysis focuses on questions such as:

- What is the total revenue and average order value?
- How does revenue change over time?
- Which product categories generate the most revenue?
- Which sellers generate the most revenue?
- What percentage of orders are delivered late?
- Does late delivery affect customer review scores?
- Which sellers have the most problematic orders?
- Which orders have unusually high freight costs?
- What percentage of orders are cancelled?
- Which product categories have the lowest sales?

Tech Stack:

Python
PostgreSQL
SQL
Pandas
SQLAlchemy
Matplotlib
Seaborn
python-dotenv

The project calculates:

- total orders
- total revenue
- average order value
- monthly revenue
- revenue by product category
- seller revenue

The project analyzes:

- delivered orders
- delayed orders
- delayed order percentage
- delay duration
- delivery status

The project analyzes:

- review score distribution
- average review score
- relationship between delivery performance and review scores

The project identifies:

- top sellers by revenue
- sellers with problematic orders
- sellers with high freight costs
- sellers with low review scores


Example Business Insight

After running the analysis, the results can be used to identify relationships such as:

Are delayed orders associated with lower customer review scores?

The final conclusions should be based on the actual results generated from the database.

Installation

Clone the repository and create a virtual environment:
python -m venv .venv

Activate it on Windows:
.venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Database Configuration
Create a PostgreSQL database and configure the .env file.

Do not commit .env to GitHub.

Running the Project
From the project root:

python -m src.main

The project will connect to PostgreSQL, execute the analysis queries and display the results in the terminal.

Visualizations
The next stage of the project is to generate charts from the analysis results.

Planned visualizations include:
Monthly Revenue
Revenue by Product Category
Top Sellers
Order Status Distribution
Delivery Delay Rate
Review Score Distribution
Delivery Status vs Review Score
Freight Cost vs Product Price

Charts will be stored in:
reports/figures/

Portfolio Goal
This project demonstrates an end-to-end data analysis workflow:

SQL + PostgreSQL -> Python + Pandas -> Data Analysis -> Visualization -> Business Insights

The focus is not only on writing queries, but also on translating the results into useful business conclusions.