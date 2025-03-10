from graphtools import *
import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule
import pycuda.gpuarray as gpuArray
import numpy as np

def makeClusterList(graph,clusters):
    #Cuda stuff needed
    start = cuda.Event()
    end = cuda.Event()
    
    # array into something the gpu can read
    clusters_gpu = gpuarray.to_gpu(clusters)
    
    #creating the function the gpu is going to use
    func = SourceModule("""
    __global__ void getGraphGpu(float *nodes, int nodes_length, float *graph, int graph_length, float *clusters, int clusters_length)
    {
         nodes = [n for n in graph.node if graph.node[n]['cluster'] in clusters]
         
         n = 0;
         
         for (i = 0; i < graph_length; i++)
            for( j = 0; j < clusters_length; j++)
                if ( graph[i] == clusters[j] )
                    nodes[n] = graph[i]
    }
    """)
    
    #creating where the answer is going to be
    listToTraverse= [[]] * len(clusters)
    func = func.get_function(getGraphGpu)
    
    for i in range(len(clusters)):
        # trying to use the function in gpu
        func (listOfNodes[i].Out, graph.In, clusters_gpu.In)
    
    
    return listOfAnswers
