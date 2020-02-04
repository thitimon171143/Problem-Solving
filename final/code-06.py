import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
G.add_edges_from([('A','B'),('A','M'),('A','L'),('B','C'),('B','D'),
                ('B','N'),('B','O'),('C','D'),('D','E'),('D','O'),
                ('E','F'),('F','G'),('F','N'),('G','H'),('H','N'),
                ('H','I'),('H','P'),('P','O'),('P','I'),('P','M'),
                ('I','J'),('J','K'),('K','M'),('K','L')])

print('Shortest path from E to L is :',nx.shortest_path(G,source='E',target='L'))

final_avg = 999999999.99
final_key = ''
node_allSP = dict(nx.shortest_path_length(G,weight='weight'))
print(node_allSP)
for key in node_allSP:
    avg_nodeSP = sum(node_allSP[key].values())/(len(node_allSP[key])-1)
    print('AverageSP to all nodes of :',key,' is',avg_nodeSP)
    if final_avg > avg_nodeSP:
        final_avg = avg_nodeSP
        final_key = key

print('The centroid is : ',final_key,'the length is ',final_avg)

nx.draw(G,with_labels=True,font_color='yellow',node_size=1500)
plt.show()