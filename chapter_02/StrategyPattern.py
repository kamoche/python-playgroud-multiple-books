class Order:

    def __init__(self, customer, item, promotion=None):
        self.customer = customer
        self.items = list(item)
        self.promotion = promotion


