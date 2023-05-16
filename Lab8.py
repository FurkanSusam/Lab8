from abc import ABC

class doc(ABC):
    address=None

    def __init__(self, address):
        self.address=address

    def calculateFreqs(self):
        pass

class ListCount(doc):

    def calculateFreqs(self):
        numA = 1
        cnt = 0
        orgList = list()
        Holder = list()
        holderAll = list()
        with open(self.address, 'r') as file:
            content = file.read()
            for char in content:
                if char.isalpha():
                    char = char.lower()
                    holderAll.append(char)
                    if char not in Holder:
                        Holder.append(char)
                        Holder.sort()
            for charr in Holder:
                for uniqueChar in holderAll:
                    if charr == uniqueChar:
                        cnt += 1
                if numA == 1:
                    orgList.append(f"List-> {charr}"+"  "+f"Resulting List -> {charr} = {cnt}")
                else:
                    orgList.append(f"       {charr}" + "  " + f"                  {charr} = {cnt}")
                numA = 0
                cnt = 0
        for items in orgList:
            print(items)

class DictCount(doc):

    def calculateFreqs(self):
        dHolder = dict()
        with open(self.address, 'r') as file:
            content = file.read()
            for ch in content:
                if ch.isalpha():
                    ch = ch.lower()
                    if ch in dHolder:
                        dHolder[ch] += 1
                    else:
                        dHolder[ch] = 1
        number = 1
        sorted_char = sorted(dHolder.keys())
        for sortedChar in sorted_char:
                if number == 1:
                    print(f"Dict -> {sortedChar}" + "  " + f"Updated Dist -> {sortedChar} = {dHolder[sortedChar]}")
                else:
                    print(f"        {sortedChar}" + "  " + f"                {sortedChar} = {dHolder[sortedChar]}")
                number = 0


adress = "weirdWords.txt"
list_counter = ListCount(adress)
dict_counter = DictCount(adress)
list_counter.calculateFreqs()
print("______________")
dict_counter.calculateFreqs()