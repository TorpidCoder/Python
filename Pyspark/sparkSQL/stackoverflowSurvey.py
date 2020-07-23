__author__ = "ResearchInMotion"

import findspark
findspark.init()

from pyspark.sql import SparkSession , SQLContext

sparksession = SparkSession.builder.appName("Stackoverflow").getOrCreate()

AGE_MIDPOINT = "age_midpoint"
SALARY_MIDPOINT = "salary_midpoint"
SALARY_MIDPOINT_BUCKET = "salary_midpoint_bucket"

stackoverflowdata = sparksession.read.option("header","True").option("inferschema" , True).csv("/Users/sahilnagpal/PycharmProjects/Python/Pyspark/InputData/2016-stack-overflow-survey-responses.csv")

#print schema
print(stackoverflowdata.printSchema())

responsewithSelectedColumns = stackoverflowdata.select("country","occupation",AGE_MIDPOINT , SALARY_MIDPOINT)


print("=== Print the selected columns of the table ===")
responsewithSelectedColumns.show()

print("=== Print records where the response is from Afghanistan ===")
responsewithSelectedColumns.filter(responsewithSelectedColumns["country"] == "Afghanistan").show()

print("=== Print the count of occupations ===")
groupeddata = responsewithSelectedColumns.groupBy("occupation")
groupeddata.count().show()

print("=== Print records with average mid age less than 20 ===")
responsewithSelectedColumns.filter(responsewithSelectedColumns[AGE_MIDPOINT] < 20).show()

print("=== Print the result by salary middle point in descending order ===")
responsewithSelectedColumns.orderBy(responsewithSelectedColumns[SALARY_MIDPOINT] , ascending=False).show()

print("=== Group by country and aggregate by average salary middle point ===")
groupbyCountry = responsewithSelectedColumns.groupBy("country")
groupbyCountry.avg(SALARY_MIDPOINT).orderBy("avg(salary_midpoint)",ascending=False).show()


