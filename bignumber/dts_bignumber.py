"""

MAZINGER Z
Datos para el cálculo del Big N.

Created on 31/05/2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


class DataFrame:
    """Pandas DataFrame con los datos para el cálculo del Big N."""

    def __init__(self):
        """
        Sea df un DataFrame de pandas con los datos para el cálculo del Big N,
        obtiene los valores de las columnas.
        """

    def get_df(self, df):
        """
        Getter del DataFrame.
        :param df: pandas DataFrame ; Datos para el cálculo del Big N.
        """

        return df.copy()

    def get_area(self, df):
        """
        Getter del área.
        :param df: pandas DataFrame ; Datos para el cálculo del Big N.
        """

        return df['Area'].copy()

    def get_ratio(self, df):
        """
        Getter del ratio.
        :param df: pandas DataFrame ; Datos para el cálculo del Big N.
        """

        return df['Ratio'].copy()


class BigN(DataFrame):
    """Fórmula para el cálculo del Big N."""

    def __init__(self):
        """
        Sea df un DataFrame de pandas con los datos para el cálculo del Big N,
        obtiene Big N.

        :param df: pandas DataFrame ; Datos para el cálculo del Big N.
        """

        DataFrame.__init__(self)

    def big_number(self, df):
        """
        The Big Number.
        :param df: pandas DataFrame ; Datos para el cálculo del Big N.
        """

        _df = self.get_df(df)

        # Para cada grupo  ['Caso', 'Barra', 'Punto'] busca la fila con el
        # valor máximo de 'Ratio'.
        idx = df.groupby([
            'Caso', 'Barra', 'Punto'])[
            'Ratio'].transform(max) == df['Ratio']
        __df = df[idx].copy()
        __df['ratio_area'] = __df.Ratio * __df.Area
        big_n = __df['ratio_area'].sum() / __df['Area'].sum()

        return round(big_n, 1)

    def big_number_fem(self, df):
        """
        The big number de los máximos de cada barra.
        :param df: pandas DataFrame ; Datos para el cálculo del Big N.
        """

        _df = self.get_df(df)

        # Para cada grupo  ['Caso', 'Barra'] busca la fila con el valor
        # máximos de 'Ratio'.
        idx = df.groupby(['Caso', 'Barra'])['Ratio'].transform(max) == df[
            'Ratio']
        __df = df[idx].copy()
        __df['ratio_area'] = __df.Ratio * __df.Area
        big_n = __df['ratio_area'].sum() / __df['Area'].sum()

        return round(big_n, 1)

    def big_number_fem_max(self, df):
        """"
        The big number de los ratios máximos.
        :param df: pandas DataFrame ; Datos para el cálculo del Big N.
        """

        ratio_max = df['Ratio'].max()

        return round(ratio_max, 1)

    def big_n(self, df):
        """
        The Big Number.
        :param df: pandas DataFrame ; Datos para el cálculo del Big N.
        """

        area = self.get_area(df)
        ratio = self.get_ratio(df)
        _df = self.get_df(df)

        _df['ratio_area'] = ratio * area
        big_n = _df['ratio_area'].sum() / _df['Area'].sum()

        return round(big_n, 1)

    def big_number_color(self, b_n):
        """
        Color del Big Number.
        b_n : float ; Big Number
        """

        # ratio_max = self.get_ratio().max()

        if b_n < 40:
            clr = '#66ccff'  # azul
        elif b_n < 60:
            clr = '#66ff66'  # verde
        elif b_n < 80:
            clr = 'yellow'
        elif b_n < 100:
            clr = 'orange'
        else:
            clr = 'red'

        etiqueta = f'color: {clr}'

        return etiqueta


if __name__ == '__main__':

    from tensionesrandom.dts_tensionesrandom import TensionesRandom

    tensiones_random = TensionesRandom()
    df = tensiones_random.dataframe_tensiones()
    print(df)

    bn = BigN()
    big_n = bn.big_number(df)
    big_n_fem = bn.big_number_fem(df)
    big_n_fem_max = bn.big_number_fem_max(df)
    print(big_n, big_n_fem, big_n_fem_max)

    print('---')

    import pandas as pd

    df1 = pd.DataFrame({
        'Area': [10, 20, 30],
        'Ratio': [3, 4, 5]
    })

    formulae = BigN()
    big_n = formulae.big_number(df1)
    print(big_n)
