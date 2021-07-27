"""

MAZINGER Z
Controlador de la barra más solicitada.

Created on 09/07/2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


from casosfem.dts_fem import CasosFEM
from barramassolicitada.tablemodel import PandasModel


class CntBarraMasSolicitada:
    """Muestra los valores de la barra más solicitada."""

    def __init__(self, ventana):
        """Inicializa la ventana de MainWindow."""

        self.v = ventana

    def mas_solicitada_1(self):
        """Valores de la barra más solicitada para FEM 1."""

        if self.v.df_db.empty == False:

            # Status bar.
            text = 'Generando datos de la barra más solicitada para FEM I.'
            self.v.status_bar(text)

            # modelo.
            casos_fem = CasosFEM(self.v.df_db)
            df_db1 = casos_fem.dataframe_fem1()
            df_db1_idxmax = df_db1.loc[df_db1['Ratio'].idxmax()]
            print(df_db1_idxmax)
            print(df_db1_idxmax.shape)
            print(df_db1_idxmax.info)
            model_1 = self.get_modelo(df_db1_idxmax)

            # Salida en el diálogo.
            caso = 1
            self.v.call_dialogo_barra_mas_solicitada(caso, model_1)

    def get_modelo(self, df):
        """Getter del modelo con los datos del DataFrame."""

        model = PandasModel(df)

        return model