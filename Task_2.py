import json

products = "products.json"

with open(products, encoding="utf-8") as file:
    data = json.load(file)

while True:
    name = input("\nВведите название товара: ")
    price = int(input("Введите цену: "))
    weight = int(input("Введите вес: "))
    available = input("Есть в наличии? (да/нет): ").lower()
    available = True if available == "да" else False

    new_product = {
        "name": name,
        "price": price,
        "weight": weight,
        "available": available
    }

    data["products"].append(new_product)

    add = input("Добавить еще? (да/нет): ").lower()
    if add == "нет":
        break

with open(products, "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

print("\nОбновленный список продуктов:\n")
for product in data["products"]:
    print(f"Название: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")
    print("В наличии\n" if product["available"] else "Нет в наличии!\n")