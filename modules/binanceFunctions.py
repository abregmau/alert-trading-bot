import logging
import pickle
from modules import binanceClasses

def getPrecision(requestedFutures, infoBinance):
    
    # Iterar sobre los símbolos de los contratos de futuros en la información obtenida
    for symbol_info in infoBinance['symbols']:
        symbol = symbol_info['symbol']
    
        # Verificar si el símbolo está en la lista de futuros solicitados
        if symbol in requestedFutures:
            quantity_precision = symbol_info['quantityPrecision']

    return quantity_precision

def readSignalsFromFile(filePickle):
    try:
        with open(filePickle, 'rb') as file:
            signals = pickle.load(file)
            logging.warning("File 'data.pkl' with signals read successfully")
            print(signals.list[0].signalData)
    except FileNotFoundError:
        logging.warning("File 'data.pkl' with signals not found, creating empty object")
        signals = binanceClasses.listSignals()

    return signals