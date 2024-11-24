{"filter":false,"title":"caesar-cipher.py","tooltip":"/caesar-cipher.py","undoManager":{"mark":16,"position":16,"stack":[[{"start":{"row":0,"column":0},"end":{"row":2,"column":25},"action":"insert","lines":["def getDoubleAlphabet(alphabet):","    doubleAlphabet = alphabet + alphabet","    return doubleAlphabet"],"id":1}],[{"start":{"row":2,"column":25},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":3,"column":0},"end":{"row":3,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":4},"action":"remove","lines":["    "],"id":3}],[{"start":{"row":3,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["def getMessage():","    stringToEncrypt = input(\"Please enter a message to encrypt: \")","    return stringToEncrypt",""],"id":4}],[{"start":{"row":6,"column":0},"end":{"row":8,"column":22},"action":"insert","lines":["def getCipherKey():","    shiftAmount = input( \"Please enter a key (whole number from 1-25): \")","    return shiftAmount"],"id":5}],[{"start":{"row":8,"column":22},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":6},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"remove","lines":["    "],"id":7}],[{"start":{"row":9,"column":0},"end":{"row":20,"column":27},"action":"insert","lines":["def encryptMessage(message, cipherKey, alphabet):","    encryptedMessage = \"\"","    uppercaseMessage = \"\"","    uppercaseMessage = message.upper()","    for currentCharacter in uppercaseMessage:","        position = alphabet.find(currentCharacter)","        newPosition = position + int(cipherKey)","        if currentCharacter in alphabet:","            encryptedMessage = encryptedMessage + alphabet[newPosition]","        else:","            encryptedMessage = encryptedMessage + currentCharacter","    return encryptedMessage"],"id":8}],[{"start":{"row":20,"column":27},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":9},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "]},{"start":{"row":21,"column":4},"end":{"row":22,"column":0},"action":"insert","lines":["",""]},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"remove","lines":["    "],"id":10},{"start":{"row":21,"column":4},"end":{"row":22,"column":0},"action":"remove","lines":["",""]},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":21,"column":0},"end":{"row":23,"column":56},"action":"insert","lines":["def decryptMessage(message, cipherKey, alphabet):","    decryptKey = -1 * int(cipherKey)","    return encryptMessage(message, decryptKey, alphabet)"],"id":11}],[{"start":{"row":23,"column":56},"end":{"row":24,"column":0},"action":"insert","lines":["",""],"id":12},{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"remove","lines":["    "],"id":13}],[{"start":{"row":24,"column":0},"end":{"row":36,"column":52},"action":"insert","lines":["def runCaesarCipherProgram():","    myAlphabet=\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"","    print(f'Alphabet: {myAlphabet}')","    myAlphabet2 = getDoubleAlphabet(myAlphabet)","    print(f'Alphabet2: {myAlphabet2}')","    myMessage = getMessage()","    print(myMessage)","    myCipherKey = getCipherKey()","    print(myCipherKey)","    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)","    print(f'Encrypted Message: {myEncryptedMessage}')","    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)","    print(f'Decypted Message: {myDecryptedMessage}')"],"id":14}],[{"start":{"row":36,"column":52},"end":{"row":37,"column":0},"action":"insert","lines":["",""],"id":15},{"start":{"row":37,"column":0},"end":{"row":37,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":37,"column":4},"end":{"row":37,"column":28},"action":"insert","lines":["runCaesarCipherProgram()"],"id":16}],[{"start":{"row":37,"column":0},"end":{"row":37,"column":4},"action":"remove","lines":["    "],"id":17}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":37,"column":0},"end":{"row":37,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":20,"state":"start","mode":"ace/mode/python"}},"timestamp":1729373666814,"hash":"4e3d57817759b09fc4d409c8c706f25b0f0caf26"}