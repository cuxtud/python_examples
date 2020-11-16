from morpheuscypher import Cypher
import os
import sys
from pprint import pprint
c = Cypher(morpheus=morpheus)
result = c.get("secret/testing:accounts:1[0]")
pv=result.values()
print(pv)
#kv=(str(pv).strip('[]'))[2:-1]
#print(kv)