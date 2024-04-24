import json

a = "etm"

b = f'"result":"{a}"'

c = json.loads(b)
print(b)