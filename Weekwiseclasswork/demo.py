
print([p["name"] for p in sorted([{"name": "Alice", "age": 30}, 
{"name": "Bob", "age": 25}, {"name": "Charlie", "age": 35}, {"name": "David", "age": 20}], key=lambda x: x["age"])])



