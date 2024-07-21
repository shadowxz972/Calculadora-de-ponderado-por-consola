# calcular el ponderado de n cursos

# importamos la libreria re para trabajar con expresiones regulares
import re

# creamos una funcion para validar que tenga como maximo 2 decimales
def validar_numero_flotante(num):
    #transformamos num a str para evitar errores abajo
    num = str(num)
    # compilamos la expresion regular para validar los 2 decimales
    patron = re.compile("^[0-9]+(\.[0-9]{1,2})?$")

    # verificamos si "num" coincide con el patron
    if patron.match(num):
        return True
    else:
        return False
    
# creamos las listas
notas = []
creditos = []

#hacemos una bienvenida al usuario
print("")# salto de linea2
print("Bienvenido a la calculadora de ponderado!")
print("") # salto de linea

# creamos un manejo de excepciones 
while True:
    try: 
        cantidad_cursos = int(input("Ingrese la cantidad de cursos: "))
        #validamos que sea positivo
        if cantidad_cursos < 0:
            print("El numero debe ser positivo")
        else:
            break # si es positivo se termina el bucle
    except ValueError:
        print("Tienes que ingresar un numero")
    except:
        print("Error desconocido")

# creamos un bucle for para rellenar las listas
for i in range(cantidad_cursos):
    # creamos un manejo de excepciones para las notas y validamos que sea positivo
    while True:
        try:
            nota = float(input(f"Ingrese nota {i+1}: "))
            if 0 <= nota <= 20:
                if validar_numero_flotante(nota):
                    notas.append(nota)
                    break
                else:
                    print("El maximo de decimales es 2")
            else:
                print("El numero debe estar entre 0-20")
        except ValueError:
            print("Tienes que ingresar un numero")
        except Exception as e:
            print(f"Error desconocido: {e}")
    #creamos un manejo de excepciones para los creditos y validamos que sea posito
    while True:
        try:
            credito = int(input(f"Ingrese credito {i+1}: "))
            if credito <= 0:
                print("La cantidad de creditos debe ser mayor a 0")
            else:
                creditos.append(credito)
                break
        except ValueError:
            print("Tienes que ingresar un numero")
        except Exception as e:
            print(f"Error desconocido: {e}")

# hacemos una comprension de lista para tener nota * credito
nota_por_credito = [n*c for n,c in zip(notas,creditos)]

# hacemos la formula del ponderado y lo redondeamos a 2 digitos
ponderado = round(sum(nota_por_credito) / sum(creditos), 2)

print(f"Tu ponderado es: {ponderado}")