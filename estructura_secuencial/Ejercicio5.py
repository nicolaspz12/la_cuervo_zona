value=float(input("digite el valor de su compra:"))
#(value) almacenas el valor de la compra
discount=float(input("digite el valor del descuento (%):"))
#(discount) almacena el valor del descuento
discount_value= value * (discount/100)
#(discount_value) permite entontrar el descuento
total_value=value-discount_value
# da el precio total
print("la compra fue", value, ",con un descuento de", discount_value, ", y el Valor final a pagar:", total_value, )
#imprime el resultado deseado segun la guia