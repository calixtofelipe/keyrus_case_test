from pyspark.sql import SparkSession
from pyspark import SparkFiles
from config import FTP_FILE, FTP_FOLDER, FTP_URL, FTP_USER, FTP_PASSWORD, FTP_DATASOURCE
import zipfile


def read_2_spark():
    spark = SparkSession.builder.appName("spark_download").getOrCreate()
    # sc = spark.sparkContext
    # sc.addFile(FTP_DATASOURCE)
    """
    with open(SparkFiles.get(FTP_DATASOURCE)) as testFile:
        with zipfile.ZipFile(testFile, "r") as zipped:
            zipped.extractall("")
    """


read_2_spark()