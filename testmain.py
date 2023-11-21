


#key入力　アップ、ダウン
#マウス入力


#set stage
#stage
#stageが持つ値は？
#敵の初期位置
#取得可能なアイテム
#プレイヤーの初期位置
##index= シーン　timer=リセットタイミング

#ゲーム画面描画
##縦x横 最大幅 
## ÷1マスxxpx x xx px 合わせてimagecreate

# move_human
# 移動チェック

#  X = X+n
#   &Y   [0][1][2][n]
#score




# import tkinter as tk

# class ClickerGame:
#     def __init__(self):
#         self.money = 0
#         self.plus = 1

#     def press(self, button, value):
#         print(f"ボタン {button} が押されました。")
#         self.plus = value
#         self.money += self.plus
#         self.update()

#     def update(self):
#         money_label.config(text=f"お金: {self.money} 円")

# def button(button, value):
#     game.press(button, value)

# game = ClickerGame()

# root = tk.Tk()
# root.title("Clicker Game")

# money_label = tk.Label(root, text="お金: 0 円")
# money_label.pack(pady=10)

# button_a = tk.Button(root, text="ボタン A", command=lambda: button('A', 2))
# button_a.pack(pady=5)

# button_b = tk.Button(root, text="ボタン B", command=lambda: button('B', 5))
# button_b.pack(pady=5)

# button_c = tk.Button(root, text="ボタン C", command=lambda: button('C', 10))
# button_c.pack(pady=5)

# root.mainloop()








import tkinter as tk
from tkinter import messagebox

class Game:
    def __init__(self):
        self.click_count = 0
        self.auto_items = []

    def click(self):
        self.click_count += 1

    def buy_auto_item(self, cost, auto_rate):
        if self.click_count >= cost:
            self.click_count -= cost
            self.auto_items.append(AutoItem(auto_rate))
        else:
            messagebox.showinfo("Not enough clicks", f"You need at least {cost} clicks to buy this.")

    def auto_clicker(self):
        for auto_item in self.auto_items:
            auto_item.click()

class AutoItem:
    def __init__(self, auto_rate):
        self.auto_rate = auto_rate

    def click(self):
        # AutoItemがクリックされたときに実際に何らかの処理を行う必要があります。
        # ここではクリックされるたびに `auto_rate` を加算することにしてみましょう。
        self.auto_rate += 1

class ClickerUI:
    def __init__(self, master, game):
        self.master = master
        self.game = game

        self.master.title("Clicker")

        self.label = self.create_label(f"Clicks: {self.game.click_count}", pady=10)

        self.click_button = self.create_button("Click me!", self.click, pady=20)
        self.auto_button = self.create_button("Buy Auto", self.buy_auto, pady=10)

        self.auto_clicker()

    def create_label(self, text, **kwargs):
        label = tk.Label(self.master, text=text)
        label.pack(**kwargs)
        return label

    def create_button(self, text, command, **kwargs):
        button = tk.Button(self.master, text=text, command=command)
        button.pack(**kwargs)
        return button

    def click(self):
        self.game.click()
        self.update()

    def buy_auto(self):
        self.game.buy_auto_item(10, 1)  # cost: 10, auto_rate: 1
        self.update()

    def auto_clicker(self):
        self.game.auto_clicker()
        self.update()
        self.master.after(1000, self.auto_clicker)

    def update(self):
        self.label.config(text=f"Clicks: {self.game.click_count}")

if __name__ == "__main__":
    root = tk.Tk()
    game = Game()
    clicker_ui = ClickerUI(root, game)
    root.mainloop()












