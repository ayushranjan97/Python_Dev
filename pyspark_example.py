from pyspark.sql import SparkSession
spark = SparkSession \
    .builder \
    .appName("how to read csv file") \
    .getOrCreate()
print(spark.version)
df = spark.read.csv('emp.csv',header=True)
df.show()