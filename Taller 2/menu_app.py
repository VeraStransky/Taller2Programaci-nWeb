# Función para agregar compra
def agregar_compra(compras):
    monto = float(input("Ingrese el monto de la compra: "))
    compras.append(monto)
    print(f"Compra agregada correctamente.")


# Función para mostrar compras
def mostrar_compras(compras):
    if not compras:
        print("No hay compras registradas.")
    else:
        print("Lista de compras realizadas:")
        for i, compra in enumerate(compras, 1):
            print(f"Compra {i}: ${compra}")


# Función para mostrar total gastado
def mostrar_total(compras):
    total = sum(compras)
    print(f"El total gastado es: ${total:.2f}")


# Función principal con ciclo del programa
def main():
    compras = []

    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_compra(compras)
        elif opcion == '2':
            mostrar_compras(compras)
        elif opcion == '3':
            mostrar_total(compras)
        elif opcion == '4':
            print("¡Hasta Luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()



# https://github.com/VeraStransky/Taller2Programaci-nWeb.git