class Node:
    def __init__(self, ime, prosjecna_zarada):
        self.ime = ime
        self.prosjecna_zarada = prosjecna_zarada
        self.right = None
        self.left = None
    
class BinaryTree:
    def __init__(self,root):
        self.root = root

#Napisati funkciju dodaj (Node) koja dodaje novog pjevača u binarno stablo na osnovu definisane strukture slaganja čvorova (po potrošnji).

    def dodaj(self,new_node): 
        if self.root is None:
            self.root = new_node
        else:
            self._dodaj(new_node,self.root) 

    def _dodaj(self, new_node, current_node):
        if new_node.prosjecna_zarada < current_node.prosjecna_zarada:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._dodaj(new_node, current_node.left)
        elif new_node.prosjecna_zarada > current_node.prosjecna_zarada:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._dodaj(new_node, current_node.right)
        else:
            print("The value is already in a tree")

#Napisati funkciju trazi (root: Node, max_zarada: Float) koja treba da vrati imena pjevača koji su zaradili manje od vrijednosti max_zarada

    def trazi (self, current_node, lista):
        if current_node is not None:
            if current_node.prosjecna_zarada < self.max_zarada():
                lista.append(current_node.ime)
            self.trazi(current_node.left, lista)
            self.trazi(current_node.right, lista)
        return lista
    
#Napisati funkciju min_zarada (root: Node) koja treba da vrati ime pjevača čija je prosječna zarada najveća.

    def max_zarada(self):
        if self.root is None:
            print ("Stablo je prazno")
        else:
            current = self.root
            while current.right:
                current = current.right
            return current.prosjecna_zarada

#Napisati funkciju preorder (root: Node) koja treba da štampa sve čvorove stabla po preorder načinu obilaska.

    def preorder_print(self, start, traversal):
            if start:
                traversal += (str(start.ime) + "-" + str(start.prosjecna_zarada) + " -> ")
                traversal = self.preorder_print(start.left, traversal)
                traversal = self.preorder_print(start.right, traversal)
            return traversal


n1 = Node("Arnad", 300)

stablo = BinaryTree(n1)

n2 = Node("Elvis", 500)
n3 = Node("Anesa", 400)
n4 = Node("Nikola", 200)
n5 = Node("Marko", 100)
n6 = Node("Balsa", 600)


stablo.dodaj(n2)
stablo.dodaj(n3)
stablo.dodaj(n4)
stablo.dodaj(n5)
stablo.dodaj(n6)
lista = []
print(stablo.max_zarada())
print(stablo.preorder_print(stablo.root, ""))
print(stablo.trazi(stablo.root,lista))
