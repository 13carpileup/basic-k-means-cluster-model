import random
import matplotlib.pyplot as plt
from settings import *
def cluster():
    colours=['b','g','r','c','m','y','k','w']
    plot=[[random.uniform(0,1),random.uniform(0,1)] for i in range(points)] 
    clusters=clusterNumber

    def kmeans(group=[],first=False):
        if not first:
            tracker={i:[0,0] for i in range(clusters)}
            tracker2={i:0 for i in range(clusters)}
            for i in range(len(plot)):
                tracker[group[i]][0]+=plot[i][0]
                tracker[group[i]][1]+=plot[i][1]
                tracker2[group[i]]+=1
            centroids=[[tracker[i][0]/tracker2[i],tracker[i][1]/tracker2[i]] for i in range(clusters)]
        else:
            centroids=[[random.uniform(0,1),random.uniform(0,1)] for i in range(clusters)]
        group=[]
        for item in plot:
            cs=[((item[0]-centroids[i][0])**2)+((item[1]-centroids[i][1])**2) for i in range(clusters)]
            minNum=min(cs)
            group.append(cs.index(minNum))
        return [group,centroids]

    stor=kmeans(first=True)
    group=stor[0]
    centroids=stor[1]

    for i in range(len(plot)):
        plt.scatter(plot[i][0],plot[i][1],c=colours[group[i]],s=7)
    for item in centroids:
        plt.scatter(item[0],item[1],c="Black",s=15)
    plt.grid(True)
    plt.xlim([0,1])
    plt.ylim([0,1])
    plt.savefig('before.png')
    plt.close()
    storage=0
    counter=0
    while storage!=group:
        stor=kmeans(group=stor[0])
        storage=group
        group=stor[0]
        counter+=1
    centroids=stor[1]
    x=plt.subplots()
    plt.xlim([0,1])
    plt.ylim([0,1])
    for i in range(len(plot)):
        plt.scatter(plot[i][0],plot[i][1],c=colours[group[i]],s=7)
    for item in centroids:
        plt.scatter(item[0],item[1],c="Black",s=15)

    plt.grid(True)

    plt.savefig('after.png')
    plt.close()
    return counter

cluster()
