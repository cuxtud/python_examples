from morpheuscypher import Cypher
import os
import sys
from pprint import pprint
c = Cypher(morpheus=morpheus)
result = c.get("secret/labkey:license:0")
print(result)
print(result.values())
pv=result.values()
print(pv)