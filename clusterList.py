"""
Created on Wed Nov 27 17:45:26 2019

@author: sergi
"""

from graphtools import *

def makeClusterList(graph,clusters):
    listToTraverse
    for i in range(len(clusters)):
        listToTraverse[i] = get_cluster(graph,[i])
        
     for i in range(len(clusters))
        j=i+1
        for j in range(len(clusters)) 
            if verbose: print "Checking c%d c%d" % (i, j)
            ms = merge_score(graph, listToTraverse[i], listToTraverse[j], a)
            if verbose: print "Merge score: %f" % (ms)
            if ms > max_score:
                if verbose: print "Better than: %f" % (max_score)
                max_score = ms
                ci, cj = clusters[i], clusters[j]
  """
    for i in range(len(clusters))
        j=i+1
        for j in range(len(clusters)) 
            if verbose: print "Checking c%d c%d" % (i, j)
            ms = merge_score(graph, get_cluster(graph,clusters[i]), get_cluster(graph,clusters[j]), a)
            if verbose: print "Merge score: %f" % (ms)
            if ms > max_score:
                if verbose: print "Better than: %f" % (max_score)
                max_score = ms
                ci, cj = clusters[i], clusters[j]
   """
