class Profesor:
    def imprimir(self):
        print("Es un profesor.")


class ProfesorTitular(Profesor):
    def __init__(self):
        self.anios = 0

    def imprimir(self):
        print("Es un profesor titular.")

    def imprimir_anios(self):
        print(f"Años = {self.anios}")


def main():
    profesores = []

    profesor1 = Profesor()
    profesor2 = ProfesorTitular()

    profesores.append(profesor1)
    profesores.append(profesor2)

    for profesor in profesores:
        profesor.imprimir()


if __name__ == "__main__":
    main()
