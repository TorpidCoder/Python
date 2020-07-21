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
    country = field[3]
    name = field[2]
    return country,name

data = sparkcont.textFile("/Users/sahilnagpal/PycharmProjects/Python/Pyspark/InputData/airports.text")
airportsByCountry = data.map(columns).groupByKey()
for country , name in airportsByCountry.collectAsMap().items():
    print(country,":",list(name))