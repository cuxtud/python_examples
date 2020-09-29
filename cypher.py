from morpheuscypher import Cypher
import os
import sys
from pprint import pprint
c = Cypher(morpheus=morpheus)
print(sys.executable)
print("morpheus['morpheus']:")
pprint(morpheus['morpheus'])
print("OS Env:")
pprint(os.environ)
print("sys.argv:")
pprint(sys.argv)
print("morpheus:")
pprint(morpheus)
result = c.get("secret/testing:accounts:1")
print(result)