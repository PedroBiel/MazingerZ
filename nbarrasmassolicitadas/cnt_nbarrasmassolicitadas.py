"""

MAZINGER Z
Controlador de la barra más solicitada.

Created on 09/07/2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


from casosfem.dts_fem import CasosFEM
# from barramassolicitada.tablemodel import PandasModel
# from barramassolicitada.dts_barramassolicitada import BarraMasSolicitada
from nbarrasmassolicitadas.dts_nbarrasmassolicitadas import NBarrasMax
from nbarrasmassolicitadas.tablemodel import PandasModel


class CntNBarraMasSolicitadas:
    """Muestra los valores de las n barras más solicitadas."""

    def __init__(self, ventana):
        """Inicializa la ventana de MainWindow."""

        self.v = ventana

    def get_dataframe_db(self):
        """Getter del DataFrame con los datos de la base de datos."""

        return self.v.df_db.copy()

    def get_n_barras(self):
        """Getter del número de barras más solicitadas a mostrar."""

        return self.v.lne_n_barras.text()

    def n_mas_solicitadas_1(self):
        """Valores de las n barras más solicitadas para FEM 1."""

        if self.v.df_db.empty == False:

            # Status bar.
            text = 'Generando datos de las n barras más solicitadas para FEM I.'
            self.v.status_bar(text)

            # Modelo
            n_barras = self.get_n_barras()
            df = self.get_dataframe_db()
            n_barras_max = NBarrasMax(df, n_barras)
            df_n_barras_1 = n_barras_max.mas_solicitadas_1()
            model_1 = self.get_modelo(df_n_barras_1)

            # Salida en el diálogo.
            caso = 1
            self.v.call_dialogo_n_barras(df_n_barras_1, caso, model_1)

            # Status bar.
            text = 'Las ' + str(n_barras) + ' barras más solicitadas para FEM I.'
            self.v.status_bar(text)

    def n_mas_solicitadas_2(self):
        """Valores de la barra más solicitada para FEM 2."""

        if self.v.df_db.empty == False:
            # Status bar.
            text = 'Generando datos de las n barras más solicitadas para FEM ' \
                    'II.'
            self.v.status_bar(text)

            # Modelo
            n_barras = self.get_n_barras()
            df = self.get_dataframe_db()
            n_barras_max = NBarrasMax(df, n_barras)
            df_n_barras_2 = n_barras_max.mas_solicitadas_2()
            model_2 = self.get_modelo(df_n_barras_2)

            # Salida en el diálogo.
            caso = 2
            self.v.call_dialogo_n_barras(df_n_barras_2, caso, model_2)

            # Status bar.
            text = 'Las ' + str(
                n_barras) + ' barras más solicitadas para FEM II.'
            self.v.status_bar(text)

    def n_mas_solicitadas_3(self):
        """Valores de la barra más solicitada para FEM 1."""

        if self.v.df_db.empty == False:
            # Status bar.
            text = 'Generando datos de las n barras más solicitadas para FEM ' \
                   'III.'
            self.v.status_bar(text)

            # Modelo
            n_barras = self.get_n_barras()
            df = self.get_dataframe_db()
            n_barras_max = NBarrasMax(df, n_barras)
            df_n_barras_3 = n_barras_max.mas_solicitadas_3()
            model_3 = self.get_modelo(df_n_barras_3)

            # Salida en el diálogo.
            caso = 3
            self.v.call_dialogo_n_barras(df_n_barras_3, caso, model_3)

            # Status bar.
            text = 'Las ' + str(
                n_barras) + ' barras más solicitadas para FEM III.'
            self.v.status_bar(text)

    def mas_solicitada(self, caso):
        """
        Valores de la barra más solicitada.
        caso : int ; caso FEM
        """

        df_db = ''
        casos_fem = CasosFEM(self.v.df_db)
        if caso == 1:
            df_db = casos_fem.dataframe_fem1()
        elif caso == 2:
            df_db = casos_fem.dataframe_fem2()
        elif caso == 3:
            df_db = casos_fem.dataframe_fem3()
        else:
            print('Oops!')

        barra = BarraMasSolicitada()
        db_idxmax = barra.mas_solicitada(df_db)

        return db_idxmax

    def get_modelo(self, df):
        """Getter del modelo con los datos del DataFrame."""

        model = PandasModel(df)

        return model

