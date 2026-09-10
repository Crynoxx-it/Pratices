import requests
import json
import looging

pyspark.sql import SparkSession
spark=SparkSession.builder.appName("test").getOrCreate()

response= requests.get("http:/hi/heloo")
data=response.json

print(f"data successfull initead{data} to s3")
df=spark.createDataFrame(data)
df.PrintSchema()
df.Show(5)

