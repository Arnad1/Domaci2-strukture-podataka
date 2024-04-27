
class Node:
    def __init__(self, ime : str, ulaz : int):
        self.ime = ime
        self.ulaz = ulaz
        self.next = None

class CircularLinkedList:
    def __init__(self, head = None):
        self.head = head

    # dodavanje nove stanice, proslijeđuje se Node (koji ima naziv stanice i broj putnika koji ulaze na tu stanicu) i prosljeđuje se broj putnika koji izlaze 
    # ovim insterom će Node.ulaz predstavljati koliko je putnika trenutno tu, a ne koliko je putnika ušlo na ovu stanicu, jer dodajemo preostale putnike sa prethodne stanice i oduzimamo koliko izlazi
    def unesi(self, nova_stanica, izlaz):
        current = self.head
        preostalo = 0
        if not self.head:
            self.head = nova_stanica
            nova_stanica.next = self.head
            nova_stanica.ulaz = nova_stanica.ulaz - izlaz
        else:
            while current.next != self.head:
                current = current.next
            preostalo = current.ulaz
            current.next = nova_stanica
            nova_stanica.next = self.head
            nova_stanica.ulaz = nova_stanica.ulaz + preostalo - izlaz
        if nova_stanica.ulaz<0:
            nova_stanica.ulaz = 0
            print("Svi putnici su izašli")
        

    #print sva stajalista i broj putnika
    def sva_stajalista(self):
        current = self.head
        if not self.head:
            print("Trasa ne postoji")
        else:
            while current.next != self.head:
                print(f"Stajalište: {current.ime}; Broj putnika {current.ulaz}")   
                current = current.next
            print(f"Stajalište: {current.ime}; Broj putnika {current.ulaz}")   
                     
            
    # funkcija za prolaženje kroz prethodno postavljena stajališta 5 puta, na početku će broj putnika biti 0
    def kruzenje_tramvaja(self):
        current = self.head
        current.ulaz = 0
        i = 0
        preostalo = 0
        br_krugova = int(input("Koliko krugova pravi tramvaj: "))
        while i < br_krugova:
            preostalo = 0
            trasa = {}
            while current.next != self.head:
                ulazi = int(input(f"Broj putnika koji ulaze na stanici {current.ime}: "))
                izlazi = int(input(f"Broj koji izlazi: "))
                current.ulaz = preostalo + ulazi - izlazi
                if current.ulaz<0:
                    current.ulaz= 0
                preostalo = current.ulaz
                trasa[current.ime] = current.ulaz
                current = current.next    
            ulazi = int(input(f"Broj putnika koji ulaze na stanici {current.ime}: "))
            izlazi = int(input(f"Broj koji izlazi: "))
            current.ulaz = preostalo + ulazi - izlazi
            if current.ulaz<0:
                    current.ulaz= 0
            preostalo = current.ulaz
            trasa[current.ime] = current.ulaz
            print ("Trasa tramvaja:")
            print(trasa)
            current = self.head
            i += 1        

            
tramvaj8 = CircularLinkedList()

# staviću da ima 5 stanica i da se smjena završava nakon broja krugova koji korisnik unese

n1 = Node("Hotel Hilton", 10)
n2 = Node("Delta City", 30)
n3 = Node("Donja Gorica", 25)
n4 = Node("Stara Varoš", 15)
n5 = Node("Gintaš", 8)

#unosi se node sa imenom stanice i brojem putnika koji ulaze, a drugi atribut je broj putnike koji izlaze na toj stanici, uzima u obzir broj preostalih putnika sa prethodne stanice
tramvaj8.unesi(n1, 6)
tramvaj8.unesi(n2,20)
tramvaj8.unesi(n3,30)
tramvaj8.unesi(n4,7)
tramvaj8.unesi(n5,15)

# funkcija kruzenje_tramvaja uzima u obzir i dodaje broj putnika koji su preostali iz prethodne stanice, i racuna da pocetkom svake nove rute svi putnici izlaze
tramvaj8.sva_stajalista()
tramvaj8.kruzenje_tramvaja() 
