# Yelp Business Reviews Analysis - End-to-End Data Pipeline

## 📊 Project Overview

An end-to-end data analytics project analyzing Yelp business reviews using Python, AWS S3, Snowflake, and SQL. This project demonstrates ETL pipeline development, cloud data warehousing, and business intelligence analysis.

## 🎯 Business Problem

Analyze Yelp's business review data to uncover insights about:
- Top-performing cities and businesses
- Review sentiment trends over time
- Business category performance
- Customer engagement patterns

## 🏗️ Architecture
```
Yelp JSON Data (5GB+)
    ↓
Python Script (Split into chunks)
    ↓
AWS S3 (Cloud Storage)
    ↓
Snowflake (Data Warehouse)
    ↓
SQL Analysis
    ↓
Business Insights
```

## 🛠️ Tech Stack

- **Languages**: Python, SQL
- **Cloud Platform**: AWS S3
- **Data Warehouse**: Snowflake
- **Libraries**: pandas, boto3, snowflake-connector-python
- **Tools**: VS Code, Git

## 🔑 Key Features

- ✅ Processed 5GB+ of JSON data
- ✅ Handled 6M+ review records
- ✅ Automated ETL pipeline with error handling
- ✅ Cloud-based data warehousing
- ✅ Scalable architecture for large datasets
- ✅ Comprehensive SQL analysis
