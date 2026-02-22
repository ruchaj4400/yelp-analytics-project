
COPY INTO yelp_reviews
FROM 's3://namastesql/yelp/'
CREDENTIALS = (
    AWS_KEY_ID = '***************'
    AWS_SECRET_KEY = '**************'
)
FILE_FORMAT = (TYPE = JSON);

COPY INTO yelp_businesses
FROM 's3://namastesql/yelp/yelp_academic_dataset_business.json'
CREDENTIALS = (
    AWS_KEY_ID = '********'
    AWS_SECRET_KEY = '****************'
)
FILE_FORMAT = (TYPE = JSON);