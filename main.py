from MainController import MainController


def display_menu():
    """
    Muestra un menú para seleccionar el tipo de criptomoneda.
    :return: La criptomoneda seleccionada por el usuario.
    """
    print("Selecciona la criptomoneda para operar:")
    cryptocurrencies = {
        "1": "BTCUSDT",
        "2": "ETHUSDT",
        "3": "BNBUSDT",
        "4": "SOLUSDT",
        "5": "ADAUSDT",
        "6": "XRPUSDT",
        "7": "DOTUSDT",
        "8": "DOGEUSDT",
        "9": "MATICUSDT",
        "10": "LTCUSDT"
    }

    for key, value in cryptocurrencies.items():
        print(f"{key}: {value}")

    choice = input("Ingresa el número de la criptomoneda: ")
    while choice not in cryptocurrencies:
        print("Selección no válida. Intenta nuevamente.")
        choice = input("Ingresa el número de la criptomoneda: ")

    return cryptocurrencies[choice]


def main():
    # API key para Binance
    api_key = ""

    # Mostrar el menú y seleccionar la criptomoneda
    symbol = display_menu()

    # Inicialización del MainController con el símbolo seleccionado
    controller = MainController(api_key, symbol=symbol)

    # Inicia la ejecución continua del flujo
    controller.start(interval=3)



if __name__ == "__main__":
    main()