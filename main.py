# ejercicio 1 python

print("calculo de edad en el 2070")
edad = int(input("Ingrese su Edad :"))
año_actual = int(input("Año Actual: "))

año = 2070


def calculo_edad():
    edad_futura = (año - año_actual) + edad
    print("su edad en el año "+str(año)+" serà de: "+str(edad_futura)+" años" )
    return edad_futura
calculo_edad()
