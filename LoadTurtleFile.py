from rdflib import Graph

# Load the TTL file into an RDFLib Graph
g = Graph()
g.parse("fld.ttl", format="turtle")

# Print out each triple in the graph
for subj, pred, obj in g:
    pass
    #print(subj, pred, obj)


# query the graph
qres = g.query(
    """SELECT ?s ?p ?o
       WHERE {
          ?s ?p ?o .
       }""")

for row in qres:
    print("Row: ", row)