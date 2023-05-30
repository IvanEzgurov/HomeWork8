from logic import *
from Interf import *

nameFile = "phoneNumber.txt"

inputNumber = -1
while(inputNumber != 6):
    checFile(nameFile)
    inputNumber = interface()
    try:
        inputNumber = int(inputNumber)
        if not(0 < inputNumber < 7):
            raise IOError("Не в диапазоне")
        
        if inputNumber == 1:
            printPhoneBook(nameFile)
        elif inputNumber == 2:
            addContact(nameFile)
        elif inputNumber == 3:
            searchPeople(nameFile)
        elif inputNumber == 4:
            delPeople(nameFile)
        elif inputNumber == 5:
            changePeople(nameFile)
    except Exception:
        print('\n Ввод не корректный \n')