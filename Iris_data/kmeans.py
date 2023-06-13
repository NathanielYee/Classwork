'''
The k means clustering algorithm
'''
import csv
import random as rnd
import copy
import seaborn as sns
import matplotlib.pyplot as plt
from collections import defaultdict

def read_data(filename):
    '''Read CSv'''
    data = []
    classes = []
    with open(filename,'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) # skip header
        for row in reader:
            data.append(tuple(float(x) for x in row[:4]))
            classes.append(row[4])
    return data,classes


def pick_initial_centroids(data,k):
    '''picking k random data points as initial centroids'''
    return rnd.sample(data,k)


def kmeans(data,k):
    '''Perform k-means clustering
    data- our attribute data (list of tuples)
    k- the number of clusters
    return - list of k centroids'''
    # Step 1 pick k random points to be intial centroid
    centroids = pick_initial_centroids(data,k)
    # Step 2 Assign each poiont to a clubster by finding the nearest centroid

    # Step 3 adjust move each centroid by averaging the attribute values
    # of the points associated with that centroid


    # Step 4


    return centroids



def main():
    # read in the data
    data, classes = read_data('iris.dat')

    # cluster the data
    kmeans(data, k=5)

    # visualize the clusters to validate the result
    pass

if __name__ == '__main__':
    main()