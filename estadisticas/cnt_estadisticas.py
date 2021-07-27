"""

MAZINGER Z
Controlador de las estadísticas.

Created on 02/06/2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


from estadisticas.dts_estadisticas import Estadisticas
from estadisticas.tablemodel import PandasModel


class CntEstadisticas:
    """Muestra las estadísticas del DataFrame con los datos."""

    def __init__(self, ventana):
        """Inicializa la ventana de MainWindow."""

        self.v = ventana

    def get_dataframe_db(self):
        """Getter del DataFrame con los datos de la base de datos."""

        return self.v.df_db.copy()

    def describe(self):
        """Genera estadísticas descriptivas."""

        if self.v.df_db.empty == False:

            # Status bar.
            text = 'Generando las estadísticas descriptivas.'
            self.v.status_bar(text)

            # Modelo
            df = self.get_dataframe_db()
            estadisticas = Estadisticas(df)
            df_describe = estadisticas.dataframe_describe_fem()
            model = self.get_modelo(df_describe)

            # Salida en el diálogo.
            caso = 0
            self.v.call_dialogo_describe(df_describe, caso, model)

            # Status bar.
            text = 'Estadísticas descriptivas.'
            self.v.status_bar(text)

    def describe_1(self):
        """Genera estadísticas descriptivas de los casos FEM 1."""

        if self.v.df_db.empty == False:

            # Status bar.
            text = 'Generando las estadísticas descriptivas de los casos FEM ' \
                   'I. '
            self.v.status_bar(text)

            # Modelo.
            df = self.get_dataframe_db()
            estadisticas = Estadisticas(df)
            df_describe_1 = estadisticas.dataframe_describe_fem1()
            model_1 = self.get_modelo(df_describe_1)

            # Salida en el diálogo.
            caso = 1
            self.v.call_dialogo_describe(df_describe_1, caso, model_1)

            # Status bar.
            text = 'Estadísticas descriptivas de los casos FEM I.'
            self.v.status_bar(text)

    def describe_2(self):
        """Genera estadísticas descriptivas de los casos FEM 2."""

        if self.v.df_db.empty == False:

            # Status bar.
            text = 'Generando las estadísticas descriptivas de los casos FEM ' \
                   'II. '
            self.v.status_bar(text)

            # Modelo.
            df = self.get_dataframe_db()
            estadisticas = Estadisticas(df)
            df_describe_2 = estadisticas.dataframe_describe_fem2()
            model_2 = self.get_modelo(df_describe_2)

            # Salida en el diálogo.
            caso = 2
            self.v.call_dialogo_describe(df_describe_2, caso, model_2)

            # Status bar.
            text = 'Estadísticas descriptivas de los casos FEM II.'
            self.v.status_bar(text)

    def describe_3(self):
        """Genera estadísticas descriptivas de los casos FEM 3."""

        if self.v.df_db.empty == False:

            # Status bar.
            text = 'Generando las estadísticas descriptivas de los casos FEM ' \
                   'III. '
            self.v.status_bar(text)

            # Modelo.
            df = self.get_dataframe_db()
            estadisticas = Estadisticas(df)
            df_describe_3 = estadisticas.dataframe_describe_fem3()
            model_3 = self.get_modelo(df_describe_3)

            # Salida en el diálogo.
            caso = 3
            self.v.call_dialogo_describe(df_describe_3, caso, model_3)

            # Status bar.
            text = 'Estadísticas descriptivas de los casos FEM III.'
            self.v.status_bar(text)

    def get_modelo(self, df):
        """Getter del modelo con los datos del DataFrame."""

        model = PandasModel(df)

        return model
