"""

MAZINGER Z
Datos de los tipos de las columnas del DataFrame importado de la base de
datos.

Created on 31/05/2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""

import numpy as np


class DFAstype:
    """Convierte un objeto pandas en un dtype especificado."""

    def __init__(self, df):
        """Inicializa el DataFrame."""

        self.df = df

        self.cols = [
            'Area', 'Smax', 'Smin', 'SmaxMy', 'SmaxMz', 'SminMy', 'SminMz',
            'Sx', 'Ty', 'Tz', 'T', 'Mises', 'Limite', 'Ratio'
        ]  # Dolumnas del DataFrame donde replacar comas por puntos y NaN.

    def get_df_columns(self):
        """Getter de la lista con los nombres de las columnas."""

        return list(self.df.columns)

    def replace_astype(self):
        """
        Sustituya 'comas' de los decimales por 'puntos' dcimales y
        convierte cada column en el dtype especificado.
        """

        df_replaced_comas = self.replace_comas_por_puntos()
        df_replaced_nan = self.replace_nan(df_replaced_comas)
        df_astype = self.as_type(df_replaced_nan)

        return df_astype

    def replace_comas_por_puntos(self):
        """Sustituya 'comas' de los decimales por 'puntos' dcimales."""

        df_sin_comas = self.df.copy()

        for col in self.cols:
            df_sin_comas[col] = df_sin_comas[col].str.replace(',', '.')

        return df_sin_comas

    def replace_nan(self, df):
        """Reemplaza NaN por ceros."""

        df_sin_nan = df.copy()

        for col in self.cols:
            df_sin_nan[col] = df_sin_nan[col].replace(np.nan, 0.)

        return df_sin_nan

    def as_type(self, df):
        """
        Convierte cada column en el dtype especificado.
        https://pbpython.com/pandas_dtypes.html
        """

        df_new = df.astype({
            'Modelo': 'str',
            'Barra': 'int32',
            'Seccion': 'str',
            'Area': 'float32',
            'Material': 'str',
            'Caso': 'int',
            'Nombre': 'str',
            'Punto': 'str',
            'Smax': 'float32',
            'Smin': 'float32',
            'SmaxMy': 'float32',
            'SmaxMz': 'float32',
            'SminMy': 'float32',
            'SminMz': 'float32',
            'Sx': 'float32',
            'Ty': 'float32',
            'Tz': 'float32',
            'T': 'float32',
            'Mises': 'float32',
            'Limite': 'float32',
            'Ratio': 'float32'
        })

        return df_new
