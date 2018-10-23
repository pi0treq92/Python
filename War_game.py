##################
#  Card war game #
##################


from random import shuffle

Color = 'H D S C'.split()
Ranking = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


#Tworzenie talii za pomocą List comprehension
mycards = [(c,r) for c in Color for r in Ranking]

#Tworzenie talii za pomocą nested loop
mycard = []
for r in Ranking:
    for c in Color:
        mycard.append((c,r))
class Deck:
    def __init__(self):
        print("Tworzenie nowej talii")
        self.allcards = mycards

    def shuffle(self):
        print('Tasowanie')
        shuffle(self.allcards)

    def split_on_half(self):
        print('Rozdawanie')
        return(self.allcards[:26], self.allcards[26:])

class Hand:
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return 'Masz {} kart'.format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove(self ):
        return self.cards.pop()

class Player:

    """
    Klasa Player pobiera imie z instancji Hand.
    Obiekt klasy Player może zagrywać karty i sprawdzać czy wciąż je posiada

    """

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove()
        print('{} rzuca {} karte'.format(self.name, drawn_card))
        print('\n')
        return drawn_card

# Metoda dzieki ktorej, gracz wyklada trzy karty na stol, podczas wojny
    def remove_war_card(self):
        war_card = []
        if len(self.hand.cards)<3:
            return self.hand.cards
        else:
            for x in range(3):
                war_card.append(self.hand.remove())
            return war_card

    def still_has(self):
        """

        Sprawdza czy Gracz ma wciaz karty

        """
        return len(self.hand.cards) !=0

class Play:
    pass

print('Witaj w grze w wojne')

d = Deck()
d.shuffle()

half1, half2 = d.split_on_half()

comp = Player('Computer', Hand(half2))

name = input('Wpisz swoje imie: ')
gracz = Player(name, Hand(half1))

rounds = 0
war_count = 0

while(gracz.still_has() and comp.still_has()):
    rounds +=1
    print('Nowa runda')
    print('Aktualny wynik')
    print(gracz.name+' ma: '+str(len(gracz.hand.cards)))
    print(comp.name + ' ma: ' + str(len(comp.hand.cards)))
    print('graj!\n')

    table_card = []

    c_card = comp.play_card()
    p_card = gracz.play_card()

    table_card.append(c_card)
    table_card.append((p_card))

#Sprawdzenie czy na stole jest wojna
    if c_card[1] == p_card[1]:
# Indeks 1 ponieważ mamy tuple gdzie indeks zawiera ranking

        war_count +=1
        print('Wojna')

        table_card.extend(gracz.remove_war_card())
        table_card.extend(comp.remove_war_card())

#Porownanie kart na stole, inaczej Ranking[index(c_card[1]) = 5 ]
        if Ranking.index(c_card[1]) < Ranking.index(p_card[1]):
            comp.hand.add(table_card)
        else:
            gracz.hand.add(table_card)

    else:
        if Ranking.index(c_card[1]) < Ranking.index(p_card[1]):
            comp.hand.add(table_card)
        else:
            gracz.hand.add(table_card)

print('Game over, liczba rund: '+str(rounds))
print('Wojne pojawila sie '+str(war_count)+' razy')
if comp.still_has() == 0:
    print('Wygrales! ')
else:
    print('Przegrales {}! :('.format(gracz.name))

