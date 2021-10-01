"""

MAZINGER Z
Controlador de las barras de estudio.

Created on 17/09/2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


from barrasestudio.dts_barrasestudio import BarrasEstudio

class CntBarrasEstudio:
    """Barras de las que se mostrarán los datos."""

    def __init__(self, ventana):
        """Inicializa la ventana de MainWindow."""

        self.v = ventana

    def get_barras_estudio(self):
        """Getter de las barras de estucio."""

        return self.v.barras_estudio.text()

    def barras_de_estudio(self):
        """Pasa el string de las barras de estudio a una lista."""

        get_barras_estudio = self.get_barras_estudio()

        barrasestudio = BarrasEstudio(get_barras_estudio)
        self.v.barras = barrasestudio.str2list()
        print('CntBarrasEstudio.barras_de_estudio', self.v.barras)
