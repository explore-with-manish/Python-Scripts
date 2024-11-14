from pyspark.sql import SparkSession
from pyspark.sql.dataframe import DataFrame


def create_spark_session(app_name: str = "PySparkApp") -> SparkSession:
    """
    Creates and returns a SparkSession.
    """
    return SparkSession.builder.appName(app_name).getOrCreate()


def load_data(spark: SparkSession, file_path: str) -> DataFrame:
    """
    Loads a CSV file into a DataFrame.

    :param spark: SparkSession
    :param file_path: Path to the CSV file
    :return: DataFrame containing the CSV data
    """
    return spark.read.csv(file_path, header=True, inferSchema=True)


def filter_data_by_age(df: DataFrame, age_threshold: int) -> DataFrame:
    """
    Filters the DataFrame for rows where age is greater than the specified threshold.

    :param df: Input DataFrame
    :param age_threshold: Age threshold for filtering
    :return: Filtered DataFrame
    """
    return df.filter(df["age"] > age_threshold)


def group_by_city_and_count(df: DataFrame) -> DataFrame:
    """
    Groups the DataFrame by city and counts the number of people per city.

    :param df: Input DataFrame
    :return: DataFrame with counts per city
    """
    return df.groupBy("city").count()


def main():
    # Initialize SparkSession
    spark = create_spark_session("ModularPySparkExample")

    # Load data
    file_path = "people.csv"  # Replace with your file path
    df = load_data(spark, file_path)

    # Filter data
    filtered_df = filter_data_by_age(df, 30)

    # Group and count by city
    result_df = group_by_city_and_count(filtered_df)

    # Show the result
    result_df.show()

    # Stop the Spark session
    spark.stop()


# Run the main function
if __name__ == "__main__":
    main()
