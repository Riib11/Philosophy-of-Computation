import model
import networkx as nx

def make_similarity_graph(model_name):
  M = model.load_model(model_name)

  # create graph
  G = nx.Graph()
  
  # create nodes
  for word, vocab in M.wv.vocab.items():
    G.add_node(word)
    G.node[word]["count"] = vocab.count

  # create undirected edges
  for word, vocab in M.wv.vocab.items():
    # si: similarity index
    for (w, si) in list(M.wv.most_similar(word)):
      G.add_edge(word, w, weight=si)

  return G


model_name = "bible"

G = make_similarity_graph(model_name)
nx.write_gexf(G, "network/"+model_name+".gexf")
