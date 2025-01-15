import pandas as pd
import requests
from datetime import datetime
from Analyzer import Analyzer
from logger import Logger
from Bot import Bot
from data_stream import DataStream
import time


class MainController:
    def __init__(self, api_key, symbol="BTCUSDT", interval="1m"):
        # Solicitar datos iniciales al usuario
        balance = float(input("Ingrese su balance inicial (USD): "))
        holdings = float(input("Ingrese la cantidad inicial de criptomonedas que posee: "))
        print(f"Inicializando con un balance de ${balance:.2f} y {holdings:.4f} BTC.")
        
        self.data_stream = DataStream(symbol, interval)
        self.bot = Bot(balance=balance, holdings=holdings)
        self.logger = Logger()


    def run(self):
        try:
            print(f"Obteniendo datos para {self.data_stream.symbol}...")

            # Obtener los datos del stream
            data = self.data_stream.get_data()

            # Inicializar Analyzer con los datos obtenidos
            self.analyzer = Analyzer(data)

            # Calcular las Bandas de Bollinger
            df_with_bands = self.analyzer.calculate_bollinger_bands()

            # Decidir la acción (comprar, vender o mantener)
            action = self.bot.decide_action(df_with_bands)

            # Obtener el precio actual para ejecutar la acción
            current_price = df_with_bands.iloc[-1]["close"]

            # Ejecutar la acción
            self.bot.execute_trade(action, current_price)

            # Registrar la decisión
            self.logger.log_decision(action, self.data_stream.symbol, current_price)

            print(f"Precio actual de {self.data_stream.symbol}: {current_price:.2f}")

        except Exception as e:
            print(f"Error: {e}")

    def start(self, interval=3):
        # Este método mantendrá la aplicación corriendo indefinidamente en intervalos definidos.
        while True:
            self.run()
            print(f"Esperando {interval} segundos antes de la siguiente operación...")
            time.sleep(interval)
