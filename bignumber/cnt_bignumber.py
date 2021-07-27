"""

MAZINGER Z
Controlador del Big Number.

Created on 01/06/2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""

from bignumber.dts_bignumber import BigN
from casosfem.dts_fem import CasosFEM


class CntBigN:
    """
    Cálcula el Big N de la máquina.
    Es el resultado de la suma de todos los ratios de las barras multiplicados
    por sus áreas y dividido por la suma de las áreas.

           Σ (ratio * area)
    BigN = ----------------
                Σ area
    """

    def __init__(self, ventana):
        """Inicializa la ventana de MainWindow."""

        self.v = ventana

    def calcula_big_n(self):
        """Cálcula el Big N."""

        bn = BigN()

        # Ratio ponderado de todas las barras y posiciones.
        casos_fem = CasosFEM(self.v.df_db)
        df_db1 = casos_fem.dataframe_fem1()
        df_db2 = casos_fem.dataframe_fem2()
        df_db3 = casos_fem.dataframe_fem3()

        self.v.big_n = bn.big_number(self.v.df_db)
        self.v.big_n1 = bn.big_number(df_db1)
        self.v.big_n2 = bn.big_number(df_db2)
        self.v.big_n3 = bn.big_number(df_db3)
        self.v.big_n_color = bn.big_number_color(self.v.big_n)
        self.v.big_n1_color = bn.big_number_color(self.v.big_n1)
        self.v.big_n2_color = bn.big_number_color(self.v.big_n2)
        self.v.big_n3_color = bn.big_number_color(self.v.big_n3)

        # Ratio ponderado de todas las barras con el valor máximo de FEM.
        self.v.big_n_fem = bn.big_number_fem(self.v.df_db)
        self.v.big_n_fem1 = bn.big_number_fem(df_db1)
        self.v.big_n_fem2 = bn.big_number_fem(df_db2)
        self.v.big_n_fem3 = bn.big_number_fem(df_db3)
        self.v.big_n_fem_color = bn.big_number_color(self.v.big_n_fem)
        self.v.big_n_fem1_color = bn.big_number_color(self.v.big_n_fem1)
        self.v.big_n_fem2_color = bn.big_number_color(self.v.big_n_fem2)
        self.v.big_n_fem3_color = bn.big_number_color(self.v.big_n_fem3)

        # Ratio máximo FEM.
        self.v.big_n_fem_max = bn.big_number_fem_max(self.v.df_db)
        self.v.big_n_fem1_max = bn.big_number_fem_max(df_db1)
        self.v.big_n_fem2_max = bn.big_number_fem_max(df_db2)
        self.v.big_n_fem3_max = bn.big_number_fem_max(df_db3)
        self.v.big_n_fem_max_color = bn.big_number_color(
            self.v.big_n_fem_max
        )
        self.v.big_n_fem1_max_color = bn.big_number_color(
            self.v.big_n_fem1_max
        )
        self.v.big_n_fem2_max_color = bn.big_number_color(
            self.v.big_n_fem2_max
        )
        self.v.big_n_fem3_max_color = bn.big_number_color(
            self.v.big_n_fem3_max
        )

        # Ratio ponderado de todas las barras.
        self.v.bign = bn.big_n(self.v.df_db)
        self.v.bign_1 = bn.big_n(df_db1)
        self.v.bign_2 = bn.big_n(df_db2)
        self.v.bign_3 = bn.big_n(df_db3)
        self.v.bign_color = bn.big_number_color(self.v.bign)
        self.v.bign_1_color = bn.big_number_color(self.v.bign_1)
        self.v.bign_2_color = bn.big_number_color(self.v.bign_2)
        self.v.bign_3_color = bn.big_number_color(self.v.bign_3)



        self.v.salida_big_n()
