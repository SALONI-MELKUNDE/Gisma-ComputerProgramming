
collection_a = [
    {"name": "sal", "age": 30},
    {"name": "swap", "age": 25},
    {"name": "san", "age": 35},
    {"name": "sam", "age": 20}
]


sorted_names = [person["name"] for person in sorted(collection_a, key= lambda x: x["age"])]

print("Names sorted by age:", sorted_names)

