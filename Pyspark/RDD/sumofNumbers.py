__author__ = "ResearchInMotion"

import findspark
findspark.init()
from pyspark import SparkConf
from pyspark import SparkContext

sparkconf = SparkConf().setAppName("WordCount").setMaster("local[*]")
sparkcont = SparkContext(conf=sparkconf)
sparkcont.setLogLevel("ERROR")

data = sparkcont.textFile("/Users/sahilnagpal/PycharmProjects/Python/Pyspark/InputData/prime_nums.text")
numbers = data.flatMap(lambda numbers : numbers.split("\t"))
integernumbers = numbers.map(lambda numbers : int(numbers)).reduce(lambda a,b : a+b)
print(integernumbers)