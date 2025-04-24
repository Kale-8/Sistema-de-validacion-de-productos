
# Calculadora de Costo Total de Compra

Este programa es una herramienta interactiva que permite calcular el costo total de una compra en una tienda, considerando precio, cantidad y posibles descuentos. Fue desarrollado como parte de una asignación para simular un escenario real en una empresa de software.

---

## 🛠️ Funcionalidades

- Solicita al usuario el nombre del producto, precio unitario, cantidad y descuento.
- Valida que el precio y la cantidad sean positivos.
- Valida que el descuento esté entre 0% y 100%.
- Calcula el subtotal, el monto de descuento y el total por producto.
- Permite ingresar múltiples productos.
- Muestra un resumen detallado de la compra con formato claro y amigable.

---

## 📋 Ejemplo de uso

Al ejecutar el programa, el usuario ingresará información como esta:

```
-------> Ingresa el nombre del producto: Camiseta
-------> Ingresa el precio del producto: 25.50
-------> Cuantos productos deseas comprar: 3
-------> Ingresa el descuento que tiene el producto: 10
-------> ¿Deseas comprar otro producto?
Si: 1
No: 2
```

Y al finalizar:

```
========================================
DETALLE DE FACTURACIÓN
========================================
Producto       : Camiseta
Cantidad       : 3.0
Precio unitario: $25.50
Subtotal       : $76.50
Descuento (10.0%): -$7.65
Total          : $68.85
========================================
Costo final    : $68.85
========================================
```
---

## 📌 Validaciones

- **Precio**: Debe ser un número mayor a 0.
- **Cantidad**: Debe ser un número mayor a 0.
- **Descuento**: Debe estar en el rango de 0 a 100%.

---

## ✅ Pruebas sugeridas

- Ingresar productos sin descuento.
- Usar el valor máximo y mínimo posible de descuento (0% y 100%).
- Intentar ingresar valores negativos o caracteres no válidos.
- Procesar múltiples productos en una misma sesión.
