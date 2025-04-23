# Se crea una lista donde se almacenaran los productos que el usuario va a comprar
productsList = []
# Se crea un ciclo para habilitar la compra de 2 o mas productos
while True:
# Se crea una funcion para alertar errores
    def alert():
        print('\nEl numero ingresado es incorrecto, ingresalo nuevamente')
# Se crea una funcion para 
    def validation(text, condition):
        while True:
            try:
                number = float(input(f'\n{text} '))
                if condition(number): return number
                alert()
            except ValueError: alert()
# Se crea un diccionario donde se guardaran los datos del producto
    fullProduct = {}
# Se declaran las llaves necesarias
    fullProduct['product'] = str(input('\n-------> Ingresa el nombre del producto: '))
    fullProduct['price'] = validation('\n-------> Ingresa el precio del producto:', lambda x: x > 0)
    fullProduct['amount'] = validation('\n-------> Cuantos productos deseas comprar: ', lambda x: x > 0)
    fullProduct['discount'] = validation('\n-------> Ingresa el descuento que tiene el producto: ', lambda x: 0 <= x <= 100)
    fullProduct['sub-total'] = float(fullProduct['price'] * fullProduct['amount'])
    fullProduct['full-price'] = float(fullProduct['sub-total'] - (fullProduct['sub-total'] * (fullProduct['discount']/100)))
# Se añade el producto a la lista
    productsList.append(fullProduct)
# Se valida si el usuario desea comprar otro producto
    print('\n-------> ¿Deseas comprar otro producto?\n\nSi: 1\n\nNo: 2')
    if input().strip() == '2': break
# Print del resultado
print("\n")
print("="*40)
print("DETALLE DE FACTURACIÓN")
print("="*40)
for product in productsList:
    print(f"Producto       : {product['product']}")
    print(f"Cantidad       : {product['amount']}")
    print(f"Precio unitario: ${product['price']:.2f}")
    print(f"Subtotal       : ${product['sub-total']:.2f}")
    print(f"Descuento ({product['discount']}%): -${product['sub-total'] * (product['discount']/100):.2f}")
    print(f"Costo final    : ${product['full-price']:.2f}")
    print("="*40)
# Test de git