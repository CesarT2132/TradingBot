class Bot:
    def __init__(self, position=None, balance=1000, holdings=0):
        """
        Inicializa el bot con una posición de trading, balance y cantidad de activos.

        :param position: La posición actual del bot, puede ser 'long', 'short' o None.
        :param balance: El balance simulado en dólares u otra moneda base.
        :param holdings: La cantidad de criptomoneda que posee.
        """
        self.position = position  # 'long', 'short' o None
        self.balance = balance  # Balance en moneda base (USD)
        self.holdings = holdings  # Cantidad de criptomoneda que posee

    def decide_action(self, df):
        """
        Decide qué acción tomar según las Bandas de Bollinger.

        :param df: DataFrame con los datos de precios y las Bandas de Bollinger.
        :return: La acción a tomar ('BUY', 'SELL', 'HOLD').
        """
        latest = df.iloc[-1]  # Tomamos el último valor del DataFrame
        price = latest['close']  # Último precio de cierre
        upper_band = latest['Upper_Band']  # Banda superior
        lower_band = latest['Lower_Band']  # Banda inferior

        # Si el precio está por encima de la Banda Superior, vende
        if price > upper_band:
            return 'SELL'
        # Si el precio está por debajo de la Banda Inferior, compra
        elif price < lower_band:
            return 'BUY'
        # Si el precio está dentro de las Bandas de Bollinger, mantiene la posición
        else:
            return 'HOLD'

    def execute_trade(self, action, price):
        """
        Ejecuta la acción de trading y ajusta el balance y las tenencias.

        :param action: La acción que se debe ejecutar ('BUY', 'SELL', 'HOLD').
        :param price: El precio actual de la criptomoneda.
        """
        if action == 'BUY':
            if self.position != 'long' and self.balance > 0:
                # Compra todo el balance disponible
                self.holdings += self.balance / price
                self.balance = 0
                self.position = 'long'
                print(f"Compra ejecutada. Nuevas tenencias: {self.holdings:.4f} BTC.")
            else:
                print("No se puede comprar: ya en posición de COMPRA o sin balance disponible.")
        elif action == 'SELL':
            if self.position != 'short' and self.holdings > 0:
                # Vende todas las tenencias
                self.balance += self.holdings * price
                self.holdings = 0
                self.position = 'short'
                print(f"Venta ejecutada. Nuevo balance: ${self.balance:.2f}.")
            else:
                print("No se puede vender: ya en posición de VENTA o sin tenencias.")
        elif action == 'HOLD':
            print("Manteniendo la posición actual.")
        else:
            print("Acción inválida. No se ejecutó ninguna operación.")
