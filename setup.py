from setuptools import setup

descripcion_larga = open('Readme.rst').read()

setup(
    name = "Exemplo de empaquetado",
    version = "0.12",
    description = "Descripción breve del Ejemplo de empaquetado",
    long_description = descripcion_larga,
    keywords = "empaquetado instalador paquetes",
    packages = []
)