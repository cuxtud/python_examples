import morpheus-cypher
from morpheuscypher import Cypher
import os
import sys
from pprint import pprint
print(sys.executable)
print("morpheus['morpheus']:")
pprint(morpheus['morpheus'])
print("OS Env:")
pprint(os.environ)
print("sys.argv:")
pprint(sys.argv)
print("morpheus:")
pprint(morpheus)
c = Cypher(morpheus=morpheus)
result = c.get("secret/testing:accounts:1")
print(result)