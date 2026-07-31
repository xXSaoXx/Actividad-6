class ArticuloCientifico:
    def __init__(self, titulo, autor, palabras_claves=None,
                 publicacion=None, anio=None, resumen=None):
        self.titulo = titulo
        self.autor = autor
        self.palabras_claves = palabras_claves if palabras_claves else []
        self.publicacion = publicacion
        self.anio = anio
        self.resumen = resumen

    def imprimir(self):
        print(f"Título del artículo = {self.titulo}")
        print(f"Autor del artículo = {self.autor}")
        print("Palabras clave =")
        for palabra in self.palabras_claves:
            print(palabra)
        print(f"Publicación = {self.publicacion}")
        print(f"Año = {self.anio}")
        print(f"Resumen = {self.resumen}")


def main():
    palabras = ["Física", "Espacio", "Tiempo"]

    articulo = ArticuloCientifico(
        "La teoría especial de la relatividad",
        "Albert Einstein",
        palabras,
        "Anales de Física",
        1913,
        "Las leyes de la física son las mismas en todos los sistemas de referencia inerciales."
    )
    articulo.imprimir()


if __name__ == "__main__":
    main()
