import morpheus-cypher
from morpheuscypher import Cypher
c = Cypher(morpheus=morpheus)
result = c.get("secret/testing:accounts:1")
print(result)