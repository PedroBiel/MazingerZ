"""

MAZINGER Z
Datos de la columna Casos.

Created on 31/05/2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""

import pandas as pd


class ColCaso:
    """
    Convierte la columna Caso en enteros con el número del caso FEM
    despreciando la parte de texto.
    """

    def __init__(self, df):
        """Inicializa el DataFrame."""

        self.df = df

        self.column = 'Caso'

    def get_df(self):
        """Getter del DataFrame."""

        return self.df.copy()

    def col_split(self):
        """
        Convierte los valores alfanuméricos (str) de la columna a nñumeros
        enteros (int) ignorando la parte de texto del nombre del caso.
        :return:
        """

        df = self.get_df()
        df_temporal = pd.DataFrame(df[self.column].str.split(' ',1).tolist(),
                                   columns = ['caso_int','caso_str']
                                   )
        df[self.column] = df_temporal['caso_int']

        return df
