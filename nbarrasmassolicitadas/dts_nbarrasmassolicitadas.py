"""

MAZINGER Z
Datos de la barra más solicitada.

Created on 14/07/2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


from casosfem.dts_fem import CasosFEM


class NBarrasMax:
    """Fórmula para el cálculo de los datos de las n barras más solicitadas."""

    def __init__(self, df):
        """
        Sea df un DataFrame de pandas con los datos para el cálculo de las
        barras más solicitadas, obtiene los valores correspondientes.

        :param df: pandas DataFrame ; Datos para el cálculo de las barras más
                                      solicitadas.
        """

        self.df = df.copy()
        self.casos_fem = CasosFEM(self.df)
        self._df = None

    def mas_solicitadas_1(self):
        """
        Datos relativos a las n barras más solicitadas de los casos FEM 1.
        :param df : pandas DataFrame ; Datos para el cálculo de las barras más
                                       solicitadas.
        """

        caso = 1
        df1 = self.dataframe_n_barras(caso)
        print('\ndf1')
        print(df1)



    def dataframe_n_barras(self, caso: int):
        """
        Genera los datos de las n barras más solicitadas.
        Caso 1 : FEM I.
        Caso 2 : FEM II.
        Caso 3 : FEM III.
        """

        if caso == 1:
            self._df = self.casos_fem.dataframe_fem1()
        elif caso == 2:
            self._df = self.casos_fem.dataframe_fem2()
        elif caso == 3:
            self._df = self.casos_fem.dataframe_fem3()
        else:
            print('Oops!')

        cols = ['Barra', 'Seccion', 'Caso', 'Mises', 'Ratio']
        df_n_barras = self._df.sort_values(ascending=False, by='Ratio')
        df_n_barras = df_n_barras.drop_duplicates('Barra')

        return df_n_barras








# class BarraMasSolicitada(DataFrame):
#     """Fórmula para el cálculo de los datos de la barra más solicitada."""
#
#     def __init__(self):
#         """
#         Sea df un DataFrame de pandas con los datos para el cálculo de la barra más
#         solicitada, obtiene los valores correspondientes.
#
#         :param df: pandas DataFrame ; Datos para el cálculo de la barra más
#                                       solicitada.
#         """
#
#         DataFrame.__init__(self)
#
#     def mas_solicitada(self, df):
#         """
#         Datos relativos a la barra más solicitada.
#         :param df : pandas DataFrame ; Datos para el cálculo de la barra más
#                                        solicitada.
#         """
#
#         _df = self.get_df(df)
#         df_idxmax = _df.loc[_df['Ratio'].idxmax()]
#
#         return df_idxmax
