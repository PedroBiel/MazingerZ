"""

MAZINGER Z
Datos de la barra más solicitada.

Created on 14/07/2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


class DataFrame:
    """
    Pandas DataFrame con los datos para el cálculo de la barra más solicitada.
    """

    def __init__(self):
        """
        Sea df un DataFrame de pandas con los datos para el cálculo de la barra
        más solicitada, obtiene los valores de las columnas.
        """

    def get_df(self, df):
        """
        Getter del DataFrame.
        :param df: pandas DataFrame ; Datos para el cálculo de la barra más
                                      solicitada.
        """

        return df.copy()


class BarraMasSolicitada(DataFrame):
    """Fórmula para el cálculo de los datos de la barra más solicitada."""

    def __init__(self):
        """
        Sea df un DataFrame de pandas con los datos para el cálculo de la barra más
        solicitada, obtiene los valores correspondientes.

        :param df: pandas DataFrame ; Datos para el cálculo de la barra más
                                      solicitada.
        """

        DataFrame.__init__(self)

    def mas_solicitada(self, df):
        """
        Datos relativos a la barra más solicitada.
        :param df : pandas DataFrame ; Datos para el cálculo de la barra más
                                       solicitada.
        """

        _df = self.get_df(df)
        df_idxmax = _df.loc[_df['Ratio'].idxmax()]

        return df_idxmax
