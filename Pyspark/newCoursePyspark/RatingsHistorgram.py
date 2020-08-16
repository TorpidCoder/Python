__author__ = "ResearchInMotion"

import findspark
findspark.init()

from pyspark import SparkConf , SparkContext
import collections

sparkconf = SparkConf().setMaster("local[*]").setAppName("Histogram Data")
sparkcont = SparkContext(conf=sparkconf)
sparkcont.setLogLevel("ERROR")

def ratingsFetch(line):
    field = line.split()
    ratings = field[2]
    return ratings

data = sparkcont.textFile("/Users/sahilnagpal/PycharmProjects/Python/Pyspark/newCoursePyspark/inputData/u.data")
ratings = data.map(ratingsFetch)
groupbyRatings = ratings.countByValue()


sortedgroupbyRatings = collections.OrderedDict(sorted(groupbyRatings.items()))
for key , value in sortedgroupbyRatings.items():
    print(key , value)


