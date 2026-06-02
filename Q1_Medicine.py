# ==========================================
# 1. Entity Class & Data Structure
# ==========================================
class Medicine:
    """Entity class representing a pharmacy product."""

    def __init__(self, product_id, name, item_type, price, stock):
        self.product_id = product_id
        self.name = name
        self.item_type = item_type  # e.g., tablets, syrup, supplements
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"[{self.product_id}] {self.name} ({self.item_type}) - ${self.price:.2f} | Stock: {self.stock}"
