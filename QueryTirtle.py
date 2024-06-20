from rdflib import Graph

# Load the RDF data
g = Graph()
g.parse("https://paul.ti.rw.fau.de/~ec25opos/fld.ttl", format="ttl")

# Define the SPARQL query
queryFile = open("construct.rq", "r")
query = queryFile.read()
queryFile.close()

# Print the query
print(query)

# Execute the query
results = g.query(query)

# Print the results
for row in results:
    print(row)
