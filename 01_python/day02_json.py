import json

data={
    "name":"siddhi",
    "hobbies":"crocet"
}

print(data)
print(type(data))

text=json.dumps(data)

print(text)
print(type(text))

back_to_dict=json.loads(text)

print(back_to_dict)
print(type(back_to_dict))