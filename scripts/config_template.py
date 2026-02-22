"""
Configuration template for AWS and Snowflake credentials
"""

# AWS S3 Configuration
AWS_ACCESS_KEY_ID = "your_aws_access_key_here"
AWS_SECRET_ACCESS_KEY = "your_aws_secret_key_here"
AWS_REGION = "us-east-1"  # Change to your region
S3_BUCKET_NAME = "your-s3-bucket-name"
S3_FOLDER = "yelp-data"

# Snowflake Configuration
SNOWFLAKE_ACCOUNT = "your-account-identifier"  # e.g., "abc12345.us-east-1"
SNOWFLAKE_USER = "your_username"
SNOWFLAKE_PASSWORD = "your_password"
SNOWFLAKE_WAREHOUSE = "COMPUTE_WH"
SNOWFLAKE_DATABASE = "YELP_DB"
SNOWFLAKE_SCHEMA = "PUBLIC"

# File paths
DATA_FOLDER = "../data"
SPLIT_FILES_FOLDER = "../data/split_files"