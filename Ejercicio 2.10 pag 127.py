class Pedido:
    def calcular_pedido(self, *datos):
        if len(datos) == 4:
            primer_plato, costo_primer_plato, bebida, costo_bebida = datos
            total = costo_primer_plato + costo_bebida
            print(f"El costo de {primer_plato} y {bebida} es = ${total}")

        elif len(datos) == 6:
            (primer_plato, costo_primer_plato, segundo_plato,
             costo_segundo_plato, bebida, costo_bebida) = datos
            total = costo_primer_plato + costo_segundo_plato + costo_bebida
            print(f"El costo de {primer_plato} + {segundo_plato} + {bebida} es = ${total}")

        elif len(datos) == 8:
            (primer_plato, costo_primer_plato, segundo_plato,
             costo_segundo_plato, postre, costo_postre,
             bebida, costo_bebida) = datos
            total = costo_primer_plato + costo_segundo_plato + costo_postre + costo_bebida
            print(f"El costo de {primer_plato} + {segundo_plato} + {bebida} + {postre} es = ${total}")


class Suma:
    def sumar(self, *numeros):
        return sum(numeros)


def main():
    pedido1 = Pedido()
    pedido1.calcular_pedido("Sancocho", 5000, "Gaseosa", 2000)

    pedido2 = Pedido()
    pedido2.calcular_pedido(
        "Crema de verduras", 5000, "Churrasco", 6000, "Gaseosa", 2000
    )

    pedido3 = Pedido()
    pedido3.calcular_pedido(
        "Crema de espinacas", 5000, "Salmón", 10000,
        "Tiramisú", 5000, "Gaseosa", 2000
    )

    suma = Suma()
    print(f"Suma de dos enteros: {suma.sumar(10, 20)}")
    print(f"Suma de tres enteros: {suma.sumar(10, 20, 30)}")
    print(f"Suma de dos decimales: {suma.sumar(10.5, 20.5)}")
    print(f"Suma de tres decimales: {suma.sumar(10.5, 20.5, 30.5)}")


if __name__ == "__main__":
    main()
