import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

G.add_edges_from([('A','C'),('A','D'),('A','B'),
                  ('B','K'),('B','H'),('B','A'),
                  ('C','A'),('C','K'),
                  ('K','C'),('K','G'),('K','B'),
                  ('G','K'),('G','B'),('G','H'),
                  ('H','G'),('H','B'),('H','J'),('H','F'),('H','E'),
                  ('F','J'),('F','H'),
                  ('J','F'),('J','H'),('J','Z'),
                  ('E','H'),('E','Z'),('E','D'),
                  ('D','A'),('D','E')])

nx.draw(G,with_labels=True,font_color='yellow',node_size=1500)
plt.show()

for n in G.neighbors('A'):
  print(n)
