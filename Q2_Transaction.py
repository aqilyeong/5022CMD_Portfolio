from datetime import datetime

# ==========================================
# Entity Class
# ==========================================

class Transaction:
    """
    Entity class representing a customer transaction in an online shopping system.
    Attributes are encapsulated with validation to ensure data integrity.
    """

    def __init__(self, transaction_id: str, customer_name: str,
                 product_name: str, amount: float, transaction_date: str):
        if amount < 0:
            raise ValueError(f"Amount cannot be negative. Got: {amount}")
        # YYYY-MM-DD format allows correct lexicographic date comparison during sorting
        try:
            datetime.strptime(transaction_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Date must be in YYYY-MM-DD format. Got: {transaction_date}")

        self._transaction_id   = transaction_id.strip().upper()
        self._customer_name    = customer_name.strip()
        self._product_name     = product_name.strip()
        self._amount           = float(amount)
        self._transaction_date = transaction_date.strip()

    @property
    def transaction_id(self) -> str:
        return self._transaction_id

    @property
    def customer_name(self) -> str:
        return self._customer_name

    @property
    def product_name(self) -> str:
        return self._product_name

    @property
    def amount(self) -> float:
        return self._amount

    @property
    def transaction_date(self) -> str:
        return self._transaction_date

    @amount.setter
    def amount(self, value: float) -> None:
        if value < 0:
            raise ValueError("Amount cannot be negative.")
        self._amount = float(value)

    def __str__(self) -> str:
        return (f"[{self._transaction_id}] {self._customer_name:<15} | "
                f"{self._product_name:<18} | ${self._amount:>9.2f} | {self._transaction_date}")

    def __repr__(self) -> str:
        return (f"Transaction(id='{self._transaction_id}', customer='{self._customer_name}', "
                f"product='{self._product_name}', amount={self._amount}, "
                f"date='{self._transaction_date}')")