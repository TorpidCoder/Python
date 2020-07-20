__author__ = "ResearchInMotion"

import findspark
findspark.init()

from pyspark import SparkContext , SparkConf
sparkconf = SparkConf().setMaster("local[*]").setAppName("Sorted Word Count")
sparkcont = SparkContext(conf=sparkconf)
sparkcont.setLogLevel("ERROR")

def requiredColumn(line):
    field = line.split(",")
    price = float(field[2])
    bedroom = field[3]
    return  bedroom , price

data = sparkcont.textFile("/Users/sahilnagpal/PycharmProjects/Python/Pyspark/InputData/RealEstate.csv")
mainData = data.map(requiredColumn)
averageHousePrice = mainData.mapValues(lambda value : (value,1)).reduceByKey(lambda a,b : (a[0] + b[0] , a[1] , b[1])).mapValues(lambda values : values[0]/values[1]).sortByKey()

for values in averageHousePrice.collect():
    print(values)
