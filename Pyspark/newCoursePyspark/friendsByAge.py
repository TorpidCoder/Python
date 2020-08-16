__author__ = "ResearchInMotion"

import findspark

findspark.init()

from pyspark import SparkConf, SparkContext

sparkconf = SparkConf().setMaster("local[*]").setAppName("Friends By Name")
sparkcont = SparkContext(conf=sparkconf)
sparkcont.setLogLevel("ERROR")


def meanColumns(line):
    field = line.split(",")
    age = int(field[2])
    friendsCount = int(field[3])
    return age, friendsCount


data = sparkcont.textFile(
    "/Users/sahilnagpal/PycharmProjects/Python/Pyspark/newCoursePyspark/inputData/fakefriends.csv")
friendsByAgedata = data.map(meanColumns).mapValues(lambda x: (x, 1)).reduceByKey(
    lambda x, y: (x[0] + y[0], x[1] + y[1])).mapValues(lambda x : x[0]/x[1])


for values in friendsByAgedata.collect():
    print(values)
