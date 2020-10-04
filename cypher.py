from morpheuscypher import Cypher
import os
import sys
from pprint import pprint
c = Cypher(morpheus=morpheus)
result = c.get("secret/lklabs:license")
print(result)