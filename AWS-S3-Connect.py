import boto3
import pandas as pd
#from datetime import datetime, timedelta,timezone
#import calendar
import io

AWS_ACCESS_KEY_ID = 'XXXXXXXXXXXXXXXXXXXXXXX'
AWS_SECRET_ACCESS_KEY = 'YYYYYYYYYYYYYYYYYYYYYYYY'

BUCKET = 'your-bucket-name-here'
custPersona = None
file_format = 'csv' # parquet/csv/json etc

# for FILE_TO_READ refer the key in the metadata of the file in s3.

if file_format == 'csv':
    # To read csv
    FILE_TO_READ = 'path/to/your/csvfile/here/filenamehere.csv' #Refer key in your metadata of the file to be read in S3
    client = boto3.client('s3',
                       aws_access_key_id=AWS_ACCESS_KEY_ID,
                       aws_secret_access_key=AWS_SECRET_ACCESS_KEY
                     )
    result = client.get_object(Bucket=BUCKET, Key=FILE_TO_READ)
    custPersona = pd.read_csv(result['Body'])
elif file_format == 'parquet':
    # To read parquet
    buffer = io.BytesIO()
    FILE_TO_READ = 'path/to/your/csvfile/here/filenamehere.pq'
    session = boto3.Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
                       aws_secret_access_key=AWS_SECRET_ACCESS_KEY
                     )
    client = session.resource('s3')
    # To list all the files in a bucket with specified prefix as in regex
    # bucket = client.Bucket(BUCKET)
    # objs = list(bucket.objects.filter(Prefix=affnity_path))
    # objs
    result = client.Object(BUCKET, FILE_TO_READ)
    result.download_fileobj(buffer)
    custPersona = pd.read_parquet(buffer)
