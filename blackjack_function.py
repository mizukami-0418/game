import random

print("BJゲーム開始")

# トランプを作成
card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_card = []
com_card = []

# カード選択関数
def card_choice():
    index = random.randrange(len(card_list))
    select_card = card_list.pop(index)
    return select_card

# 選んだカードをカードリストに格納する
def select_card(card_list):
    select_card = card_choice()
    card_list.append(select_card)

# カードを配布
def deal_the_cards():
    for _ in range(2):
        # プレイヤーのカード
        select_card(player_card)
        # comのカード
        select_card(com_card)


def change_ace(card_list):
    index = card_list.index(11)
    card_list[index] = 1
    return sum(card_list)

# プレイヤーのカード追加
def player_add_card():
    while True:
        print(player_card)
        add_choice = input("追加でカードが必要ですか？'yes' or 'no'：")
        player_total = sum(player_card)
        if add_choice == "yes":
            select_card(player_card)
            new_total = sum(player_card)
            if new_total > 21:
                if 11 in player_card:
                    # エースがあれば1でカウントする
                    next_total = change_ace(player_card)
                    print(f"合計は{next_total}")
                else:
                    print(f"合計{new_total}です。")
                    return new_total
                    break
        else:
            return player_total
            break

# comのカード追加。15以下の場合は自動で引き続ける
def com_add_card():
    while True:
        com_total = sum(com_card)
        if com_total <= 15:
            select_card(com_card)
            new_total = sum(com_card)
            if new_total > 21:
                if 11 in com_card:
                    # エースがあれば1でカウントする
                    next_total = change_ace(com_card)
                else:
                    return new_total
                    break
        else:
            return com_total
            break

def judgement(player_score, com_score):
    if player_score > 21 and com_score > 21:
        return print(f"プレイヤー:{player_score}　com:{com_score}　両方バーストで引き分けです")
    elif player_score > 21:
        return print(f"プレイヤー:{player_score}　com:{com_score}　comの勝ちです")
    elif com_score > 21:
        return print(f"プレイヤー:{player_score}　com:{com_score}　あなたの勝ちです")
    elif player_score == com_score:
        return print(f"プレイヤー:{player_score}　com:{com_score}　引き分けです")
    elif player_score > com_score:
        return print(f"プレイヤー:{player_score}　com:{com_score}　あなたの勝ちです")
    else:
        return print(f"プレイヤー:{player_score}　com:{com_score}　comの勝ちです")


# プレイヤーのカードとcomの１枚目をオープン
deal_the_cards()
c_card1 = com_card[0]

print(f"プレイヤーの手札は：{player_card}")
print(f"ディーラーの手札は：{c_card1}")

player_score = player_add_card()
com_score = com_add_card()
judgement(player_score, com_score)