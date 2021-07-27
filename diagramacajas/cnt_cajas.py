"""

MAZINGER Z
Controlador de los diagramas de cajas.

Created on 10/06/2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""

from casosfem.dts_fem import CasosFEM
from diagramacajas.dts_cajas import BoxPlot

class CntDiagramaCajas:
    """Crea los diagramas de cajas con los datos de la base de datos."""

    def __init__(self, ventana):
        """Inicializa la ventana de MainWindow."""

        self.v = ventana

        self.box_plot = BoxPlot()


    def cajas(self):
        """Diagrama de cajas."""

        # Status bar.
        text = 'Generando el diagrama de cajas.'
        self.v.status_bar(text)

        # Gráfica.
        casos_fem = CasosFEM(self.v.df_db)
        df_db1 = casos_fem.dataframe_fem1()
        df_db2 = casos_fem.dataframe_fem2()
        df_db3 = casos_fem.dataframe_fem3()

        color1 = 'blue'
        color2 = 'green'
        color3 = 'orange'

        self.box_plot.box_plot(df_db1, df_db2, df_db3, color1, color2, color3)