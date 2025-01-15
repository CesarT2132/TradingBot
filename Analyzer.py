import pandas as pd
import numpy as np


class Analyzer:
    def __init__(self, data):
        """
        Inicializa la clase con el DataFrame de datos de precios.
        :param data: DataFrame que contiene los datos de precios (por ejemplo, 'close')
        """
        self.data = data

    def calculate_bollinger_bands(self, window=20, std_dev=2):
        """
        Calcula las Bandas de Bollinger (superior e inferior) y la media móvil (MA).

        :param window: El número de periodos para la media móvil (por defecto 20).
        :param std_dev: El número de desviaciones estándar para las bandas (por defecto 2).
        :return: DataFrame con las columnas 'MA', 'Upper_Band' y 'Lower_Band'
        """
        # Calculando la media móvil simple
        self.data['MA'] = self.data['close'].rolling(window=window).mean()

        # Calculando la desviación estándar
        self.data['Std_Dev'] = self.data['close'].rolling(window=window).std()

        # Calculando las Bandas de Bollinger
        self.data['Upper_Band'] = self.data['MA'] + \
            (self.data['Std_Dev'] * std_dev)
        self.data['Lower_Band'] = self.data['MA'] - \
            (self.data['Std_Dev'] * std_dev)

        return self.data

    def get_trading_signal(self):
        """
        Genera señales de trading basadas en las Bandas de Bollinger:
        - 'BUY' si el precio de cierre está por debajo de la Banda Inferior.
        - 'SELL' si el precio de cierre está por encima de la Banda Superior.
        - 'HOLD' si el precio de cierre está dentro de las bandas.

        :return: String con la señal de trading ('BUY', 'SELL' o 'HOLD')
        """
        latest = self.data.iloc[-1]  # Última fila de datos

        if latest['close'] > latest['Upper_Band']:
            return "SELL"
        elif latest['close'] < latest['Lower_Band']:
            return "BUY"
        return "HOLD"
