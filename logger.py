import logging


class Logger:
    def __init__(self, log_file='trading_log.txt'):
        """
        Inicializa la clase Logger y configura el archivo donde se guardarán los logs.

        :param log_file: El archivo donde se guardarán los registros de las decisiones.
        """
        self.log_file = log_file
        self._setup_logger()

    def _setup_logger(self):
        """
        Configura el logger con formato, nivel de log y archivo de salida.
        """
        self.logger = logging.getLogger('TradingLogger')
        self.logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler(self.log_file)
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def log_decision(self, action, symbol, price):
        """
        Registra una decisión de trading en el archivo de log.

        :param action: La acción tomada ('BUY', 'SELL', 'HOLD').
        :param symbol: El símbolo que se está operando (por ejemplo, 'BTCUSDT').
        :param price: El precio en el que se realizó la acción.
        """
        log_message = f"Action: {action} | Symbol: {symbol} | Price: {price}"
        self.logger.info(log_message)

    def display_logs(self):
        """
        Muestra todos los logs registrados en el archivo de log.
        """
        with open(self.log_file, 'r') as file:
            logs = file.readlines()
            for log in logs:
                print(log.strip())