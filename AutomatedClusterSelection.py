import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import sklearn.cluster as cluster
import time
import pandas as pds
import hdbscan as hdb
import seaborn as sns
import sys

#TODO: Cluster Points fil

def clusterPoints(pointsDF,minSample):
    clusters = hdb.HDBSCAN(min_samples=minSample,min_cluster_size=2,alpha=1.0).fit_predict(pointsDF)
    return clusters



#TODO: plotting for orig and clustered data
def plotClusters(pointsDf,clusters,size,minSample):
    palette = sns.color_palette('bright', np.unique(clusters).max() + 1)
    colors = [palette[x] if x >= 0 else (0.0, 0.0, 0.0) for x in clusters]
    plt.figure(figsize=(20,15))
    plt.scatter(pointsDf[0], pointsDf[1], c=colors,alpha=.9, s=2, linewidths=8)
    plt.title(str(minSample))
    frame = plt.gca()
    frame.axes.get_xaxis().set_visible(False)
    frame.axes.get_yaxis().set_visible(False)
    plt.savefig(str(minSample))


def plotOriginal(pointsDf):
    plt.figure(figsize=(20,15))
    plt.scatter(pointsDf[0], pointsDf[1],alpha=.9, s=2, linewidths=8)
    plt.title(str("Original"))
    frame = plt.gca()
    frame.axes.get_xaxis().set_visible(False)
    frame.axes.get_yaxis().set_visible(False)
    plt.savefig(str("Original"))


#TODO: Run CheckM

def runCheckM():

    pass

#TODO: Select bins to be manually inspected

def selectBins():

    pass

#Make binList

def makeBinList(fasta,clusters,binPrefix):
    binList=list()
    count=0
    with open(fasta) as fasta:
        for line in fasta:
            if line.startswith(">"):
                if clusters[count] != -1:
                    binList.append(line.strip()[1:]+"\t"+binPrefix+"."+str(clusters[count]))
                count+=1
    return binList

def printBinList(binList,minSample):
    with open(str("binlist_"+str(minSample)+".txt"), mode="w") as outfile:
        for line in binList:
            outfile.write("%s\n" % line)


#TODO: Make bin fastas

def makeFastas():

    pass



def main():
    sns.set_context('poster')
    sns.set_color_codes()
    #read in the points file
    points=pds.read_csv(sys.argv[1],header=None)
    fasta=sys.argv[2]
    size=sys.argv[3]
    #plotOriginal(points)
    for minSample in [10,15,25,50,75,100]:
        print("1")
        clusters=clusterPoints(points,minSample)
        print("2")
        binPrefix="minSample"+str(minSample)
        binList=makeBinList(fasta,clusters,binPrefix)
        print("3")
        printBinList(binList,minSample)
        print("4")
        #plotClusters(points,clusters,size,minSample)

if __name__ == '__main__':
    main()