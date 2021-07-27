"""

MAZINGER Z
Constantes de los casos FEM

Created on 02/06/2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""

from itertools import chain


class Constantes:
    """Valores constantes de los casos FEM."""

    def __init__(self):
        """Define las constantes."""

        # TODO Los casos FEM son provisionales.
        self.__CASOS_FEM1 = (100, 1000, 2000, 4700)
        self.__CASOS_FEM2 = chain(
            range(1100, 1107), range(2100, 2107),
            range(4800, 4804), range(4900, 4904)
        )
        self.__CASOS_FEM3 = chain(
            range(1200, 1375), range(2200, 2375),
            range(4100, 4101), range(4400, 4407)
        )

    def get_casos_fem1(self):
        """Getter de los casos FEM 1."""

        return self.__CASOS_FEM1

    def get_casos_fem2(self):
        """Getter de los casos FEM 2."""

        return self.__CASOS_FEM2

    def get_casos_fem3(self):
        """Getter de los casos FEM 3."""

        return self.__CASOS_FEM3


if __name__ == '__main__':

    constantes = Constantes()
    fem1 = constantes.get_casos_fem1()
    fem2 = constantes.get_casos_fem2()
    fem3 = constantes.get_casos_fem3()

    for caso in fem1:
        print(caso, end=' | ')
    print()
    for caso in fem2:
        print(caso, end=' | ')
    print()
    for caso in fem3:
        print(caso, end=' | ')
