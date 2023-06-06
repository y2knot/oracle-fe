import boto3
import pandas as pd
import os
from io import StringIO

AWS_KEY = os.environ['AWS_KEY']
AWS_SECRET = os.environ['AWS_SECRET']

s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_KEY,
    aws_secret_access_key=AWS_SECRET,
    region_name='us-east-1'
)

# # # Download a file from S3
# with open("data/busd.csv", "wb") as data:
#     s3.download_fileobj('knot-bucket', 'y2k/oracles/busd.csv', data)
    
# with open("data/dai.csv", "wb") as data:
#     s3.download_fileobj('knot-bucket', 'y2k/oracles/dai.csv', data)

# with open("data/frax.csv", "wb") as data:
#     s3.download_fileobj('knot-bucket', 'y2k/oracles/frax.csv', data)

# with open("data/mai.csv", "wb") as data:
#     s3.download_fileobj('knot-bucket', 'y2k/oracles/mai.csv', data)

# with open("data/mim.csv", "wb") as data:
#     s3.download_fileobj('knot-bucket', 'y2k/oracles/mim.csv', data)

# with open("data/usdc.csv", "wb") as data:
#     s3.download_fileobj('knot-bucket', 'y2k/oracles/usdc.csv', data)

# with open("data/usdt.csv", "wb") as data:
#     s3.download_fileobj('knot-bucket', 'y2k/oracles/usdt.csv', data)

# with open("data/wbtc.csv", "wb") as data:
#     s3.download_fileobj('knot-bucket', 'y2k/oracles/wbtc.csv', data)

ticker_list = ['busd', 'dai', 'frax', 'mai', 'mim', 'usdc', 'usdt', 'wbtc', 'usdd']
for ticker in ticker_list:
    obj = s3.get_object(Bucket='knot-bucket', Key=f'y2k/oracles/{ticker}.csv')
    data = obj['Body'].read().decode('utf-8')
    df = pd.read_csv(StringIO(data))
    df.to_csv(f'data/{ticker}.csv')

