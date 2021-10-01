"""

MAZINGER Z
Controlador de la importación de la base de datos.

Created on 28/05/2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""

from importadb.constantes_importadb import Constantes
from importadb.dts_columnacaso import ColCaso
from importadb.dts_dataframeastype import DFAstype

from pyqt5_clases.qfiledialog import FileDialog
from tensionesrandom.dts_tensionesrandom import TensionesRandom
from transferenciadatos.sqlitepandasdf import SQLitePandasDF


class CntImportaDBDF:
    """
    Importa la base de datos con los valores de las tensiones según
    FEM 2131/2132 y los pasa a un pandas DataFrame.
    """

    def __init__(self, ventana):
        """Inicializa la ventana de MainWindow."""

        self.v = ventana

    def _sqlite_df(self):
        """Base de datos aleatoria para pruebas."""

        # Status bar.
        text = 'Abriendo base de datos aleatoria.'
        self.v.status_bar(text)

        # Label Importar.
        texto = '_'
        self.v.salida_importar(texto)

        try:
            self.getter_dataframe_db_provisional()
            print(self.v.df_db)
        except Exception as e:
            print(f'Oops, {e}')

        # Label Nombre DB.
        texto = 'Base de datos: aleatoria'
        self.v.salida_nombre_db(texto)

        # Label Importar.
        filas = self.v.df_db.shape[0]
        columnas = self.v.df_db.shape[1]
        texto = 'filas * cols: ' + str(filas) + ' * ' + str(columnas)
        self.v.salida_importar(texto)

        # Statusbar.
        text = 'Base de datos aleatoria importada.'
        self.v.status_bar(text)

    def getter_dataframe_db_provisional(self):
        """Getter del DataFrame con datos aleatorios para pruebas."""

        tensiones_random = TensionesRandom()
        df_db_temp = tensiones_random.dataframe_tensiones()
        if self.v.barras:  # Filtra las barras de estudio.
            self.v.df_db = df_db_temp[df_db_temp['Barra'].isin(self.v.barras)]
        else:  # La lista de barras de estudio está vacía.
            self.v.df_db = df_db_temp

    def sqlite_df(self):
        """DataFrame con los datos de la base de datos SQLite."""

        # Status bar.
        text = 'Abriendo base de datos.'
        self.v.status_bar(text)

        # Label Importar.
        texto = '_'
        self.v.salida_importar(texto)

        sqlite3 = self.get_sqlite3()
        ruta_db = self.ruta_db()

        if ruta_db != '':
            try:
                sql_df = SQLitePandasDF(ruta_db, 'Tensiones')
                df_db = sql_df.sql_to_df()
                print('\ndf_db 1')
                print(df_db.Caso.head(10))

                col_caso = ColCaso(df_db)
                df_db = col_caso.col_split()
                print('\ndf_db 2')
                print(df_db.Caso.head(10))

                df_astype = DFAstype(df_db)
                df_db = df_astype.replace_astype()

                if self.v.barras:  # Filtra las barras de estudio.
                    self.set_dataframe(
                        df_db[df_db['Barra'].isin(self.v.barras)]
                    )
                else:  # La lista de barras de estudio está vacía.
                    self.set_dataframe(df_db)

                print('\nsqlite_df.df_db')
                print(self.v.df_db)

            except sqlite3.Error as e:
                print('Error: {}'.format(e))
                self.v.message_box_db()

            text = 'Base de datos importada.'
        else:
            text = 'No se ha importado ninguna base de datos.'

        # Label Nombre DB.
        texto = 'Base de datos: ' + self.v.nombre_db
        self.v.salida_nombre_db(texto)

        # Label Importar.
        filas = self.v.df_db.shape[0]
        columnas = self.v.df_db.shape[1]
        texto =  'filas * cols: ' + str(filas) + ' * ' + str(columnas)
        self.v.salida_importar(texto)

        # Status bar.
        self.v.status_bar(text)

    def set_dataframe(self, df):
        """Setter del DataFrame."""

        self.v.df_db = df.copy()

    def get_sqlite3(self):
        """Getter de la librería sqlite3."""

        return self.v.sqlite3

    def ruta_db(self):
        """Ruta y nombre de la base de datos."""

        constantes = Constantes()
        subtitulo = constantes.get_abrir_datos()
        tipo_fichero = constantes.get_tipo_ficheros()
        pfad = FileDialog(subtitulo, '', tipo_fichero)
        ruta_nombre_db = pfad.get_open_file_name()

        posicion = ruta_nombre_db.rfind('/')
        self.v.nombre_db = ruta_nombre_db[posicion + 1:]

        return ruta_nombre_db
