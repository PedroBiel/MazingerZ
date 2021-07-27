# -*- coding: utf-8 -*-
"""
Conecta con base de datos SQLite y transfiere los datos a un pandas DataFrame

Created on Tu Apr 28 16:45:40 2020

__author__ = Pedro Biel
__version__ = 1.0.0
__email__ = structural.eng.biel@gmail.com
"""


import pandas as pd
import sqlite3


class SQLitePandasDF:
    """
    Conecta con base de datos SQLite y transfiere los datos a un pandas
    DataFrame.
    La ruta y el nombre de la base de datos es un mismo parámetro.
    """

    def __init__(self, ruta_base_datos, tabla):
        self.ruta_base_datos = ruta_base_datos  # Ruta donde se encuentra la base de datos y nombre de la base de datos con extensión.
        self.tbl = tabla  # Tabla de la base de datos.

    def sql_to_df(self):
        conn = sqlite3.connect(self.ruta_base_datos)
        df_db = pd.read_sql('SELECT * FROM ' + self.tbl + ';', conn)
            
        return df_db


class SQLitePandasDF2:
    """
    Conecta con base de datos SQLite y transfiere los datos a un pandas
    DataFrame.
    La ruta y el nombre de la base de datos son dos parámetros diferentes.
    """

    def __init__(self, ruta, base_datos, tabla):
        self.ruta = ruta  # Ruta donde se encuentra la base de datos.
        self.base_datos = base_datos  # Nombre de la base de datos sin extensión.
        self.tbl = tabla  # Tabla de la base de datos.

    def sql_to_df(self):
        self.db = self.ruta + '/' + self.base_datos + '.db'
        conn = sqlite3.connect(self.db)
        df_db = pd.read_sql('SELECT * FROM ' + self.tbl + ';', conn)

        return df_db
