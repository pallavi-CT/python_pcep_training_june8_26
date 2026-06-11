# iterations in dicts and defaultdict examples
catalog = {
    "PR001": {'name': 'Bluetooth Headphones', 'price': 23000, 'stock': 23},
    "PR002": {'name': 'Wired Headphones', 'price': 15000, 'stock': 20},
    "PR003": {'name': 'Laptop Stand', 'price': 10000, 'stock': 3},
    "PR004": {'name': 'USB Keyboard', 'price': 18000, 'stock': 0}
}

print('=======Full Catalog======')
for sku, product in catalog.items():  # key, value
   status = "In Stock" if product.get('stock') > 0 else "Out of Stock"
   print(f' {sku} | {product['name']:22} | {product['price']:>7.2f} | {status}')

# for sku in catalog.keys():
#    product = catalog[sku]
#    if product.get('stock') > 0:
#       status = "In stock"
#    else:
#       status = "Out of stock"
   
#    print(f' {sku} | {product['name']:22} | {product['price']:>7.2f} | {status}')

print("Items In Stock")
in_stock = {sku: p for sku, p in catalog.items() if p['stock'] > 0}
print("\nItems in stock: ", in_stock)
print()
print(f'Stocked Items: {list(in_stock.keys())} : {list(in_stock.values())}')