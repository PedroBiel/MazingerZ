"""

MAZINGER Z
Constantes de los diagramas de dispersión

Created on 08/06/2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


class Constantes:
    """Valores constantes para los diagramas de dispersión."""

    def __init__(self):
        """Define las constantes."""

        self.__TITULO_DISPERSION = "Diagrama de dispersión de todos los " \
                                   "casos FEM "
        self.__TITULO_DISPERSION_FEM1 = "Diagrama de dispersión de los " \
                                   "casos FEM I"
        self.__TITULO_DISPERSION_FEM2 = "Diagrama de dispersión de todos " \
                                   "casos FEM II"
        self.__TITULO_DISPERSION_FEM3 = "Diagrama de dispersión de todos " \
                                   "casos FEM III"
        self.__XLABEL = "Barras"
        self.__YLABEL = "Ratio"

    def get_titulo_dispersion(self):
        """Getter del título del diagrama de dispersión."""

        return self.__TITULO_DISPERSION

    def get_titulo_dispersion_1(self):
        """Getter del título del diagrama de dispersión de FEM 1."""

        return self.__TITULO_DISPERSION_FEM1

    def get_titulo_dispersion_2(self):
        """Getter del título del diagrama de dispersión de FEM 2."""

        return self.__TITULO_DISPERSION_FEM2

    def get_titulo_dispersion_3(self):
        """Getter del título del diagrama de dispersión de FEM 3."""

        return self.__TITULO_DISPERSION_FEM3

    def get_xlabel(self):
        """Getter de la etiqueta x del diagrama."""

        return self.__XLABEL

    def get_ylabel(self):
        """Getter de la etiqueta y del diagrama."""

        return self.__YLABEL
