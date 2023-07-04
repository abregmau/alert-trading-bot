# General Libraries

def readMessage(message):
    textMessage = message.message
    messageId = message.id
    messageDate = message.date

    if textMessage != None:
        if "COIN DETECTED" in textMessage:
            start = textMessage.find("#") + 1
            end = textMessage[start:].find("\n") + start
            currency = textMessage[start:end]

            start = textMessage.find("Entry Range:") + len("Entry Range:")
            end = textMessage[start:].find("-") + start
            entryPrice1 = float(textMessage[start:end].strip())

            start = end + 1
            end = textMessage[start:].find("\n") + start
            entryPrice2 = float(textMessage[start:end].strip())

            start = textMessage.find("Target 1:") + len("Target 1:")
            end = textMessage[start:].find("\n") + start
            target1 = float(textMessage[start:end].strip())

            start = textMessage[end:].find("Target 2:") + len("Target 2:") + end
            end = textMessage[start:].find("\n") + start
            target2 = float(textMessage[start:end].strip())

            start = textMessage[end:].find("Target 3:") + len("Target 3:") + end
            end = textMessage[start:].find("\n") + start
            target3 = float(textMessage[start:end].strip())

            start = textMessage[end:].find("Target 4:") + len("Target 4:") + end
            end = textMessage[start:].find("\n") + start
            target4 = float(textMessage[start:end].strip())

            start = textMessage[end:].find("Target 5:") + len("Target 5:") + end
            end = textMessage[start:].find("\n") + start
            target5 = float(textMessage[start:end].strip())

            start = textMessage[end:].find("Target 6:") + len("Target 6:") + end
            end = textMessage[start:].find("\n") + start
            target6 = float(textMessage[start:end].strip())

            start = textMessage[end:].find("Target 7:") + len("Target 7:") + end
            end = textMessage[start:].find("\n") + start
            target7 = float(textMessage[start:end].strip())

            start = textMessage[end:].find("Target 8:") + len("Target 8:") + end
            end = textMessage[start:].find("\n") + start
            target8 = float(textMessage[start:end].replace("Long Term", "").strip())

            start = textMessage[end:].find("Target 9:") + len("Target 9:") + end
            end = textMessage[start:].find("\n") + start
            target9 = float(textMessage[start:end].replace("Long Term", "").strip())

            start = textMessage.find("Stop-Loss:") + len("Stop-Loss :")
            end = textMessage[start:].find("\n") + start
            stopLoss = float(textMessage[start:end].replace("*", "").strip())

            if "UP | LONG" in textMessage:
                typeSignal = "long"
            elif "DOWN | SHORT" in textMessage:
                typeSignal = "short"

            # Translate currency pairs

            currency = currency.replace("/","")

            dictMessage = {
                    "messageId": messageId,
                    "messageDate": messageDate,
                    "currency": currency,
                    "typeSignal": typeSignal,
                    "entryPrice1": entryPrice1,
                    "entryPrice2": entryPrice2,
                    "target1": target1,
                    "target2": target2,
                    "target3": target3,
                    "target4": target4,
                    "target5": target5,
                    "target6": target6,
                    "target7": target7,
                    "target8": target8,
                    "target9": target9,
                    "stopLoss": stopLoss,
                }
            
            return dictMessage
        
def validateSignal(element):
    
    if(element) == None:
        return False
    
    messageId = element["messageId"]
    messageDate = element["messageDate"]
    currency = element["currency"]
    typeSignal = element["typeSignal"]
    entryPrice1 = element["entryPrice1"]
    entryPrice2 = element["entryPrice2"]
    target1 = element["target1"]
    target2 = element["target2"]
    target3 = element["target3"]
    target4 = element["target4"]
    target5 = element["target5"]
    target6 = element["target6"]
    target7 = element["target7"]
    target8 = element["target8"]
    target9 = element["target9"]
    stopLoss = element["stopLoss"]

    if typeSignal == "long":
        if (
            not (entryPrice1 > entryPrice2)
            or not (target1 < target2 < target3 < target4 < target5 < target6 < target7 < target8 < target9)
            or not (stopLoss < entryPrice2)
        ):
            return False

    if typeSignal == "short":
        if (
            not (entryPrice1 < entryPrice2)
            or not (target1 > target2 > target3 > target4 > target5 > target6 > target7 > target8 > target9)
            or not (stopLoss > entryPrice2)
        ):
            return False

    return True