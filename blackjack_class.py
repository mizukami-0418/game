import random

class CardDeck:
    # Initialized the card deck
    def __init__(self):
        self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # Draw a card from the card deck
    def draw_card(self):
        if self.cards:
            index = random.randrange(len(self.cards))
            return self.cards.pop(index)
        else:
            raise ValueError("カードがもうありません")


class Player():
    # Initialized the player's cards
    def __init__(self):
        self.cards = []

    # Add a card to my hand
    def add_card(self, card):
        self.cards.append(card)

    # Adjust Ace value
    def adjust_for_ace(self):
        for i in range(len(self.cards)):
            if self.cards[i] == 11:
                self.cards[i] = 1
                break

    # Calculate the total of cards
    def score(self):
        total = sum(self.cards)
        if total > 21 and 11 in self.cards:
            self.adjust_for_ace()
            total = sum(self.cards)
        return total

class BlackJackGame():
    def __init__(self):
        self.deck = CardDeck()
        self.player = Player()
        self.dealer = Player()

    # Deal initial cards to player and dealer
    def deal_initial_cards(self):
        for _ in range(2):
            self.player.add_card(self.deck.draw_card())
            self.dealer.add_card(self.deck.draw_card())

    # Draw a card for the player
    def player_turn(self):
        while True:
            print(f"あなたの手札は{self.player.cards}　合計：{self.player.score()}")
            choice = input("カードを引きますか？　(yes/no)：")
            if choice.lower() == 'yes':
                self.player.add_card(self.deck.draw_card())
                if self.player.score() > 21:
                    if 11 in self.player.cards:
                        self.player.adjust_for_ace(self.player.cards)
                    else:
                        print("バーストです")
                        break
            elif choice.lower() == 'no':
                break
            else:
                print("yesかnoで入力お願いします")

    # Automatically draw cards for the dealer
    def dealer_turn(self):
        while self.dealer.score() < 16:
            self.dealer.add_card(self.deck.draw_card())
            if self.dealer.score() > 21:
                if 11 in self.dealer.cards:
                    self.dealer.adjust_for_ace(self.dealer.cards)
                else:
                    break


    # Judge the result
    def judge(self):
        p = self.player.score()
        d = self.dealer.score()
        print(f"あなたの手札: {self.player.cards} 合計: {p}")
        print(f"ディーラーの手札: {self.dealer.cards} 合計: {d}")

        if p > 21 and d > 21:
            print("両方バーストで引き分け")
        elif p > 21:
            print("あなたはバースト。ディーラーの勝ち！")
        elif d > 21:
            print("ディーラーがバースト。あなたの勝ち！")
        elif p > d:
            print("あなたの勝ち！")
        elif p < d:
            print("ディーラーの勝ち！")
        else:
            print("引き分け！")

    # Replay the game
    def replay(self):
        while True:
            replay_select = input("もう一度プレイしますか？（yes/no）:")
            if replay_select.lower() == "yes":
                self.deck = CardDeck()
                self.player = Player()
                self.dealer = Player()
                self.play()
                break
            elif replay_select.lower() == "no":
                print("ゲームを終了します")
                break
            else:
                print("yesかnoで入力して下さい")

    # Play the game
    def play(self):
        self.deal_initial_cards()
        self.player_turn()
        self.dealer_turn()
        self.judge()
        self.replay()

if __name__ == "__main__":
    game = BlackJackGame()
    game.play()