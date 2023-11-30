# My daughter's name is Laney, and she watched me create this file, so it is named after her.

import random

class Card:
    def __init__(self, name, cost, card_type):
        self.name = name
        self.cost = cost
        self.card_type = card_type

    def __str__(self):
        return f"{self.name} ({self.cost})"

class Player:
    def __init__(self, name):
        self.name = name
        self.deck = []
        self.hand = []
        self.discard_pile = []

    def draw_hand(self, num_cards):
        for _ in range(num_cards):
            if not self.deck:
                self.shuffle_discard_into_deck()
            card = self.deck.pop()
            self.hand.append(card)

    def shuffle_discard_into_deck(self):
        random.shuffle(self.discard_pile)
        self.deck.extend(self.discard_pile)
        self.discard_pile = []

    def gain_card(self, card):
        self.discard_pile.append(card)

    def play_card(self, card_index):
        if 0 <= card_index < len(self.hand):
            card = self.hand.pop(card_index)
            self.discard_pile.append(card)
            return card
        return None

    def show_hand(self):
        print(f"{self.name}'s hand: {', '.join(map(str, self.hand))}")

def initialize_game():
    kingdom_cards = [
        Card("Copper", 0, "Treasure"),
        Card("Silver", 3, "Treasure"),
        Card("Gold", 6, "Treasure"),
        Card("Estate", 2, "Victory"),
        Card("Duchy", 5, "Victory"),
        Card("Province", 8, "Victory"),
    ]

    # Initialize players
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    # Initialize supply piles
    supply_piles = {card.name: 10 for card in kingdom_cards}

    return player1, player2, supply_piles

def main():
    player1, player2, supply_piles = initialize_game()

    current_player = player1

    while supply_piles["Province"] > 0:
        print("\n" + "=" * 30)
        print(f"{current_player.name}'s turn")

        current_player.draw_hand(5)
        current_player.show_hand()

        # Implement player's turn logic here
        # For simplicity, let's assume the player buys a Province if they can afford it
        if supply_piles["Province"] > 0 and any(card.name == "Gold" for card in current_player.hand):
            current_player.gain_card(Card("Province", 8, "Victory"))
            supply_piles["Province"] -= 1
            print(f"{current_player.name} buys a Province!")

        current_player.show_hand()

        # End the turn
        current_player.shuffle_discard_into_deck()

        # Switch to the other player
        current_player = player2 if current_player == player1 else player1

    print("\nGame Over!")
    print(f"{current_player.name} wins!")

if __name__ == "__main__":
    main()
