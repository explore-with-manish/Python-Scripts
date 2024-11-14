from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder.appName("SparkSQLExample").getOrCreate()

# Load the data
df = spark.read.csv("people.csv", header=True, inferSchema=True)

# Register the DataFrame as a temporary view
df.createOrReplaceTempView("people")

# Perform transformations using Spark SQL
query = """
    SELECT city, COUNT(*) AS count
    FROM people
    WHERE age > 30
    GROUP BY city
"""
result_df = spark.sql(query)

# Show the result
result_df.show()
