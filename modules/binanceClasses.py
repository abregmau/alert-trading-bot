# General Libraries
import logging
import pickle
from modules import binanceFunctions

class signal:
    def __init__(self, signalData, infoBinance):
        self.signalData = signalData
        self.status = "new signal" # Possible status: "new signal","pending", ""
        self.precision = binanceFunctions.getPrecision(signalData['currency'],infoBinance)
        self.order = ""
    
    def print(self):
        print(self.signalData)

    def checkSignal(self, clientBinance):
        symbol = self.signalData['currency']
        entryPrice1 = self.signalData['entryPrice1']
        if self.signalData['typeSignal'] == 'long':
            side = 'BUY'
        elif self.signalData['typeSignal'] == 'short':
            side = 'SELL'

        quantity = float(round(10000.0 / entryPrice1 , self.precision))

        if self.status == "new signal":
            clientBinance.futures_change_leverage(symbol=symbol, leverage=20)
            self.order = clientBinance.futures_create_order(symbol=symbol, type='LIMIT', timeInForce='GTC', price=entryPrice1, side=side, quantity=quantity)
            self.status = "pending"

        if self.status == "pending":
            print(clientBinance.futures_get_order(symbol=symbol, orderId = self.order['orderId']))
            
class listSignals:
    def __init__(self):
        self.list = []

    def appendSignal(self, signal):
        self.list.append(signal)

    def printSignals(self):
        for signal in self.list:
            signal.print()

    def saveSignalsToFile(self, filePickle):
        with open(filePickle, 'wb') as file:
            pickle.dump(self, file)
            logging.debug("File 'data.pkl' with signals saved successfully")

    def checkListStatus(self, clientBinance):
        for signal in self.list:
                signal.checkSignal(clientBinance)