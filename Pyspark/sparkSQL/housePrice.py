__author__ = "ResearchInMotion"

import findspark
findspark.init()

from pyspark import SparkConf , SparkContext
from pyspark.sql import SparkSession ,SQLContext

sparksession = SparkSession.builder.appName("House Price").getOrCreate()

realestatedata = sparksession.read.\
     option("header" , "true")\
    .option("inferschema" , value=True)\
    .csv("/Users/sahilnagpal/PycharmProjects/Python/Pyspark/InputData/RealEstate.csv")

# reading the schema

print(realestatedata.printSchema())

# calculation

calculation = realestatedata.groupBy("Location").avg("Price SQ Ft").orderBy("avg(Price SQ Ft)").show()
print(calculation)

