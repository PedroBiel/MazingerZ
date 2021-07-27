"""

MAZINGER Z
Datos para los diagramas de dispersión.

Created on 31/05/2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""

import matplotlib.pyplot as plt


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


class ScatterPlot(DataFrame):
    """
    Scatter plot.
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

    def scatter_plot_fem(self, df, titulo, xlabel, ylabel, color):
        """
        Scatter plot del caso FEM particular.

        :param titulo: str ; título de la gráfica.
        :param xlabel: str ; etiqueta del eje x.
        :param ylabel: str ; etiqueta del eje y.
        :param color: str ; color del los puntos del gráfico.
        """

        fig = plt.figure(figsize=(9, 5))
        ax = fig.add_subplot()

        barras = self.get_barra(df)
        ratios = self.get_ratio(df)

        bottom = 0
        top = max(120, round(max(ratios) / 10, 0) * 10)
        ax.set_ylim(bottom, top)
        plt.axhline(y=100, xmin=0, xmax=max(barras), c='r')

        plt.scatter(x=barras, y=ratios, c=color, alpha=0.2)
        plt.xlabel(xlabel, fontsize=12)
        plt.ylabel(ylabel, fontsize=12)
        plt.title(titulo, fontsize=14)
        plt.show()

    def scatter_plot(
        self, df1, df2, df3, titulo, xlabel, ylabel, color1, color2, color3
        ):
        """
        Scatter plot del caso FEM particular.

        :param titulo: str ; título de la gráfica.
        :param xlabel: str ; etiqueta del eje x.
        :param ylabel: str ; etiqueta del eje y.
        :param color1: str ; color del los puntos FEM 1 del gráfico.
        :param color2: str ; color del los puntos FEM 2 del gráfico.
        :param color3: str ; color del los puntos FEM 3 del gráfico.
        """

        fig = plt.figure(figsize=(9, 5))
        ax = fig.add_subplot()

        barras_1 = self.get_barra(df1)
        barras_2 = self.get_barra(df2)
        barras_3 = self.get_barra(df3)

        max_barras_1 = max(barras_1)
        max_barras_2 = max(barras_2)
        max_barras_3 = max(barras_3)
        max_barras = max(max_barras_1, max_barras_2, max_barras_3)

        ratios_1 = self.get_ratio(df1)
        ratios_2 = self.get_ratio(df2)
        ratios_3 = self.get_ratio(df3)

        max_ratios_1 = max(ratios_1)
        max_ratios_2 = max(ratios_2)
        max_ratios_3 = max(ratios_3)
        max_ratios = max(max_ratios_1, max_ratios_2, max_ratios_3)

        bottom = 0
        top = max(120, round(max_ratios / 10, 0) * 10)
        ax.set_ylim(bottom, top)
        plt.axhline(y=100, xmin=0, xmax=max_barras, c='r')

        plt.scatter(x=barras_3, y=ratios_3, c=color3, alpha=0.2)
        plt.scatter(x=barras_2, y=ratios_2, c=color2, alpha=0.2)
        plt.scatter(x=barras_1, y=ratios_1, c=color1, alpha=0.2)

        plt.xlabel(xlabel, fontsize=12)
        plt.ylabel(ylabel, fontsize=12)
        plt.title(titulo, fontsize=14)
        plt.show()
