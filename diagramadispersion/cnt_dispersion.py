"""

MAZINGER Z
Controlador de los diagramas de dispersión.

Created on 07/06/2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""

from casosfem.dts_fem import CasosFEM
from diagramadispersion.constantes_dispersion import Constantes
from diagramadispersion.dts_scatter import ScatterPlot


class CntDiagramaDispersion:
    """Crea los diagramas de dispersión con los datos de la base de datos."""

    def __init__(self, ventana):
        """Inicializa la ventana de MainWindow."""

        self.v = ventana

        self.constantes = Constantes()
        self.titulo_dispersion = self.constantes.get_titulo_dispersion()
        self.titulo_dispersion_1 = self.constantes.get_titulo_dispersion_1()
        self.titulo_dispersion_2 = self.constantes.get_titulo_dispersion_2()
        self.titulo_dispersion_3 = self.constantes.get_titulo_dispersion_3()
        self.xlabel = self.constantes.get_xlabel()
        self.ylabel = self.constantes.get_ylabel()

        self.scatter_plot = ScatterPlot()

    def dispersion(self):
        """Diagrama de dispersión."""

        if self.v.df_db.empty == False:

            # Status bar.
            text = 'Generando el diagrama de dispersión.'
            self.v.status_bar(text)

            # Gráfica.
            casos_fem = CasosFEM(self.v.df_db)
            df_db1 = casos_fem.dataframe_fem1()
            df_db2 = casos_fem.dataframe_fem2()
            df_db3 = casos_fem.dataframe_fem3()

            color1 = 'blue'
            color2 = 'green'
            color3 = 'orange'
            self.scatter_plot.scatter_plot(
                df_db1, df_db2, df_db3, self.titulo_dispersion, self.xlabel,
                self.ylabel, color1, color2, color3
            )

            # Status bar.
            text = 'Diagrama de dispersión.'
            self.v.status_bar(text)

    def dispersion_1(self):
        """Diagrama de dispersión de FEM 1."""

        if self.v.df_db.empty == False:

            # Status bar.
            text = 'Generando el diagrama de dispersión FEM I.'
            self.v.status_bar(text)

            # Gráfica.
            casos_fem = CasosFEM(self.v.df_db)
            df_db1 = casos_fem.dataframe_fem1()

            color = 'blue'
            self.scatter_plot.scatter_plot_fem(
                df_db1, self.titulo_dispersion_1, self.xlabel, self.ylabel,
                color
            )

            # Status bar.
            text = 'Diagrama de dispersión FEM I.'
            self.v.status_bar(text)

    def dispersion_2(self):
        """Diagrama de dispersión de FEM 2."""

        if self.v.df_db.empty == False:

            # Status bar.
            text = 'Generando el diagrama de dispersión FEM II.'
            self.v.status_bar(text)

            # Gráfica.
            casos_fem = CasosFEM(self.v.df_db)
            df_db2 = casos_fem.dataframe_fem2()

            color = 'green'
            self.scatter_plot.scatter_plot_fem(
                df_db2, self.titulo_dispersion_2, self.xlabel, self.ylabel,
                color
            )

            # Status bar.
            text = 'Diagrama de dispersión FEM II.'
            self.v.status_bar(text)

    def dispersion_3(self):
        """Diagrama de dispersión de FEM 3."""

        if self.v.df_db.empty == False:

            # Status bar.
            text = 'Generando el diagrama de dispersión FEM II.'
            self.v.status_bar(text)

            # Gráfica.
            casos_fem = CasosFEM(self.v.df_db)
            df_db3 = casos_fem.dataframe_fem3()

            color = 'orange'
            self.scatter_plot.scatter_plot_fem(
                df_db3, self.titulo_dispersion_3, self.xlabel, self.ylabel,
                color
            )

            # Status bar.
            text = 'Diagrama de dispersión FEM III.'
            self.v.status_bar(text)
