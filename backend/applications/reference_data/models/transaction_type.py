from django.db import models
from applications.abstracts.models.global_abastract_model import AbstractModel


class TransactionType(AbstractModel):
    """
    Represents a type of transaction in the marketplace.

    Categorizes how a collectible item is exchanged,
    such as through sale, auction, or trade.
    Notes:
    fill the model through fixture:
    path: reference_data/fixtures/transaction_type.json

    """

    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = "transactionstypes"
        verbose_name = "Transaction Type"
        verbose_name_plural = "Transactions Types"
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name

    def __repr__(self):
        return f"{type(self).__name__}(name={self.name}, is_active={self.is_active})"
