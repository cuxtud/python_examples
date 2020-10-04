from morpheuscypher import Cypher
import os
import sys
from pprint import pprint
c = Cypher(morpheus=morpheus)
result = c.get("secret/labkey:license")
pv=result.values()
kv=(str(pv).strip('[]'))[2:-1]
return kv