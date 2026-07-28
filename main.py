from src.product import Product

# Cas valide
p1 = Product(id_product=1, product_name="Laptop", quantity=5, price=999.99)
print(p1)

# Cas invalides pour tester les erreurs
try:
    p2 = Product(id_product=2, product_name="", quantity=5, price=100.0)
except ValueError as e:
    print("Error:", e)

try:
    p3 = Product(id_product=3, product_name="Phone", quantity=5, price=-10.0)
except ValueError as e:
    print("Error:", e)

try:
    p4 = Product(id_product=4, product_name="Tablet", quantity=0, price=200.0)
except ValueError as e:
    print("Error:", e)
