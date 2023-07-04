# General Libraries
import logging

class signal:
    def __init__(self, signalData):
        self.signalData = signalData
        self.status = "new signal"
        # Possible status: "new signal","pending", 
    
    def print(self):
        print(self.signalData)

    def checkSignal(self, clientBinance):
        if self.status == "new signal":
            clientBinance.futures_change_leverage(symbol=self.signalData['currency'], leverage=20)
            response = clientBinance.futures_create_order(symbol=self.signalData['currency'],type='LIMIT',timeInForce='GTC',price=5.0,side='BUY',quantity=1)
            print(response)
            self.status = "pending"
            
class listSignals:
    def __init__(self):
        self.list = []

    def appendSignal(self, signal):
        self.list.append(signal)

    def printSignals(self):
        for signal in self.list:
            signal.print()

    def checkListStatus(self, clientBinance):
        for signal in self.list:
                signal.checkSignal(clientBinance)