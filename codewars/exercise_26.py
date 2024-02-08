class VendingMachine:
    def __init__(self, num_items, item_coins):
        self.num_items = num_items
        self.item_coins = item_coins

    def buy(self, num_items_to_buy, num_coins):
        if num_items_to_buy > self.num_items:
            raise ValueError("Not enough items in stock")
        if num_coins < self.item_coins:
            raise ValueError("Not enough coins inserted")

        total_coins_needed = num_items_to_buy * self.item_coins
        change = num_coins - total_coins_needed

        if change < 0:
            raise ValueError("Not enough coins inserted")

        self.num_items -= num_items_to_buy
        return change
