'''
The k means clustering algorithm
'''
import csv
import random as rnd
import copy

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import defaultdict


def read_data(filename):
    '''Read CSV'''
    data = []
    classes = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header
        for row in reader:
            data.append(tuple(float(x) for x in row[:4]))
            classes.append(row[4])
    return data,classes


def pick_initial_centroids(data, k):
    '''picking k random data points as initial centroids'''
    return rnd.sample(data, k)


def euclidean(p1, p2):
    '''Compute the euclidean distance'''
    return sum([(x1 - x2) ** 2 for x1, x2 in zip(p1, p2)])


def closest(centroids, point, dfunc):
    '''Determine the closest centroid for one point
    using the specified distance function dfunc'''
    nearest = 0
    nearest_dist = dfunc(centroids[0], point)

    for c in range(1, len(centroids)):
        dist = dfunc(centroids[c], point)
        if dist < nearest_dist:
            nearest = c
            nearest_dist = dist
    return nearest


def find_closest_centroid(centroids, data, dfunc):
    '''For each data point find the closest centroid
    centrois the list of centrois
    data our dat set
    dfunc distance function
    return a dict (centroid-->list of points)'''
    cdict = defaultdict(list)
    for point in data:
        c = closest(centroids, point, dfunc)
        cdict[c].append(point)
    return cdict


def adjust_centroid(cdict):
    adjusted = []
    for c in cdict:
        pts = cdict[c]
        df = pd.DataFrame(pts)
        centroid = list(df.mean())
        adjusted.append(centroid)
    return adjusted


def kmeans(data, k):
    '''Perform k-means clustering
    data- our attribute data (list of tuples)
    k- the number of clusters
    return - list of k centroids'''
    # Step 1 pick k random points to be intial centroid
    centroids = pick_initial_centroids(data, k)
    # Step 2 Assign each poiont to a cluster by finding the nearest centroid
    cdict = find_closest_centroid(centroids, data, euclidean)
    # Step 3 adjust move each centroid by averaging the attribute values
    # of the points associated with that centroid
    new_centroids = adjust_centroid(cdict)
    while centroids != new_centroids:
        centroids = copy.deepcopy(new_centroids)
        cdict = find_closest_centroid(centroids, data, euclidean)
        new_centroids = adjust_centroid(cdict)
    return centroids
    # Step 4


def visualize(centroids, data):
    df = pd.DataFrame(data)
    df['cluster'] = [closest(centroids, point, euclidean) for point in data]
    sns.pairplot(df, hue='cluster')
    plt.show()

def visualize_wcss(data,kmin=1,kmax=10):
    pass



def main():
    # read in the data
    data, classes = read_data('iris.dat')
    # print(data)
    # print(classes)

    # cluster the data
    centroids = kmeans(data, k=10)

    # visualize the clusters to validate the result
    visualize(centroids, data)


if __name__ == '__main__':
    main()
