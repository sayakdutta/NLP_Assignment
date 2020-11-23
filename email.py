# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 11:23:38 2020

@author: sayakdibyo
"""

import os
import sys
import re
import math
import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter
# Enron email network analysis
# please change the direcoty in line 8 ans 20 to the folder with download data.

def limit(dict):
    max=-math.inf
    min=math.inf
    for key in dict:
        if(max<dict[key]):
            max=dict[key]
        if(min>dict[key]):
            min=dict[key]
    return max,min

def normalize(dict):
    max,min=limit(dict)
    for key in dict:
        dict[key]=100.0*(dict[key]-min)/(max-min)
    return dict

os.chdir("C:\\Users\\sayakdibyo\\Desktop\\maildir")
names = [d for d in os.listdir(".") if "." not in d]
# create networkx graph
G=nx.DiGraph()
g=nx.Graph()
email={}
tot_email=0
for name in names:
    
    os.chdir("C:\\Users\\sayakdibyo\\Desktop\\maildir\\%s" % name)
    subfolders = os.listdir('.')
    sent_dirs = [n for n, sf in enumerate(subfolders) ]
    sent_dirs_words = [subfolders[i] for i in sent_dirs]
    for d in sent_dirs_words:
        os.chdir('C:\\Users\\sayakdibyo\\Desktop\\maildir\\%s\\%s' % (name,d))
        file_list = os.listdir('.')
        for filename in file_list:
                if(not os.path.isfile(filename)):
                    continue
                f = open(filename, 'r')
                content=f.readlines()
                #print(content)
                tolist=content[3]
                tolist=re.sub('To: ', '', tolist)
                tolist=re.sub('\r\n','',tolist)
                tolist=re.sub('@enron.com','',tolist)
                tolist=re.sub('.com','',tolist)
                recipientslist = tolist.split(',')
        
                fromlist=content[2]
                fromlist=re.sub('From: ', '', fromlist)
                fromlist=re.sub('\r\n','',fromlist)
                fromlist=re.sub('@enron.com','',fromlist)
                fromlist=re.sub('.com','',fromlist)
                
        
                if '<nodes>' not in fromlist:
                  
                    for recipients in recipientslist:
                        if (recipients!=' '):
                            #print "Nodes of graph: ", fromlist
                            #print "Edges of graph: ", recipients
                            # add nodes
                            
                           
                            fromlist=fromlist.strip('\n')
                            recipients=recipients.strip('\n')
                            if(recipients.isspace() or fromlist.isspace()):
                                continue
                            for val,i in enumerate(fromlist):
                                if i.isalnum():
                                    break
                            fromlist=fromlist[val:]
                            for val,i in enumerate(recipients):
                                if i.isalnum():
                                    break
                            recipients=recipients[val:]
                            if(fromlist.startswith("Subject") or recipients.startswith("Subject")):
                                continue
                            G.add_node(fromlist.strip())
                            G.add_node(recipients.strip())
                            # add edges
                            G.add_edge(fromlist, recipients)
                            
                            g.add_node(fromlist.strip())
                            g.add_node(recipients.strip())
                            # add edges
                            g.add_edge(fromlist, recipients)
                            if(fromlist not in email):
                                email[fromlist]=0
                            if(recipients not in email):
                                email[recipients]=0   
                            email[fromlist]+=1
                            email[recipients]+=1
                            tot_email+=1
    
# stat: centrality analysis
degreecentral=nx.degree_centrality(G)

cluster=nx.clustering(G)
mat=nx.shortest_path(G)
shortest_path={}
"""
for key in mat:
    print(key,mat[key])
    break
"""
for key in mat:
    if(key not in shortest_path.keys()):
        shortest_path[key]=0
    for k in mat[key]:
        shortest_path[key]+=len(mat[key][k])-1
betweenness=nx.betweenness_centrality(G)
h,a=nx.hits(G)
clique=nx.number_of_cliques(g)
max_clique=nx.node_clique_number(g)
for key in max_clique:
    max_clique[key]=1.0*(email[key]/tot_email)*math.pow(2,max_clique[key]-1)


email=normalize(email)
degreecentral=normalize(degreecentral)
cluster=normalize(cluster)
shortest_path=normalize(shortest_path)
betweenness=normalize(betweenness)
h=normalize(h)
a=normalize(a)
clique=normalize(clique)
max_clique=normalize(max_clique)

score={}
for key in email:
    if(key in degreecentral and key in cluster and key in shortest_path and key in betweenness and key in h and key in a and key in clique
       and key in max_clique):
        if(key not in score):
            score[key]=0
        score[key]+=(email[key]+degreecentral[key]+cluster[key]+shortest_path[key]+betweenness[key]+h[key]+a[key]+clique[key]+max_clique[key])/9

max,_=limit(score)
for key in score:
    score[key]=100.0*score[key]/max

f = open("C:\\Users\\sayakdibyo\\Desktop\\nlp_assignment\\score.txt", "w")
original_stdout = sys.stdout
sys.stdout = f

for key in sorted(score.items(),key=itemgetter(1),reverse=True):
    print(key[0],key[1])
 
   
sys.stdout = original_stdout 


"""
fig = plt.figure(figsize=(100, 100)) 
# draw graph

nx.draw(G,node_size=25,with_labels=True)
plt.axis('equal') 
plt.show() 
fig.savefig('C:\\Users\\sayakdibyo\\Desktop\\nlp_assignment\\plot.png') 
"""