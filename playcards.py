class Card():
    # 定义牌面数字
    RANKS = ["A", "2", "3", "4", "5", "6",
             "7", "8", "9", "10", "J", "Q", "K"]
    # 定义纸牌花色
    SUITS = ["梅", "方", "红", "黑"]

    # 初始化牌面、花色、是否显示正面
    def __init__(self, rank, suit, face_up=True):
        self.rank = rank  # 指牌面数字1-13
        self.suit = suit  # 指牌面花色
        self.is_face_up = face_up  # 是否显示牌的正面，true为正

    # 打印纸牌信息函数
    def __str__(self):
        if self.is_face_up:
            rep = self.suit + self.rank
        else:
            rep = "XX"
        return rep

    # 定义纸牌的顺序号
    def pic_order(self):
        if self.rank == "A":
            FaceNum = 1
        elif self.rank == "J":
            FaceNum = 11
        elif self.rank == "Q":
            FaceNum = 12
        elif self.rank == "K":
            FaceNum = 13
        else:
            FaceNum = int(self.rank)

        if self.suit == "梅":
            Suit = 1
        elif self.suit == "方":
            Suit = 2
        elif self.suit == "红":
            Suit = 3
        elif self.suit == "黑":
            Suit = 4

        return (Suit - 1) * 13 + FaceNum

    # 定义翻牌方法
    def flip(self):
        self.is_face_up = not self.is_face_up

# 定义一手牌的类，即一个玩家手里的牌


class Hand():
    def __init__(self):
        self.cards = []  # cars列表变量存储牌手手里的牌

    def __str__(self):  # 重写print方法 打印牌手手中的牌
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + '\t'
        else:
            rep = "无牌"
        return rep

    def claer(self):  # 清空手里的牌
        self.cards = []

    def add(self, card):  # 增加牌
        self.cards.append(card)

    def give(self, card, other_hand):  # 把牌给其他牌手的方法
        self.cards.remove(card)
        other_hand.add(card)


# 定义一副牌的类 可以看做是一个手里有52张牌的牌手 所以继承自hand类，其中cards列表中存储了52张牌，且需要增加洗牌、发牌的方法


class Poke(Hand):
    def populate(self):  # 生成一副牌
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):  # 洗牌方法
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=13):  # 发牌给每个玩家 每人默认13张牌
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("不能发牌了，牌已经发完了")

# 主程序


if __name__ == '__main__':
    print("这是一个简单的纸牌游戏模块")
    players = [Hand(), Hand(), Hand(), Hand()]
    poke1 = Poke()
    poke1.populate()  # 生成一副牌
    poke1.shuffle()  # 洗牌
    poke1.deal(players, 13)

    # 显示4位牌手的牌
    n = 1

    for hand in players:
        print("牌手", n, end=":")
        print(hand)
        n = n + 1
    input("\n按任意键退出")
