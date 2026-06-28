# ==========================================
# 1. Entity Class
# ==========================================
class Medicine:
    """
    Entity class representing a pharmacy product.
    Attributes are encapsulated with validation to prevent invalid data states.
    """

    def __init__(self, product_id: str, name: str, item_type: str, price: float, stock: int):
        # Validate on construction so invalid objects can never exist
        if price < 0:
            raise ValueError(f"Price cannot be negative. Got: {price}")
        if stock < 0:
            raise ValueError(f"Stock cannot be negative. Got: {stock}")

        self._product_id = product_id.strip().upper()
        self._name = name.strip()
        self._item_type = item_type.strip().lower()  # normalise type casing
        self._price = price
        self._stock = stock

    # --- Read-only properties ---
    @property
    def product_id(self):
        return self._product_id

    @property
    def name(self):
        return self._name

    @property
    def item_type(self):
        return self._item_type

    @property
    def price(self):
        return self._price

    @property
    def stock(self):
        return self._stock

    # --- Writable properties with validation ---
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    @stock.setter
    def stock(self, value):
        if value < 0:
            raise ValueError("Stock cannot be negative.")
        self._stock = value

    def __str__(self):
        return (f"[{self._product_id}] {self._name} ({self._item_type}) "
                f"- ${self._price:.2f} | Stock: {self._stock}")

    def __repr__(self):
        return (f"Medicine(product_id='{self._product_id}', name='{self._name}', "
                f"item_type='{self._item_type}', price={self._price}, stock={self._stock})")