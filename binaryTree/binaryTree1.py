print("hellow word")

class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

drinks=node("drinks")
hot=node("hot")
cold=node("cold")
tea=node("tea")
coffee=node("coffee")
cola=node("cola")
fanta=node("fanta")

hot.left=tea
hot.right=cola
cold.left=coffee
cold.right=fanta

drinks.left=hot
drinks.right=cold

print(drinks.left.left.data)