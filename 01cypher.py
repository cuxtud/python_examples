from morpheuscypher import Cypher
c = Cypher(url="https://10.30.20.131", token="xxxx")
result = c.get("secret/testing:accounts:1")
print(result)