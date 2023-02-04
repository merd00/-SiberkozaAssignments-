# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json

json_mo = '{"name":"mert", "age":22}'
m = json.loads(json_mo)
print(json_mo)

m["name"]="mert"


json_mo = json.dumps(m)
print(json_mo)