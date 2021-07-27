"""

MAZINGER Z
Controlador de los diagramas de distribución acumulada y de la densidad de
probabilidad.

Created on 08/06/2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from casosfem.dts_fem import CasosFEM
from diagramadistribucionacumulada.constantes_distracum import Constantes
from diagramadistribucionacumulada.dts_distracum import HistPlot

class CntDiagramaDistribucionAcumulada:
    """
    Crea los diagramas de la distribución acumulada y de la densidad de
    probabilidad.
    """

    def __init__(self, ventana):
        """Inicializa la ventana de MainWindow."""

        self.v = ventana

        self.constantes = Constantes()
        self.titulo_distr_acum_1 = self.constantes.get_titulo_distr_acum_1()
        self.titulo_distr_acum_2 = self.constantes.get_titulo_distr_acum_2()
        self.titulo_distr_acum_3 = self.constantes.get_titulo_distr_acum_3()

        self.hist_plot = HistPlot()

    def distribucion_acumulada_1(self):
        """
        Diagrama de la distribución acumulada y de la densidad de probabilidad.
        """

        if self.v.df_db.empty == False:

            # Status bar.
            text = 'Generando el diagrama de la distribución acumulada de la '\
                'probabilidad de la densidad FEM I.'
            self.v.status_bar(text)

            # Gráfica.
            casos_fem = CasosFEM(self.v.df_db)
            df_db1 = casos_fem.dataframe_fem1()
            color1 = 'blue'

            self.hist_plot.hist_plot_fem(
                df_db1, self.titulo_distr_acum_1, color1
            )

            # Status bar.
            text = 'Diagrama de la distribución acumulada de la '\
                'probabilidad de la densidad FEM I.'
            self.v.status_bar(text)

    def distribucion_acumulada_2(self):
        """
        Diagrama de la distribución acumulada y de la densidad de probabilidad.
        """

        if self.v.df_db.empty == False:

            # Status bar.
            text = 'Generando el diagrama de la distribución acumulada de la '\
                'probabilidad de la densidad FEM II.'
            self.v.status_bar(text)

            # Gráfica.
            casos_fem = CasosFEM(self.v.df_db)
            df_db2 = casos_fem.dataframe_fem2()
            color2 = 'green'

            self.hist_plot.hist_plot_fem(
                df_db2, self.titulo_distr_acum_2, color2
            )

            # Status bar.
            text = 'Diagrama de la distribución acumulada de la ' \
                   'probabilidad de la densidad FEM II.'
            self.v.status_bar(text)

    def distribucion_acumulada_3(self):
        """
        Diagrama de la distribución acumulada y de la densidad de probabilidad.
        """

        if self.v.df_db.empty == False:

            # Status bar.
            text = 'Generando el diagrama de la distribución acumulada de la '\
                'probabilidad de la densidad FEM III.'
            self.v.status_bar(text)

            # Gráfica.
            casos_fem = CasosFEM(self.v.df_db)
            df_db3 = casos_fem.dataframe_fem3()
            color3 = 'orange'

            self.hist_plot.hist_plot_fem(
                df_db3, self.titulo_distr_acum_3, color3
            )

            # Status bar.
            text = 'Diagrama de la distribución acumulada de la ' \
                   'probabilidad de la densidad FEM III.'
            self.v.status_bar(text)
