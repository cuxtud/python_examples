from morpheuscypher import Cypher
c = Cypher(url="https://10.30.20.131", token="4885b1f6-0160-401d-8be7-2a7dab9b05ce")
result = c.get("secret/testing:accounts:1")
print(result)