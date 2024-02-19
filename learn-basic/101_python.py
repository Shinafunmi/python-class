#python json

import json

x = '{"name":"john", "age": 30, "city": "new york"}'

y = json.loads(x)

print(y["city"])


####

a = {
    "name": "john",
    "age": 50,
    "city": "greensburg"
}

b = json.dumps(a)
print(b)