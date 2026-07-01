"""GGILES quickstart example from the package README."""

import matplotlib.pyplot as plt
import networkx as nx
from ggiles import make_converter
from ggiles.graph_invariant import AlphabeticNodeOrdering, GraphInvariantProcessor, MorganAlgorithm

G = nx.DiGraph()
G.add_node(0, type="a", id="1")
G.add_node(1, type="c", id="2")
G.add_node(2, type="b", id="3")
G.add_node(3, type="d", id="4")
G.add_node(4, type="b", id="5")
G.add_node(5, type="c", id="6")
G.add_node(6, type="a", id="7")
G.add_node(7, type="e", id="8")
G.add_node(8, type="a", id="9")
G.add_edge(0, 1, type="a-c", flt=0.1)
G.add_edge(1, 2, type="c-b", flt=1.2)
G.add_edge(2, 3, type="b-d", flt=2.3)
G.add_edge(3, 4, type="d-b", flt=3.4)
G.add_edge(4, 1, type="b-c", flt=4.1)
G.add_edge(3, 5, type="d-c", flt=3.5)
G.add_edge(6, 4, type="a-b", flt=4.6)
G.add_edge(4, 7, type="b-e", flt=5.7)

# Plot the graph
pos = nx.kamada_kawai_layout(G)
edge_labels = nx.get_edge_attributes(G, "type")
node_labels = nx.get_node_attributes(G, "type")

plt.figure(figsize=(10, 8))
nx.draw(
    G,
    pos,
    with_labels=True,
    labels=node_labels,
    node_color="cyan",
    node_size=500,
    font_size=10,
    font_weight="bold",
)
nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_color="green",
    font_weight="bold",
)

plt.title("Example graph")

plt.show()

invariant = GraphInvariantProcessor(layers=[MorganAlgorithm(), AlphabeticNodeOrdering("type")])
graph_converter = make_converter(invariant=invariant)
sequence = graph_converter.graph_to_sequence(G)
print(sequence)

reconstructed_graph = graph_converter.sequence_to_graph(sequence)
print(
    nx.is_isomorphic(
        G,
        reconstructed_graph,
        node_match=lambda x, y: x["type"] == y["type"],
        edge_match=lambda x, y: x["type"] == y["type"],
    )
)
