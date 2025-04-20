import random

janken = ["g", "c", "p"]

print("じゃんけんゲーム開催")

# プレイヤー選択
def user_select():
    user_select = input("グー(g)、チョキ(c)、パー(p)をアルファベットで選んでください:")
    return user_select

# com選択
def com_select():
    com_select = random.choice(janken)
    return com_select

# じゃんけんの結果判定
def game_result(u_select, c_select, even, win, lose):
    print(f"あなたは{u_select}、COMは{c_select}")
    if u_select == c_select:
        even += 1
        print("あいこ")
    elif u_select == "g" and c_select == "c" or u_select == "c" and c_select == "p" or u_select == "p" and c_select == "g":
        win += 1
        print("あなたの勝ち")
    else:
        lose += 1
        print("COMの勝ち")
    return win, lose, even # win、lose、evenの値を更新する


def janken_game():
    is_game_over = False
    win = 0
    lose = 0
    even = 0

    while not is_game_over:
        user = user_select()
        com = com_select()
        win, lose, even = game_result(user, com, win, lose, even)
        game_continue = input("つづけますか？'y' or 'n':")
        if game_continue == "n":
            print("ゲーム終了")
            print(f"結果は{win}勝{lose}敗{even}分")
            is_game_over = True
        else:
            print("つづけます")

janken_game()