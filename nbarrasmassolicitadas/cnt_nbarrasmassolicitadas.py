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
from barramassolicitada.dts_barramassolicitada import BarraMasSolicitada


class CntNBarraMasSolicitadas:
    """Muestra los valores de las n barras más solicitadas."""

    def __init__(self, ventana):
        """Inicializa la ventana de MainWindow."""

        self.v = ventana

    def get_dataframe_db(self):
        """Getter del DataFrame con los datos de la base de datos."""

        return self.v.df_db.copy()

    def n_mas_solicitadas_1(self):
        """Valores de las n barras más solicitadas para FEM 1."""

        if self.v.df_db.empty == False:

            # Status bar.
            text = 'Generando datos de las n barras más solicitadas para FEM I.'
            self.v.status_bar(text)

            # # Datos.
            # caso = 1
            # db1_idxmax = self.mas_solicitada(caso)
            # self.v.call_dialogo_barra_mas_solicitada(caso, db1_idxmax)

            # Modelo
            df = self.get_dataframe_db()
            n_barras = NBarrasMax(df)  # TODO Crear dts_nbarrasmax
            df_n_barras_1 = n_barras.dataframe_max_fem1()
            model_1 = self.get_modelo(df_n_barras)

            # Salida en el diálogo.
            caso = 1
            self.v.call_dialogo_n_barras(df_n_barras_1, caso, model_1)

            # Status bar.
            text = 'N barras más solicitadas para FEM I.'
            self.v.status_bar(text)

    def mas_solicitada_2(self):
        """Valores de la barra más solicitada para FEM 2."""

        if self.v.df_db.empty == False:

            # Status bar.
            text = 'Generando datos de la barra más solicitada para FEM II.'
            self.v.status_bar(text)

            # Datos.
            caso = 2
            db2_idxmax = self.mas_solicitada(caso)
            self.v.call_dialogo_barra_mas_solicitada(caso, db2_idxmax)

            # Status bar.
            text = 'Barra más solicitada para FEM II.'
            self.v.status_bar(text)

    def mas_solicitada_3(self):
        """Valores de la barra más solicitada para FEM 1."""

        if self.v.df_db.empty == False:

            # Status bar.
            text = 'Generando datos de la barra más solicitada para FEM III.'
            self.v.status_bar(text)

            # Datos.
            caso = 3
            db3_idxmax = self.mas_solicitada(caso)
            self.v.call_dialogo_barra_mas_solicitada(caso, db3_idxmax)

            # Status bar.
            text = 'Barra más solicitada para FEM III.'
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
