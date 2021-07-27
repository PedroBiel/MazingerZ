"""

MAZINGER Z
Diálogo BarraMasSolicitada.

Created on 09/07/2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""

from PyQt5 import uic
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QAbstractScrollArea


class DlgBarraMasSolicitada(QDialog):
    """Diálogo BarraMasSolicitada."""

    def __init__(self, parent=None, caso=None, model=None):
        """
        Inicializa el DataFrame con los datos y el modelo
        :param parent: None.
        :param caso: int ; caso FEM.
        :param model: QTableView ; modelo del table view.
        """

        QDialog.__init__(self, parent)
        uic.loadUi('barramassolicitada/vst_nbarrasmassolicitadas.ui', self)

        self.caso = caso
        self.model = model

        # Widgets PyQt5.
        self.lbl = self.label
        # self.tbl = self.tableView
        self.txt = self.textEdit
        self.btn_cerrar = self.pushButton

        fuente_label = QFont()
        fuente_label.setPointSize(14)
        fuente_label.setBold(1)
        self.lbl.setFont(fuente_label)

        # Título de la ventana.
        self.setWindowTitle('Barra más solicitada')

        # Alto y anchomínima de la ventana.
        self.setMinimumHeight(620)
        self.setMinimumWidth(930)

        # Texto de etiquetas.
        if self.caso == 1:
            self.lbl.setText(
                'Barra más solicitada de los casos FEM I.'
            )
        elif self.caso == 2:
            self.lbl.setText(
                'Barra más solicitada de los casos FEM II.'
            )
        elif self.caso == 3:
            self.lbl.setText(
                'Barra más solicitada de los casos FEM III.'
            )

        # Modelo de la tabla.
        self.tbl.setModel(self.model)
        # Ajusta el ancho de las columnas a los contenidos.
        # self.tbl.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        # self.tbl.resizeColumnsToContents()

        # Botones.
        self.btn_cerrar.setText('Cerrar')
        self.btn_cerrar.setShortcut('Ctrl+Q')
        self.btn_cerrar.setToolTip('Cierra el diálogo | Ctrl+Q')

        # Eventos.
        self.btn_cerrar.clicked.connect(self.cierra_ventana)

    def cierra_ventana(self):
        """Cierra el diálogo."""

        self.reject()
