# "sfURL": "fh76732.ap-south-1.aws.snowflakecomputing.com",
#     "sfAccount": "fh76732.ap-south-1.aws",
#     "sfUser": "Swarnali",
#     "sfPassword": "Swarnali@123",

from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import *
from pyspark import SparkConf, SparkContext

sc = SparkContext("local", "Simple App")
spark = SQLContext(sc)
spark_conf = SparkConf().setMaster('local').setAppName('<APP_NAME>')

# You might need to set these
# sc._jsc.hadoopConfiguration().set("fs.s3n.awsAccessKeyId", "<AWS_KEY>")
# sc._jsc.hadoopConfiguration().set("fs.s3n.awsSecretAccessKey", "<AWS_SECRET>")

# Set options below
sfOptions = {
  "sfURL" : "fh76732.ap-south-1.aws.snowflakecomputing.com",
  "sfUser" : "Swarnali",
  "sfPassword" : "Swarnali@123",
  "sfDatabase" : "DEMO",
  "sfSchema" : "DBO",
  "sfWarehouse" : "Compute_WH"
}

SNOWFLAKE_SOURCE_NAME = "net.snowflake.spark.snowflake"

df = spark.read.format(SNOWFLAKE_SOURCE_NAME) \
  .options(**sfOptions) \
  .option("query",  "SELECT * FROM EMP") \
  .load()

df.show()