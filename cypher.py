from morpheuscypher import Cypher
import os
import sys
from pprint import pprint
c = Cypher(morpheus=morpheus)
result = c.get("secret/labkey:license")
print(result)
print(result.values())
pv=result.values()
pp=pv[2:-1]
print(pp)