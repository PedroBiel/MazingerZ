"""

MAZINGER Z
Modelo para los diagramas de la distribución acumulada y de la densidad de
probabilidad.

Created on 08/06/2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib import mlab


class DataFrame:
    """Pandas DataFrame con los datos para la representación del plot."""

    def __init__(self):
        """
        Sea df un DataFrame de pandas con los datos para la representación del
        plot, obtiene los valores de las columnas.
        """

    def get_df(self, df):
        """
        Getter del DataFrame.
        :param df: pandas DataFrame ; Datos para la representación de la
                                      gráfica.
        """

        return df.copy()

    def get_barra(self, df):
        """
        Getter de la barra.
        :param df: pandas DataFrame ; Datos para la representación de la
                                      gráfica.
        """

        return df['Barra'].copy()

    def get_ratio(self, df):
        """
        Getter del ratio.
        :param df: pandas DataFrame ; Datos para la representación de la
                                      gráfica.
        """

        return df['Ratio'].copy()


class HistPlot(DataFrame):
    """
    Histograma.
    :param df: pandas DataFrame ; Datos para la representación de la gráfica.
    """

    def __init__(self):
        """
        Sea df un DataFrame de pandas con los datos para la representación de
        la gráfica, obtiene la gráfica.

        :param df: pandas DataFrame ; datos para la representación de la
                                      gráfica.

        """

        DataFrame.__init__(self)

    def hist_plot_fem(self, df, titulo_distr_acum, color):
        """Histograma para cada caso FEM particular."""

        # Para cada grupo  ['Caso', 'Barra', 'Punto'] busca la fila con el
        # valor máximo de 'Ratio'.
        idx = df.groupby([
            'Caso', 'Barra', 'Punto'])[
                  'Ratio'].transform(max) == df['Ratio']
        __df = df[idx].copy()

        ratio = self.get_ratio(__df)

        fig = plt.figure(figsize=(6, 6))
        sns.histplot(data=ratio, bins=50, kde=True, color=color).set_title(
            titulo_distr_acum
        )
        ax2 = plt.twinx()
        sns.kdeplot(data=ratio, cumulative=True, ax=ax2, color=color) #.set_title(titulo_dens_prob)
        plt.show()
