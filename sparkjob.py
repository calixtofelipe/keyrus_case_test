from pyspark.sql import SparkSession


def read_2_spark():

    spark = SparkSession.builder.appName("teste").getOrCreate()
    dataframe = spark.read.json("/database/teste.json")


read_2_spark()