# -*- coding: utf-8 -*-
"""

MAZINGER Z
Muestra los resultados de las tensiones según FEM 2131/2132

Created on 28/05/2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""

import matplotlib as plt
import pandas as pd
import qtmodern.styles
import qtmodern.windows
import sqlite3

import sys

from PyQt5 import uic
from PyQt5.QtCore import QLibraryInfo, QLocale, QRegExp, Qt, QTranslator
from PyQt5.QtGui import (
    QFont, QIcon, QIntValidator, QKeySequence, QRegExpValidator
)
from PyQt5.QtWidgets import QApplication, QMainWindow

from barrasestudio.cnt_barrasestudio import CntBarrasEstudio
from importadb.cnt_importadb import CntImportaDBDF
from bignumber.cnt_bignumber import CntBigN
from estadisticas.cnt_estadisticas import CntEstadisticas
from estadisticas.dlg_describe import DlgDescribe
from diagramadispersion.cnt_dispersion import CntDiagramaDispersion
from diagramadistribucionacumulada.cnt_distribucionacumulada import \
    CntDiagramaDistribucionAcumulada
from diagramacajas.cnt_cajas import CntDiagramaCajas
from barramassolicitada.cnt_barramassolicitada import CntBarraMasSolicitada
from barramassolicitada.dlg_barramassolicitada import DlgBarraMasSolicitada
from nbarrasmassolicitadas.cnt_nbarrasmassolicitadas import \
    CntNBarraMasSolicitadas
from nbarrasmassolicitadas.dlg_nbarrasmassolicitadas import \
    DlgNBarrasMasSolicitadas


class MainWindow(QMainWindow):

    def __init__(self, parent=None):

        QMainWindow.__init__(self, parent)
        uic.loadUi('vistas/mazingerz.ui', self)

        # Entorno virtual
        print('\nEntorno virtual:', sys.prefix)
        print('pandas', pd.__version__)
        print('python', sys.version)
        print('qtmodern', qtmodern.__version__)

        # Icono y título de la ventana.
        self.setWindowIcon(QIcon("img/Mazinger-Z.ico"))
        self.setWindowTitle("Mazinge Z 0.0.0 beta")

        # Librerías.
        self.plt = plt
        self.sqlite3 = sqlite3

        # Parámetros.
        self.barras = []  # list int; barras de estudio.
        self.df_db = pd.DataFrame()  # pandas DataFrame; datos.
        self.nombre_db = ''  # str; nombre de la base de datos.
        self.big_n = 0  # float; The Big Number.
        self.big_n1 = 0  # float; The Big Number para FEM I.
        self.big_n2 = 0  # float; The Big Number para FEM II.
        self.big_n3 = 0  # float; The Big Number para FEM III.
        self.big_n_fem = 0  # float; The Big Number para máximos.
        self.big_n_fem1 = 0  # float; The Big Number para máximos de FEM I.
        self.big_n_fem2 = 0  # float; The Big Number para máximos de FEM II.
        self.big_n_fem3 = 0  # float; The Big Number para máximos de FEM III.
        self.big_n_fem_max = 0  # float; The Big Number máximo.
        self.big_n_fem1_max = 0  # float; The Big Number máximo de FEM I.
        self.big_n_fem2_max = 0  # float; The Big Number máximo de FEM II.
        self.big_n_fem3_max = 0  # float; The Big Number máximo de FEM III.
        self.bign = 0  # float; The Big Number.
        self.bign_1 = 0  # float; The Big Number para FEM I.
        self.bign_2 = 0  # float; The Big Number para FEM II.
        self.bign_3 = 0  # float; The Big Number para FEM III.
        self.big_n_color = ''  # str; Color del Big Number para label.
        self.big_n1_color = ''  # str; Color del Big Number para label.
        self.big_n2_color = ''  # str; Color del Big Number para label.
        self.big_n3_color = ''  # str; Color del Big Number para label.
        self.big_n_fem_color = ''  # str; Color del Big Number para label.
        self.big_n_fem1_color = ''  # str; Color del Big Number para label.
        self.big_n_fem2_color = ''  # str; Color del Big Number para label.
        self.big_n_fem3_color = ''  # str; Color del Big Number para label.
        self.big_n_fem_max_color = ''  # str; Color del Big Number para label.
        self.big_n_fem1_max_color = ''  # str; Color del Big Number para label.
        self.big_n_fem2_max_color = ''  # str; Color del Big Number para label.
        self.big_n_fem3_max_color = ''  # str; Color del Big Number para label.
        self.bign_color = ''  # str; Color del Big Number para label.
        self.bign_1_color = ''  # str; Color del Big Number para label.
        self.bign_2_color = ''  # str; Color del Big Number para label.
        self.bign_3_color = ''  # str; Color del Big Number para label.
        self.n_barras = 10  # int; Nº de barras más solicitadas a mostrar.

        # QObjects.
        self.lbl_titulo = self.labelTitulo
        self.barras_estudio = self.lineEditBarrasEstudio
        regex = QRegExp("[CATOBYcatoby0-9 ]+")
        validator = QRegExpValidator(regex)
        self.barras_estudio.setValidator(validator)

        # - Importar base de datos.
        self.btn_importar = self.pushButtonImportar
        self.btn_importar.setToolTip('Importa base de datos | Ctrl+I')
        self.btn_importar.setShortcut(QKeySequence('Ctrl+I'))
        self.lbl_nombre_db = self.labelNombreDB
        self.lbl_importar = self.labelImportar

        # - The Big Numbers.
        self.lbl_big_n = self.labelBigNumber
        self.lbl_big_n.setToolTip(
            'Ratio ponderado en los puntos de todas las barras con el valor '
            'máximo FEM.')
        self.lbl_big_n1 = self.labelBigNumber1
        self.lbl_big_n1.setToolTip(
            'Ratio ponderado en los puntos de todas las barras con el valor '
            'máximo FEM I.')
        self.lbl_big_n2 = self.labelBigNumber2
        self.lbl_big_n2.setToolTip(
            'Ratio ponderado en los puntos de todas las barras con el valor '
            'máximo FEM II.')
        self.lbl_big_n3 = self.labelBigNumber3
        self.lbl_big_n3.setToolTip(
            'Ratio ponderado en los puntos de todas las barras con el valor '
            'máximo FEM III.')

        self.lbl_big_n_fem = self.labelBigNumberFEM
        self.lbl_big_n_fem.setToolTip(
            'Ratio ponderado de todas las barras con el valor máximo de '
            'FEM.')
        self.lbl_big_n_fem1 = self.labelBigNumberFEM1
        self.lbl_big_n_fem1.setToolTip(
            'Ratio ponderado de todas las barras con el valor máximo de '
            'FEM I.')
        self.lbl_big_n_fem2 = self.labelBigNumberFEM2
        self.lbl_big_n_fem2.setToolTip(
            'Ratio ponderado de todas las barras con el valor máximo de '
            'FEM II.')
        self.lbl_big_n_fem3 = self.labelBigNumberFEM3
        self.lbl_big_n_fem3.setToolTip(
            'Ratio ponderado de todas las barras con el valor máximo de '
            'FEM III.')

        self.lbl_big_n_fem_max = self.labelBigNumberFEMmax
        self.lbl_big_n_fem_max.setToolTip('Ratio máximo FEM.')
        self.lbl_big_n_fem1_max = self.labelBigNumberFEM1max
        self.lbl_big_n_fem1_max.setToolTip('Ratio máximo FEM I.')
        self.lbl_big_n_fem2_max = self.labelBigNumberFEM2max
        self.lbl_big_n_fem2_max.setToolTip('Ratio máximo FEM II.')
        self.lbl_big_n_fem3_max = self.labelBigNumberFEM3max
        self.lbl_big_n_fem3_max.setToolTip('Ratio máximo FEM III.')

        self.lbl_bign = self.labelBigN
        self.lbl_bign.setToolTip('Ratio ponderado de todas las barras.')
        self.lbl_bign_1 = self.labelBigN1
        self.lbl_bign_1.setToolTip(
            'Ratio ponderado de todas las barras con los casos FEM I.')
        self.lbl_bign_2 = self.labelBigN2
        self.lbl_bign_2.setToolTip(
            'Ratio ponderado de todas las barras con los casos FEM II.')
        self.lbl_bign_3 = self.labelBigN3
        self.lbl_bign_3.setToolTip(
            'Ratio ponderado de todas las barras con los casos FEM III.')

        # - Estadísticas.
        self.btn_describe = self.pushButtonDescribe
        self.btn_describe.setToolTip('Estadísticas de los resultados | Ctrl+E')
        self.btn_describe.setShortcut(QKeySequence('Ctrl+E'))
        self.btn_describe_1 = self.pushButtonDescribeFEM1
        self.btn_describe_1.setToolTip(
            'Estadísticas de los casos FEM 1 | Ctrl+1'
        )
        self.btn_describe_1.setShortcut(QKeySequence('Ctrl+1'))
        self.btn_describe_2 = self.pushButtonDescribeFEM2
        self.btn_describe_2.setToolTip(
            'Estadísticas de los casos FEM 2 | Ctrl+2'
        )
        self.btn_describe_2.setShortcut(QKeySequence('Ctrl+2'))
        self.btn_describe_3 = self.pushButtonDescribeFEM3
        self.btn_describe_3.setToolTip(
            'Estadísticas de los casos FEM 3 | Ctrl+3')
        self.btn_describe_3.setShortcut(QKeySequence('Ctrl+3'))
        # - Diagramas de dispersión.
        self.btn_dispersion = self.pushButtonDispersion
        self.btn_dispersion.setToolTip(
            'Diagrama de dispersión de los resultados | Ctrl+D')
        self.btn_dispersion.setShortcut(QKeySequence('Ctrl+D'))
        self.btn_dispersion_1 = self.pushButtonDispersionFEM1
        self.btn_dispersion_1.setToolTip(
            'Diagrama de dispersión de los casos FEM 1 | Ctrl+F')
        self.btn_dispersion_1.setShortcut(QKeySequence('Ctrl+F'))
        self.btn_dispersion_2 = self.pushButtonDispersionFEM2
        self.btn_dispersion_2.setToolTip(
            'Diagrama de dispersión de los casos FEM 2 | Ctrl+G')
        self.btn_dispersion_2.setShortcut(QKeySequence('Ctrl+G'))
        self.btn_dispersion_3 = self.pushButtonDispersionFEM3
        self.btn_dispersion_3.setToolTip(
            'Diagrama de dispersión de los casos FEM 3 | Ctrl+H')
        self.btn_dispersion_3.setShortcut(QKeySequence('Ctrl+H'))
        # - Diagramas de la distribución acumulada y de la densidad de
        # - probabilidad.
        self.btn_distr_acum_1 = self.pushButtonDistrAcumFEM1
        self.btn_distr_acum_1.setToolTip(
            'Diagrama de distribución acumulada y de la densidad de '
            'probabilidad de los casos FEM 1 | Ctrl+J')
        self.btn_distr_acum_1.setShortcut(QKeySequence('Ctrl+J'))
        self.btn_distr_acum_2 = self.pushButtonDistrAcumFEM2
        self.btn_distr_acum_2.setToolTip(
            'Diagrama de distribución acumulada y de la densidad de '
            'probabilidad de los casos FEM 2 | Ctrl+K')
        self.btn_distr_acum_2.setShortcut(QKeySequence('Ctrl+K'))
        self.btn_distr_acum_3 = self.pushButtonDistrAcumFEM3
        self.btn_distr_acum_3.setToolTip(
            'Diagrama de distribución acumulada y de la densidad de '
            'probabilidad de los casos FEM 3 | Ctrl+L')
        self.btn_distr_acum_3.setShortcut(QKeySequence('Ctrl+L'))
        # - Diagramas de cajas.
        self.btn_cajas = self.pushButtonCajas
        self.btn_cajas.setToolTip(
            'Diagramas de cajas de los casos FEM. | Ctrl+C')
        self.btn_cajas.setShortcut(QKeySequence('Ctrl+C'))
        # - Barra más solicitada.
        self.btn_barra_fem1 = self.pushButtonBarraFEM1
        self.btn_barra_fem1.setToolTip(
            'Barra más solicitada para FEM 1 | Ctrl+Z')
        self.btn_barra_fem1.setShortcut(QKeySequence('Ctrl+Z'))
        self.btn_barra_fem2 = self.pushButtonBarraFEM2
        self.btn_barra_fem2.setToolTip(
            'Barra más solicitada para FEM 2 | Ctrl+X')
        self.btn_barra_fem2.setShortcut(QKeySequence('Ctrl+X'))
        self.btn_barra_fem3 = self.pushButtonBarraFEM3
        self.btn_barra_fem3.setToolTip(
            'Barra más solicitada para FEM 3 | Ctrl+C')
        self.btn_barra_fem3.setShortcut(QKeySequence('Ctrl+C'))
        # - Las n barras más solicitadas.
        self.lne_n_barras = self.lineEditNBarras
        self.lne_n_barras.setAlignment(Qt.AlignCenter)
        validator = QIntValidator(1, 20, self)  # Mínimo 1, máximo 20 barras.
        self.lne_n_barras.setValidator(validator)
        self.lne_n_barras.setText('10')
        self.btn_n_barras_fem1 = self.pushButtonNBarrasFEM1
        self.btn_n_barras_fem2 = self.pushButtonNBarrasFEM2
        self.btn_n_barras_fem3 = self.pushButtonNBarrasFEM3

        # - Cerrar aplicación.
        self.btn_cerrar = self.pushButtonCerrar
        self.btn_cerrar.setToolTip('Cierra la aplicación | Ctrl+Q')

        fuente_titulo = QFont()
        fuente_titulo.setFamily('Consolas')
        fuente_titulo.setPointSize(16)
        fuente_titulo.setBold(1)
        self.lbl_titulo.setFont(fuente_titulo)

        fuente_big_n = QFont()
        fuente_big_n.setFamily('Consolas')
        fuente_big_n.setPointSize(18)
        fuente_big_n.setBold(1)
        self.lbl_big_n.setFont(fuente_big_n)
        self.lbl_big_n1.setFont(fuente_big_n)
        self.lbl_big_n2.setFont(fuente_big_n)
        self.lbl_big_n3.setFont(fuente_big_n)
        self.lbl_big_n_fem.setFont(fuente_big_n)
        self.lbl_big_n_fem1.setFont(fuente_big_n)
        self.lbl_big_n_fem2.setFont(fuente_big_n)
        self.lbl_big_n_fem3.setFont(fuente_big_n)
        self.lbl_big_n_fem_max.setFont(fuente_big_n)
        self.lbl_big_n_fem1_max.setFont(fuente_big_n)
        self.lbl_big_n_fem2_max.setFont(fuente_big_n)
        self.lbl_big_n_fem3_max.setFont(fuente_big_n)
        self.lbl_bign.setFont(fuente_big_n)
        self.lbl_bign_1.setFont(fuente_big_n)
        self.lbl_bign_2.setFont(fuente_big_n)
        self.lbl_bign_3.setFont(fuente_big_n)

        # Instancias de clase.
        self.cnt_barras_estudio = CntBarrasEstudio(self)
        self.cnt_importa_db = CntImportaDBDF(self)
        self.cnt_big_n = CntBigN(self)
        self.cnt_estadisticas = CntEstadisticas(self)
        self.dlg_describe = DlgDescribe(self)
        self.cnt_dispersion = CntDiagramaDispersion(self)
        self.cnt_distr_acum = CntDiagramaDistribucionAcumulada(self)
        self.cnt_cajas = CntDiagramaCajas(self)
        self.cnt_barra = CntBarraMasSolicitada(self)
        self.cnt_n_barras = CntNBarraMasSolicitadas(self)
        self.dlg_n_barras_mas_solicitadas = DlgNBarrasMasSolicitadas(self)

        # Eventos de las barras de estudio.
        self.barras_estudio.textChanged.connect(
            self.cnt_barras_estudio.barras_de_estudio)

        # Eventos para importar la base de datos.
        aleatorio = False
        if aleatorio:
            self.btn_importar.clicked.connect(self.cnt_importa_db._sqlite_df)
        else:
            self.btn_importar.clicked.connect(self.cnt_importa_db.sqlite_df)

        # - The Big Number.
        self.btn_importar.clicked.connect(self.cnt_big_n.calcula_big_n)

        # Eventos para mostrar información sobre estadísticas.
        self.btn_describe.clicked.connect(self.cnt_estadisticas.describe)
        self.btn_describe_1.clicked.connect(self.cnt_estadisticas.describe_1)
        self.btn_describe_2.clicked.connect(self.cnt_estadisticas.describe_2)
        self.btn_describe_3.clicked.connect(self.cnt_estadisticas.describe_3)

        # Eventos para mostrar los diagramas de dispersión.
        self.btn_dispersion.clicked.connect(self.cnt_dispersion.dispersion)
        self.btn_dispersion_1.clicked.connect(self.cnt_dispersion.dispersion_1)
        self.btn_dispersion_2.clicked.connect(self.cnt_dispersion.dispersion_2)
        self.btn_dispersion_3.clicked.connect(self.cnt_dispersion.dispersion_3)

        # Eventos para mostrar los diagramas de la ditribución acumulada y de
        # la densidad de probabilidad.
        self.btn_distr_acum_1.clicked.connect(
            self.cnt_distr_acum.distribucion_acumulada_1
        )
        self.btn_distr_acum_2.clicked.connect(
            self.cnt_distr_acum.distribucion_acumulada_2
        )
        self.btn_distr_acum_3.clicked.connect(
            self.cnt_distr_acum.distribucion_acumulada_3
        )

        # Eventos para mostrar los diagramas de cajas.
        self.btn_cajas.clicked.connect(self.cnt_cajas.cajas)

        # Eventos para la barra más solicitada.
        self.btn_barra_fem1.clicked.connect(self.cnt_barra.mas_solicitada_1)
        self.btn_barra_fem2.clicked.connect(self.cnt_barra.mas_solicitada_2)
        self.btn_barra_fem3.clicked.connect(self.cnt_barra.mas_solicitada_3)

        # Eventos para las n barras más solicitadas.
        self.btn_n_barras_fem1.clicked.connect(
            self.cnt_n_barras.n_mas_solicitadas_1
        )
        self.btn_n_barras_fem2.clicked.connect(
            self.cnt_n_barras.n_mas_solicitadas_2
        )
        self.btn_n_barras_fem3.clicked.connect(
            self.cnt_n_barras.n_mas_solicitadas_3
        )

        # Eventos para cerrar la aplicación.
        self.btn_cerrar.clicked.connect(self.cierra_aplicacion)

    # Salidas PyQt5.
    def status_bar(self, text):
        """Texto informativo en status bar."""

        self.statusbar.setFont(QFont('Consolas', 8))
        self.statusbar.showMessage(text)

    def salida_nombre_db(self, text):
        """Texto con el nombre de la base de datos importada."""

        self.lbl_nombre_db.setText(text)

    def salida_importar(self, text):
        """Texto con las dimensiones de la base de datos."""

        self.lbl_importar.setText(text)

    def salida_big_n(self):
        """The Big Number."""

        self.lbl_big_n.setStyleSheet(self.big_n_color)
        self.lbl_big_n1.setStyleSheet(self.big_n1_color)
        self.lbl_big_n2.setStyleSheet(self.big_n2_color)
        self.lbl_big_n3.setStyleSheet(self.big_n3_color)
        self.lbl_big_n.setText(str(self.big_n))
        self.lbl_big_n1.setText(str(self.big_n1))
        self.lbl_big_n2.setText(str(self.big_n2))
        self.lbl_big_n3.setText(str(self.big_n3))

        self.lbl_big_n_fem.setStyleSheet(self.big_n_fem_color)
        self.lbl_big_n_fem1.setStyleSheet(self.big_n_fem1_color)
        self.lbl_big_n_fem2.setStyleSheet(self.big_n_fem2_color)
        self.lbl_big_n_fem3.setStyleSheet(self.big_n_fem3_color)
        self.lbl_big_n_fem.setText(str(self.big_n_fem))
        self.lbl_big_n_fem1.setText(str(self.big_n_fem1))
        self.lbl_big_n_fem2.setText(str(self.big_n_fem2))
        self.lbl_big_n_fem3.setText(str(self.big_n_fem3))

        self.lbl_big_n_fem_max.setStyleSheet(self.big_n_fem_max_color)
        self.lbl_big_n_fem1_max.setStyleSheet(self.big_n_fem1_max_color)
        self.lbl_big_n_fem2_max.setStyleSheet(self.big_n_fem2_max_color)
        self.lbl_big_n_fem3_max.setStyleSheet(self.big_n_fem3_max_color)
        self.lbl_big_n_fem_max.setText(str(self.big_n_fem_max))
        self.lbl_big_n_fem1_max.setText(str(self.big_n_fem1_max))
        self.lbl_big_n_fem2_max.setText(str(self.big_n_fem2_max))
        self.lbl_big_n_fem3_max.setText(str(self.big_n_fem3_max))

        self.lbl_bign.setStyleSheet(self.bign_color)
        self.lbl_bign_1.setStyleSheet(self.bign_1_color)
        self.lbl_bign_2.setStyleSheet(self.bign_2_color)
        self.lbl_bign_3.setStyleSheet(self.bign_3_color)
        self.lbl_bign.setText(str(self.bign))
        self.lbl_bign_1.setText(str(self.bign_1))
        self.lbl_bign_2.setText(str(self.bign_2))
        self.lbl_bign_3.setText(str(self.bign_3))

        # self.label.setStyleSheet(self.big_n_color)
        # self.label.setFont(Qlabel('Consolas', 18))
        # self.label.setText(str(self.big_n))

    def call_dialogo_describe(self, df, caso, model):
        """Llama al diálogo Describe."""

        self.dlg_describe = DlgDescribe(
            parent=self, df=df, caso=caso, model=model
        )
        self.dlg_describe.show()

    # def call_dialogo_describe_1(self, df, caso, model):
    #     """Llama al diálogo Describe."""
    #
    #     self.dlg_describe = DlgDescribe(
    #         parent=self, df=df, caso=caso, model=model
    #     )
    #     self.dlg_describe.show()
    #
    # def call_dialogo_describe_2(self, df, caso, model):
    #     """Llama al diálogo Describe."""
    #
    #     self.dlg_describe = DlgDescribe(
    #         parent=self, df=df, caso=caso, model=model
    #     )
    #     self.dlg_describe.show()
    #
    # def call_dialogo_describe_3(self, df, caso, model):
    #     """Llama al diálogo Describe."""
    #
    #     self.dlg_describe = DlgDescribe(
    #         parent=self, df=df, caso=caso, model=model
    #     )
    #     self.dlg_describe.show()

    def call_dialogo_barra_mas_solicitada(self, caso, pd_obj):
        """Llama al diálogo BarraMasSolicitada."""

        self.dlg_barra_mas_solicitada = DlgBarraMasSolicitada(
            parent=self, caso=caso, pd_obj=pd_obj
        )
        self.dlg_barra_mas_solicitada.show()

    def call_dialogo_n_barras(self, df, caso, model):
        """Llama al diálogo NBarrasMasSolicitadas."""

        self.dlg_n_barras_mas_solicitadas = DlgNBarrasMasSolicitadas(
            parent=self, df=df, caso=caso, model=model
        )
        self.dlg_n_barras_mas_solicitadas.show()

    # Cerrar la aplicación.
    def cierra_aplicacion(self):
        """Cierra todas las ventanas de la aplicación."""

        try:
            self.dlg_describe.close()
            self.dlg_barra_mas_solicitada.close()
            self.dlg_n_barras_mas_solicitadas.close()
            self.plt.close('all')  # TODO cerrar todas las gráficas.

            self.close()
        except Exception as e:
            print(f'Oops! {e}')
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    qt_translator = QTranslator()
    qt_translator.load(
        'qtbase_' + QLocale.system().name(),
        QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    )
    app.installTranslator(qt_translator)

    # Qt modern
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    qtmodern.styles.dark(app)
    qtmodern.styles.dark(app)

    # Fuente.
    fuente = QFont()
    fuente.setFamily('Consolas')
    fuente.setPointSize(11)
    app.setFont(fuente)

    myapp = MainWindow()
    # mw = qtmodern.windows.ModernWindow(myapp)
    # mw.show()
    myapp.show()
    sys.exit(app.exec_())
