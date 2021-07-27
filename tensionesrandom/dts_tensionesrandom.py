# -*- coding: utf-8 -*-
"""
Tensiones aleatorias para pruebas

Created on Tue Apr 20 14:34:09 2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


import pandas as pd
import numpy as np
import random
from numpy.random import default_rng


class TensionesRandom:
    """
    Genera tensiones aleatorias para simular DataFrames de pandas con los
    valores extraidos de RSA.
    """
    
    def __init__(self, n_modelos=5, n_barras=100):
        """
        Inicializa en nº de modelos y el nº de barras de las tensiones
        aleatorias.

        :param n_modelos: int ; nº de modelos a generar.
        :param n_barras: int ; nº de barras por modelo
        """
        
        self.cols = (
            'Modelo', 'Barra', 'Seccion', 'Area', 'Material',
            'Caso', 'Nombre', 'Punto'
            'Smax', 'Smin', 'SmaxMy', 'SmaxMz', 'SminMy',
            'SminMz', 'Sx',
            'TY', 'TZ', 'T',
            'Mises', 'Limite', 'Ratio'
        )  # Columnas del DataFrame con los datos.

        self.rng = default_rng()  # https://numpy.org/doc/stable/reference/random/index.html

        self.n_modelos = n_modelos
        self.n_barras = n_barras

    def genera_modelos(self):
        """Genera una lista con modelos de cálculo."""

        num_modelos_max = self.n_modelos
        num_modelos = random.randint(0, num_modelos_max)
        modelos = ['mod_' + str(i) for i in range(num_modelos)]
        return modelos

    def genera_barras(self):
        """Genera barras."""

        num_barras_max = self.n_barras
        return [
            barra + 1 for barra in range(random.randint(0, num_barras_max))
        ]

    @staticmethod
    def genera_secciones():
        """Genera el nombre de las secciones."""

        return 'sección'

    @staticmethod
    def genera_areas(num_barras):
        """Genera las áreas de las barras"""

        areas = [random.randint(1, 1000) for _ in range(num_barras)]
        return areas

    @staticmethod
    def genera_materiales():
        """General el no,bre del material de la barras."""

        return 'material'

    @staticmethod
    def genera_casos():
        """Genera casos FEM."""

        return [1000,
                1100, 1101, 1102, 1103,
                1200, 1201, 1202, 1203,
                1300, 1301, 1302, 1303
                ]

    @staticmethod
    def genera_nombres():
        """Genera los nombres de los casos FEM."""

        return ['FEM I',
                'FEM IIa', 'FEM IIb', 'FEM IIc', 'FEM IId',
                'FEM IIIa', 'FEM IIIb', 'FEM IIIc', 'FEM IIId',
                'FEM IIIe', 'FEM IIIf', 'FEM IIIg', 'FEM IIIh'
                ]

    @staticmethod
    def genera_puntos(num_barras):
        """Genera puntos. Coincidirán con las barras."""

        # puntos = [punto for punto in range(num_barras)]
        # return puntos
        return ['origin', 'x=0,5', 'end']

    def genera_tensiones(self):
        """Genera una tensión positiva por caso FEM."""

        tensiones = []
        # num_casos = len(self.genera_casos())
        # for caso in range(num_casos):
        tension_1 = random.randint(1, 50)
        tension_2 = random.gauss(50, 50)
        tension = tension_1 + tension_2
        tensiones.append(abs(tension))
        return np.array(tensiones)

    def genera_sigma_max_My(self):
        """Genera sigma máxima My."""

        tensiones = self.genera_tensiones()
        a, b = 0.8, 1.2
        coeficientes = (b - a) * self.rng.random(len(tensiones)) + a
        return coeficientes * tensiones

    def genera_sigma_max_Mz(self):
        """Genera sigma máxima Mz."""

        tensiones = self.genera_tensiones()
        a, b = 0.0, 0.5
        coeficientes = (b - a) * self.rng.random(len(tensiones)) + a
        return coeficientes * tensiones

    def genera_sigma_x(self):
        """Genera sigma x."""

        tensiones = self.genera_tensiones()
        a, b = -0.2, 0.2
        coeficientes = (b - a) * self. rng.random(len(tensiones)) + a
        return coeficientes * np.array(tensiones)

    def genera_tau_y(self):
        """Genera tau y."""

        tensiones = self.genera_tensiones()
        a, b = -0.3, 0.3
        coeficientes = (b - a) * self.rng.random(len(tensiones)) + a
        return coeficientes * np.array(tensiones)

    def genera_tau_z(self):
        """Genera tau z."""

        tensiones = self.genera_tensiones()
        a, b = -0.5, 0.5
        coeficientes = (b - a) * self.rng.random(len(tensiones)) + a
        return coeficientes * np.array(tensiones)

    def genera_tau_x(self):
        """Genera tau y."""

        tensiones = self.genera_tensiones()
        a, b = -0.1, 0.1
        coeficientes = (b - a) * self.rng.random(len(tensiones)) + a
        return coeficientes * np.array(tensiones)

    def genera_mises(self, df):
        """Genera las tensiones de von Mises."""

        smax = df.Smax
        smin = df.Smin
        ty = df.Ty
        tz = df.Tz
        tx = df['T']
        svM1 = (smax**2 + 3 * (ty**2 + tz**2 + tx**2))**0.5
        svM2 = (smin**2 + 3 * (ty**2 + tz**2 + tx**2))**0.5
        df['Mises'] = svM1.where(svM1 > svM2, svM2)

    def genera_limite(self, df):
        """
        Genera las tensiones admisibles.
        Por simplificación se considera para
        FEM I   -> tensión admisible = 237 MPa
        FEM II  -> tensión admisible = 267 MPa
        FEM III -> tensión admisible = 295 MPa
        """

        df['Limite'] = np.where(df.Caso == 1000, 237., np.where(
            df.Caso < 1299, 267., 295.
        ))

    def genera_ratio(self, df):
        """Genera el ratio de las tensiones."""
        sigma_vonMises = df.Mises
        sigma_limite = df.Limite
        ratio = sigma_vonMises / sigma_limite * 100
        df['Ratio'] = ratio
    
    def dataframe_tensiones(self):
        """Data Frame con las tensiones aleatorias"""

        modelos = self.genera_modelos()
        barras = self.genera_barras()
        secciones = self.genera_secciones()
        areas = self.genera_areas(len(barras))
        materiales = self.genera_materiales()
        casos = self.genera_casos()
        nombres = self.genera_nombres()
        puntos = self.genera_puntos(len(barras))

        modelos_df = []
        barras_df = []
        secciones_df = []
        areas_df = []
        casos_df = []
        nombres_df = []
        puntos_df = []
        s_max_My_df = []
        s_min_My_df = []
        s_max_Mz_df = []
        s_min_Mz_df = []
        s_Fx_df = []
        t_y_df = []
        t_z_df = []
        t_x_df = []

        for modelo in modelos:
            for barra, area in zip(barras, areas):
                for punto in puntos:
                    for caso, nombre in zip(casos, nombres):


                        s_max_My = self.genera_sigma_max_My()
                        s_max_Mz = self.genera_sigma_max_Mz()
                        s_Fx = self.genera_sigma_x()
                        s_Ty = self.genera_tau_y()
                        s_Tz = self.genera_tau_z()
                        s_Tx = self.genera_tau_x()

                        for sMy, sMz, sFx, ty, tz, tx in zip(
                                s_max_My, s_max_Mz, s_Fx, s_Ty, s_Tz, s_Tx
                        ):

                            modelos_df.append(modelo)

                            barras_df.append(barra)
                            secciones_df.append(secciones)
                            areas_df.append(area)

                            casos_df.append(caso)
                            nombres_df.append(nombre)

                            puntos_df.append(punto)

                            s_max_My_df.append(sMy)
                            s_min_My_df.append(-sMy)
                            s_max_Mz_df.append(sMz)
                            s_min_Mz_df.append(-sMz)
                            s_Fx_df.append(sFx)
                            t_y_df.append(ty)
                            t_z_df.append(tz)
                            t_x_df.append(tx)

        print(barras_df)

        df = pd.DataFrame({
            'Modelo': modelos_df,
            'Barra': barras_df,
            'Seccion': secciones_df,
            'Area': areas_df,
            'Material': materiales,
            'Caso': casos_df,
            'Nombre': nombres_df,
            'Punto': puntos_df,
            'SmaxMy': s_max_My_df,
            'SminMy': s_min_My_df,
            'SmaxMz': s_max_Mz_df,
            'SminMz': s_min_Mz_df,
            'Sx': s_Fx_df,
            'Ty': t_y_df,
            'Tz': t_z_df,
            'T': t_x_df
        })

        df['Smax'] = df.SmaxMy + df.SmaxMz + df.Sx
        df['Smin'] = df.SminMy + df.SminMz + df.Sx
        self.genera_mises(df)
        self.genera_limite(df)
        self.genera_ratio(df)

        cols = [
            'Modelo', 'Barra', 'Seccion', 'Area', 'Material', 'Caso', 'Nombre',
            'Punto', 'Smax', 'Smin', 'SmaxMy', 'SmaxMz', 'SminMy', 'SminMz',
            'Sx', 'Ty', 'Tz', 'T', 'Mises', 'Limite', 'Ratio'
        ]

        df = df[cols]

        return df


if __name__ == '__main__':

    tensiones_random = TensionesRandom()
    # modelos = tensiones_random.genera_modelos()
    # barras = tensiones_random.genera_barras()
    # secciones = tensiones_random.genera_secciones()
    # areas = tensiones_random.genera_areas(len(barras))
    # materiales = tensiones_random.genera_materiales()
    # casos = tensiones_random.genera_casos()
    # nombres = tensiones_random.genera_nombres()
    # puntos = tensiones_random.genera_puntos(len(barras))
    # tensiones = tensiones_random.genera_tensiones()
    # sigma_max_My = tensiones_random.genera_sigma_max_My()
    # sigma_max_Mz = tensiones_random.genera_sigma_max_Mz()
    # sigma_x = tensiones_random.genera_sigma_x()
    df = tensiones_random.dataframe_tensiones()

    # print('modelos', modelos)
    # print(len(modelos))
    # print('barras', barras)
    # print(len(barras))
    # print('secciones', secciones)
    # print('áreas', areas)
    # print(len(areas))
    # print('materiales', materiales)
    # print('puntos', puntos)
    # print(len(puntos))
    # print('casos', casos)
    # print(len(casos))
    # print('nombres',  nombres)
    # print('tensiones', tensiones)
    # print(len(tensiones))
    # print('SmaxMy', sigma_max_My)
    # print('SmaxMz', sigma_max_Mz)
    # print('Sx', sigma_x)
    print()
    cols = [
        'Caso', 'Barra', 'Punto',
        'SmaxMy', 'SmaxMz', 'SminMy', 'SminMz',
        'Sx'
    ]

    print(df[cols])
    print(df.describe())

