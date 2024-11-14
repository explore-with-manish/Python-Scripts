from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder.appName("PySparkExample").getOrCreate()

# Load the data
df = spark.read.csv("people.csv", header=True, inferSchema=True)

# Perform transformations using PySpark DataFrame API
filtered_df = df.filter(df["age"] > 30)  # Filter age > 30
result_df = filtered_df.groupBy("city").count()  # Group by city and count

# Show the result
result_df.show()
