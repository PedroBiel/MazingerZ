"""

MAZINGER Z
Datos para mostrar la información de las estadísticas.

Created on 02/06/2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""

import numpy as np

from casosfem.dts_fem import CasosFEM


class Estadisticas:
    """Pandas DataFrame con estadísticas descriptivas."""

    def __init__(self, df):
        """
        Sea df un DataFrame de pandas, obtiene las estadísticas descriptivas.

        :param df: pandas DataFrame ;  Datos de las tensiones.
        """

        self.df = df.copy()
        self.casos_fem = CasosFEM(self.df)
        self._df = None

    def dataframe_describe_fem(self):
        """Genera estadísticas descriptivas de todos loas casos FEM."""

        caso = 0
        df0 = self.dataframe_describe(caso)

        return df0

    def dataframe_describe_fem1(self):
        """Genera estadísticas descriptivas de los casos FEM 1."""

        caso = 1
        df1 = self.dataframe_describe(caso)

        return df1

    def dataframe_describe_fem2(self):
        """Genera estadísticas descriptivas de los casos FEM 2."""

        caso = 2
        df2 = self.dataframe_describe(caso)

        return df2

    def dataframe_describe_fem3(self):
        """Genera estadísticas descriptivas de los casos FEM 3."""

        caso = 3
        df3 = self.dataframe_describe(caso)

        return df3

    def dataframe_describe(self, caso: int):
        """
        Genera estadísticas descriptivas.
        Caso 0 : Todos los casos FEM.
        Caso 1 : FEM I.
        Caso 2 : FEM II.
        Caso 3 : FEM III.
        """

        if caso == 0:
            self._df = self.df
        elif caso == 1:
            self._df = self.casos_fem.dataframe_fem1()
        elif caso == 2:
            self._df = self.casos_fem.dataframe_fem2()
        elif caso == 3:
            self._df = self.casos_fem.dataframe_fem3()
        else:
            print('Oops!')

        df_describe = self._df.describe().T
        df_round = np.round(df_describe, decimals=2)
        df_idx = df_round.reset_index()

        return df_idx


if __name__ == '__main__':

    from tensionesrandom.dts_tensionesrandom import TensionesRandom

    tensiones_random = TensionesRandom()
    df = tensiones_random.dataframe_tensiones()
    print(df)

    estadisticas = Estadisticas(df)
    describe = estadisticas.dataframe_describe_fem()
    describe_1 = estadisticas.dataframe_describe_fem1()
    print('FEM')
    print(describe)
    print('FEM 1')
    print(describe_1)
