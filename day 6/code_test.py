import custom_exceptions as ce

products = [
    {'id': 'P001', 'name': 'Laptop', 'brand': 'Dell', 'price': 234560, 'stock': 9},
    {'id': 'P002', 'name': 'keyboard', 'brand': 'Dell', 'price': 2345, 'stock': 5}
]

def view_product_by_id(product_id):
    flag = False

    for product in products:
        # try:
        if product['id'] != product_id:
            flag = False
        else:
            flag = True
            return product
               
        # except ce.ProdNotFound as ex:
        #         print('Error: ', ex)
    
    if flag == False:
        raise ce.ProdNotFound(f"Product with ID {product_id} not found")

try:
    view_product_by_id('P003')
except ce.ProdNotFound as ex:
    print('Error: ', ex)

    