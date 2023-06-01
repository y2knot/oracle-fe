import boto3
import pandas 

# # Download a file from S3
with open("data/busd.csv", "wb") as data:
    s3.download_fileobj('knot-bucket', 'y2k/oracles/busd.csv', data)

with open("data/dai.csv", "wb") as data:
    s3.download_fileobj('knot-bucket', 'y2k/oracles/dai.csv', data)

with open("data/frax.csv", "wb") as data:
    s3.download_fileobj('knot-bucket', 'y2k/oracles/frax.csv', data)

with open("data/mai.csv", "wb") as data:
    s3.download_fileobj('knot-bucket', 'y2k/oracles/mai.csv', data)

with open("data/mim.csv", "wb") as data:
    s3.download_fileobj('knot-bucket', 'y2k/oracles/mim.csv', data)

with open("data/usdc.csv", "wb") as data:
    s3.download_fileobj('knot-bucket', 'y2k/oracles/usdc.csv', data)

with open("data/usdt.csv", "wb") as data:
    s3.download_fileobj('knot-bucket', 'y2k/oracles/usdt.csv', data)

with open("data/wbtc.csv", "wb") as data:
    s3.download_fileobj('knot-bucket', 'y2k/oracles/wbtc.csv', data)
