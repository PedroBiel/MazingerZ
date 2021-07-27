"""

MAZINGER Z
Modelo para el cálculo del Big N.

Created on 31/05/2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


class DataFrame:
    """Pandas DataFrame con los datos para el cálculo del Big N."""

    def __init__(self, df):
        """
        Sea df un DataFrame de pandas con los datos para el cálculo del Big N,
        obtiene los valores de las columnas.

        :param df: pandas DataFrame ; Datos para el cálculo del Big N.
        """

        self.df = df

    def get_df(self):
        """Getter del DataFrame."""

        return self.df.copy()

    def get_area(self):
        """Getter del área."""

        return self.df['Area'].copy()

    def get_ratio(self):
        """Getter del ratio."""

        return self.df['Ratio'].copy()


class Formulae(DataFrame):
    """Fórmula para el cálculo del Big N."""

    def __init__(self, df):
        """
        Sea df un DataFrame de pandas con los datos para el cálculo del Big N,
        obtiene Big N.

        :param df: pandas DataFrame ; Datos para el cálculo del Big N.
        """

        DataFrame.__init__(self, df)

        self.area = self.get_area()
        self.ratio = self.get_ratio()

    def big_number(self):
        """The Big Number."""

        _df = self.get_df()
        _df['ratio_area'] = self.ratio * self.area
        big_n = _df['ratio_area'].sum() / _df['Area'].sum()

        # try:
        #     _df['ratio_area'] = self.ratio * self.area
        #     big_n = _df['ratio_area'].sum() / _df['Area'].sum()
        # except Exception as e:
        #     print(f'Exception: {e}')
        #     big_n = 0.

        return round(big_n, 2)

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

    formulae = Formulae(df)
    big_n = formulae.big_number()
    print(big_n)

    print('---')

    import pandas as pd

    df1 = pd.DataFrame({
        'Area': [10, 20, 30],
        'Ratio': [3, 4, 5]
    })

    formulae = Formulae(df1)
    big_n = formulae.big_number()
    print(big_n)
