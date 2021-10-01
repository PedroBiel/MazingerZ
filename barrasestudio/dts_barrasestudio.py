# -*- coding: utf-8 -*-
"""
Barras de estudio

Created on 17/09/2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


import re


class BarrasEstudio:
    """Pasa el string de las barras de estudio a una lista."""

    def __init__(self, barras_estudio: str):
        """
        Inicializa las barras de estudio.

        :param barras_estudio : str; barras con las que hacer el estudio.
        """

        self.str_barras = barras_estudio  # String con las barras de estudio.

        self.barras = []  # Lista con los grupos del string.

    def str2list(self):
        """
        Pasa de string a list.
        Formato de la lista de barras según RSA.
        Los únicos carácteres contemplados son números de 0 a 9 y las letras A,
        CA, TO, BY.
        Ejemplos:
        "" -> todas las barras
        100A102 200A212CA3 -> barras 100, 101, 102, 200, 203, 206, 209, 2012
        100to102 200to212By3 -> barras 100, 101, 102, 200, 203, 206, 209, 2012
        """

        lista_barras = []

        # Letras en minúsculas.
        self.str_barras = self.str_barras.lower()

        # Si un caracter no es 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, o, t, y,
        # espacio, hay un error en el texto.
        x = re.findall('[^0-9catoby ]', self.str_barras)
        if len(x) > 0:  # hay un error.
            print(f'Hay un error en el texto: {x}')
        else:
            # De string a lista.
            split_barras = list(self.str_barras.split(' '))
            # Elimina ''.
            if '' in split_barras:
                split_barras = list(dict.fromkeys(split_barras))
                split_barras.remove('')

            # Convierte en lista de números.
            for l_barras in split_barras:
                res = re.findall('(\d+|[A-Za-z]+)', l_barras)
                try:
                    if (('a' in res) and ('ca' not in res)) or \
                        (('to' in res) and ('by' not in res)):
                        barras = [b for b in range(int(res[0]), int(res[-1]) + 1)]
                        lista_barras += barras
                    elif (('a' in res) and ('ca' in res)) or \
                        (('to' in res) and ('by' in res)):
                        barras = [b for b in range(int(res[0]), int(res[2]) + 1, int(res[-1]))]
                        lista_barras += barras
                    elif (('a' not in res) and ('ca' not in res)) or \
                        (('to' not in res) and ('by' not in res)):
                        barras = [int(l_barras)]
                        lista_barras += barras
                except Exception as e:
                    print(f'Oops! {e}')

        return sorted(lista_barras)


if __name__ == '__main__':

    s = '1a5 100a110ca5 130 10'
    barras_estudio = BarrasEstudio(s)
    print(barras_estudio.str2list())
    print()

    s = '1 5 10 20to25 100to110by5 130'
    barras_estudio = BarrasEstudio(s)
    print(barras_estudio.str2list())
    print()

    s = ' 416A458CA14 418A460CA14 420A462CA14  '
    barras_estudio = BarrasEstudio(s)
    print(barras_estudio.str2list())
    print()

    s = ' 1093 1094 1096A1099   10'
    barras_estudio = BarrasEstudio(s)
    print(barras_estudio.str2list())
    print()
