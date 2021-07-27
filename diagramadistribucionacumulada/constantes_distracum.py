"""

MAZINGER Z
Constantes de los diagramas de distribución acumulada y de densidad de
probabilidad.

Created on 08/06/2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


class Constantes:
    """Valores constantes para los diagramas de dispersión."""

    def __init__(self):
        """Define las constantes."""

        self.__TITULO_DISTR_ACUM_FEM1 = 'Diagrama de la distribución '\
            'acumulada y \nde la densidad de probabilidad \nde los ratios '\
            'máx. de cada barra para todos los casos FEM I'
        self.__TITULO_DISTR_ACUM_FEM2 = 'Diagrama de la distribución '\
            'acumulada y \nde la densidad de probabilidad \nde los ratios '\
            'máx. de cada barra para todos los casos FEM II'
        self.__TITULO_DISTR_ACUM_FEM3 = 'Diagrama de la distribución '\
            'acumulada y \nde la densidad de probabilidad \nde los ratios '\
            'máx. de cada barra para todos los casos FEM III'
        self.__TITULO_DENS_PROB_FEM1 = "Diagrama de la densidad de "\
            "probabilidad de todos los casos FEM I"
        self.__TITULO_DENS_PROB_FEM2 = "Diagrama de la densidad de " \
            "probabilidad de todos los casos FEM II"
        self.__TITULO_DENS_PROB_FEM3 = "Diagrama de la densidad de " \
            "probabilidad de todos los casos FEM III"

    def get_titulo_distr_acum_1(self):
        """
        Getter del título del diagrama de la distribución acumulada de FEM 1.
        """

        return self.__TITULO_DISTR_ACUM_FEM1

    def get_titulo_distr_acum_2(self):
        """
        Getter del título del diagrama de la distribución acumulada de FEM 2.
        """

        return self.__TITULO_DISTR_ACUM_FEM2

    def get_titulo_distr_acum_3(self):
        """
        Getter del título del diagrama de la distribución acumulada de FEM 3.
        """

        return self.__TITULO_DISTR_ACUM_FEM3

    def get_titulo_dens_prob_1(self):
        """
        Getter del título del diagrama de la densidad de la probabilidad de
        FEM 1.
        """

        return self.__TITULO_DENS_PROB_FEM1

    def get_titulo_dens_prob_2(self):
        """
        Getter del título del diagrama de la densidad de la probabilidad de
        FEM 2.
        """

        return self.__TITULO_DENS_PROB_FEM2

    def get_titulo_dens_prob_3(self):
        """
        Getter del título del diagrama de la densidad de la probabilidad de
        FEM 3.
        """

        return self.__TITULO_DENS_PROB_FEM3
