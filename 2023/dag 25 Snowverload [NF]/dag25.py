from graphviz import Digraph

# Bestand lezen en verwerken
input_filename = "dag25.txt"
output_filename = "graph.pdf"

# Lees de inhoud van het bestand
with open(input_filename, "r") as file:
    input_data = file.read()

# Converteer de input naar een dictionary
graph = {}
for line in input_data.strip().split("\n"):
    if ":" in line:
        node, edges = line.split(":")
        graph[node.strip()] = edges.strip().split()

# Maak een directed graph met Graphviz
dot = Digraph(comment='Boom')

# Voeg nodes en verbindingen toe
for node, edges in graph.items():
    for edge in edges:
        dot.edge(node, edge)

# Render de graf en sla op als een PNG
dot.render(output_filename, format='png')

print(f"Graph image saved as {output_filename}")
