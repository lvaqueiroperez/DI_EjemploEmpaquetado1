from setuptools import setup

descripcion_larga = open('Readme.rst').read()

setup(
    name = "Exemplo de empaquetado",
    version = "0.12",
    author = "Luis",
    author_email = "lvaqueiroperez@danielcastelao.org",
    url = "https://www.danielcastelao.org",
    license = "GLP",
    platforms = "Unix",
    clasifiers = ["Development Status :: 3 - Alpha",
                  "Environment :: Console",
                  "Topic :: Software Development :: Libraries",
                  "License :: OSI Aproved :: GNU General Public License",
                  "Programming Language :: Python :: 3.4",
                  "Operating System :: Linux Ubuntu"
                  ],
    description = "Descripción breve del Ejemplo de empaquetado",
    long_description = descripcion_larga,
    keywords = "empaquetado instalador paquetes",
    packages = ['paquete1','paquete1/subPaquete1'],#OTRA FORMA: packages = find_packages(exclude= ['*.test','*.test.*']) podemo excluír lo que queramos
    package_data = {
        'paquete1' : 'notas.txt',
        'paquete/subPaquete1' : 'texto.txt'
    },
    data_files = [('datos',['dat/datos.txt'])],
    entry_points = {'console_scripts': ['imprimeAlgo = paquete1.moduloPaquete1: main',],}

)