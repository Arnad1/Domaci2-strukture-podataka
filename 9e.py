#Dat je stek S u kojem se čuvaju podaci tipa string. Na žalost, neki od elemenata steka su bombe (označene sa *). Napišite funkciju makni_bombe (S) koja će iz steka S ukloniti sve bombe, a ostale
#elemente poređati u ”naopakom” poretku. Na primjer, ako su elementi u S redom od vrha prema dnu steka (*, D, *, C, B, A), onda nakon poziva funkcije stek treba izgledati ovako: (A, B, C, D).

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0 

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self): 
        return self.items
            
    def makni_bombe(self):
        items2 = Stack()
        while not self.is_empty():
            if self.peek() == "*":
                self.pop()
            else:
                items2.push(self.peek())
                self.pop()
        return items2.get_stack()
            

s = Stack()
s.push("A")
s.push("B")
s.push("C")
s.push("*")
s.push("D")
s.push("*")

print(s.makni_bombe())
