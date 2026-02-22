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

## 📁 Project Structure
```
yelp-analytics-project/
├── scripts/
│   ├── 01_split_json.py          # Split large JSON into smaller files
│   ├── 02_upload_to_s3.py        # Upload data to S3
│   └── config_template.py        # Configuration template
├── sql/
│   ├── 01_create_tables.sql      # Snowflake table creation
│   ├── 02_load_data.sql          # Load data from S3
│   └── 03_analysis_queries.sql   # Business analysis queries
├── images/
│   └── architecture_diagram.png  # Project architecture
├── requirements.txt              # Python dependencies
├── .gitignore                   # Files to exclude from Git
└── README.md                    # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- AWS Account with S3 access
- Snowflake Account
- Yelp Dataset (download from [Yelp Dataset](https://www.yelp.com/dataset))


## 🔑 Key Features

- ✅ Processed 5GB+ of JSON data
- ✅ Handled 6M+ review records
- ✅ Automated ETL pipeline with error handling
- ✅ Cloud-based data warehousing
- ✅ Scalable architecture for large datasets
- ✅ Comprehensive SQL analysis

## 📚 Lessons Learned

- Splitting large files significantly improves upload and processing speed
- Snowflake's VARIANT data type is powerful for semi-structured JSON
- AWS S3 integration with Snowflake enables seamless data loading
- Proper indexing and partitioning critical for query performance

## 🎓 Skills Demonstrated

- ETL Pipeline Development
- Cloud Data Engineering (AWS, Snowflake)
- Python Scripting for Data Processing
- SQL Analytics and Optimization
- Data Modeling (star schema)
- Version Control (Git/GitHub)

## 🔮 Future Enhancements

- [ ] Add Apache Airflow for workflow orchestration
- [ ] Implement data quality checks with Great Expectations
- [ ] Build interactive dashboard with Power BI/Tableau
- [ ] Add sentiment analysis using NLP
- [ ] Automate daily incremental loads
- [ ] Implement CI/CD pipeline
