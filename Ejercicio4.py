name=(input("ingrese el nombre del vendedor:"))
#la variable (name) almacena el nombre dek vendedor 
basspay=int(input("ingrese el sueldo base:"))
# la variable (basspay) define el sueldo del vendedor
tip=int(input("ingrese el valor de las comisiones:"))
# la variable (tip) guarda el valor agregado de comisiones
total_pay= (basspay+tip)
# suma los valores (basspay,tip) dandonos el valor final
print("el vendedor" ,name , ", tiene un sueldo base de" ,basspay , ", durante el mes obtuvo una comision de" ,tip , "y el sueldo final es:" ,total_pay , )
