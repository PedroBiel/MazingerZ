"""

MAZINGER Z
Datos para obtener los DataFrames de los casos FEM.

Created on 02/06/2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""

from casosfem.constantes_fem import Constantes


class CasosFEM:
    """Pandas DataFrames con los diferentes casos FEM."""

    def __init__(self, df):
        """
        Sea df un DataFrame de pandas, obtiene los diferentes DataFrames de
        los casos FEM..

        :param df: pandas DataFrame ;  Datos de las tensiones.
        """

        self.df = df

        self.constantes = Constantes()

    def dataframe_fem1(self):
        """DataFrame con los casos FEM 1."""

        caso = 1
        df1 = self.dataframe_fem(caso)

        # print('\ndf1')
        # cols = ['Modelo', 'Barra', 'Seccion', 'Caso']
        # print(df1[cols])

        return df1

    def dataframe_fem2(self):
        """DataFrame con los casos FEM 2."""

        caso = 2
        df2 = self.dataframe_fem(caso)

        return df2

    def dataframe_fem3(self):
        """DataFrame con los casos FEM 2."""

        caso = 3
        df3 = self.dataframe_fem(caso)

        return df3

    def dataframe_fem(self, caso: int):
        """
        DataFrame con los casos FEM.
        Caso 1 : FEM I.
        Caso 2 : FEM II.
        Caso 3 : FEM III.
        """

        casos_fem = []

        if caso == 1:
            casos_fem = self.constantes.get_casos_fem1()
        elif caso == 2:
            casos_fem = self.constantes.get_casos_fem2()
        elif caso == 3:
            casos_fem = self.constantes.get_casos_fem3()
        else:
            print('Oops!')

        df_fem = self.df[(self.df.Caso.isin(casos_fem))]

        return df_fem


if __name__ == '__main__':
    from tensionesrandom.dts_tensionesrandom import TensionesRandom

    cols = ['Modelo', 'Barra', 'Seccion', 'Caso']
    tensiones_random = TensionesRandom()
    df = tensiones_random.dataframe_tensiones()
    print(df[cols])

    casos_fem = CasosFEM(df)
    df1 = casos_fem.dataframe_fem1()
    df2 = casos_fem.dataframe_fem2()
    df3 = casos_fem.dataframe_fem3()
    print(df1[cols])
    print(df2[cols])
    print(df3[cols])
