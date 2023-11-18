class Grid():
    def __init__(self, level_num, limit_price, quantity, side, status, order=None):
        self.level_num = level_num
        self.limit_price = limit_price
        self.quantity = quantity
        self.side = side
        self.status = status
        self.order = None
    
    def __repr__(self):
        return f"{{Grid level_num: {self.level_num}, limit_price: {self.limit_price}, quantity: {self.quantity}, side: {self.side}, status: {self.status}, order: {self.order}}}"
