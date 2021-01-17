from cards import Card
import random

class Game:
	
    def __init__ (self):
        self.size = 4
        self.card_options = ['Add', 'Boo', 'Cat', 'Dev',
							 'Egg', 'Far', 'Gum', 'Hut'] 
        self.columns = ['A', 'B', 'C', 'D']
        self.cards = []
        self.locations = []
        for column in self.columns:
            for num in range(1, self.size + 1):
                self.locations.append(f'{column}{num}')


    def set_cards(self):
        used_locations = []
        for word in self.card_options:
            for i in range(2):
                available_locations = set(self.locations) - set(used_locations)
                random_location = random.choice(list(available_locations))
                used_locations.append(random_location)
                card = Card(word, random_location)
                self.cards.append(card)
                self.cards.append(card)
									
	def create_row(self, num):
		row = []
		for column in self.columns:
			for card in self.cards:
				if card.location == f'{column}{num}':
					if card.matched:
						row.append(str(card))
					else:
						row.append("   ")
		return row
		
#method
	#create cards
	#create grid
	#check for matches
	#check game wom
	#run game
	

#dunder main
if __name__ == "__main__":
	game = Game()
	game.set_cards()
	game.cards[0].matched = True
	game.cards[1].matched = True
	game.cards[2].matched = True
	game.cards[3].matched = True
	print(game.create_row(1))
	print(game.create_row(2))
	print(game.create_row(3))
	print(game.create_row(4))
	#create game instance
	#call start game
