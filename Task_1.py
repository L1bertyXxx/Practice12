import json

with open("products.json", encoding="utf-8") as file:
    data = json.load(file)

for product in data["products"]:
    print(f"Название: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")
    if product["available"]:
        print("Есть в наличии\n")
    else:
        print("Нет в наличии\n")