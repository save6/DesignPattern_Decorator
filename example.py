'''
このコードは下記で紹介されているコードをpythonで書き直したものである。
https://www.youtube.com/watch?v=5SGdJJbrG9c&list=PL0Chh2JCYszDG15UY13BRvKfiE52feXu9&index=5

【希望】
- なるべくカードの種類は切り替えやすくしておきたい
- 複数のカード属性を好きに付けられるようにしておきたい
'''

class Card():
    def __init__(self,name,description):
        self.__name = name
        self.__description = description
    
    def getName(self):
        return self.__name
    
    def getDescription(self):
        return self.__description

class SRCard():
    def __init__(self,card):
        self.__card = card
    
    def getName(self):
        return "[SR]" + self.__card.getName()
    
    def getDescription(self):
        return "★★★★★★★★★★★★★★★\n" + self.__card.getDescription() + "\n★★★★★★★★★★★★★★★"

class RCard():
    def __init__(self,card):
        self.__card = card
    
    def getName(self):
        return "[R]" + self.__card.getName()
    
    def getDescription(self):
        return "---------------\n" + self.__card.getDescription() + "\n---------------"

class BossCard():
    def __init__(self,card):
        self.__card = card
    
    def getName(self):
        return "[BOSS]" + self.__card.getName()
    
    def getDescription(self):
        return self.__card.getDescription()

def showProperties(card):
    print("名前：" + card.getName())
    print("名前：\n" + card.getDescription())
    
if __name__=='__main__':
    CARDS = [
        Card("村人", "ほとんど戦力にはならない村人"),
        RCard(Card("傭兵", "金さえ出せば何でもこなす傭兵")),
        SRCard(Card("勇者", "訓練を積んだ歴戦の勇士")),
        BossCard(SRCard(Card("レッドドラゴン", "遥か昔から生き続ける火龍")))
    ]

    print("【カードゲームキャラ一覧】\n")

    for card in CARDS:
        showProperties(card)
        print("\n")
