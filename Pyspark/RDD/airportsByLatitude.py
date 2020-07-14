__author__ = "ResearchInMotion"

import findspark
findspark.init()
from pyspark import SparkConf
from pyspark import SparkContext

sparkconf = SparkConf().setAppName("WordCount").setMaster("local[*]")
sparkcont = SparkContext(conf=sparkconf)
sparkcont.setLogLevel("ERROR")

def columns(lines):
    field = lines.split(",")
    name = field[1]
    latitude = float(field[6])
    return name , latitude

data = sparkcont.textFile("/Users/sahilnagpal/PycharmProjects/Python/Pyspark/InputData/airports.text")
dataColumns = data.map(columns).filter(lambda latitude : latitude[1] >= 40).take(10)
print(dataColumns)
