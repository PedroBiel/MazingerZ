"""

MAZINGER Z
Datos para los diagramas de cajas.

Created on 10/06/2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""

import matplotlib.pyplot as plt
import seaborn as sns

class DataFrame:
    """Pandas DataFrame con los datos para la representación del plot."""

    def __init__(self):
        """
        Sea df un DataFrame de pandas con los datos para la representación del
        plot, obtiene los valores de las columnas.
        """

    def get_ratio(self, df):
        """
        Getter del ratio.
        :param df: pandas DataFrame ; Datos para la representación de la
                                      gráfica.
        """

        return df['Ratio'].copy()



class BoxPlot(DataFrame):
    """
    Box plot.
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

    def box_plot(self, df1, df2, df3, color1, color2, color3):

        ratio1 = self.get_ratio(df1)
        ratio2 = self.get_ratio(df2)
        ratio3 = self.get_ratio(df3)

        fig, ax = plt.subplots(1, 3, figsize=(14, 5))

        sns.boxplot(y=ratio1, ax=ax[0], color=color1).set_title('FEM I')
        sns.boxplot(y=ratio2, ax=ax[1], color=color2).set_title('FEM II')
        sns.boxplot(y=ratio3, ax=ax[2], color=color3).set_title('FEM III')

        sns.pointplot(y=ratio1, ax=ax[0], color='red')
        sns.pointplot(y=ratio2, ax=ax[1], color='red')
        sns.pointplot(y=ratio3, ax=ax[2], color='red')

        plt.show()
