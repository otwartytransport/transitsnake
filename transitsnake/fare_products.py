from dataclasses import dataclass
from typing import ClassVar, Optional, Dict

from transitsnake import BaseDatasetType, Field
from transitsnake.validation import currency_code


@dataclass
class FareProduct(BaseDatasetType):
    filename: ClassVar[str] = 'fare_products.txt'
    primary_key: ClassVar[tuple] = ('fare_product_id',)

    fare_product_id: str
    amount: float
    currency: str
    fare_product_name: Optional[str] = None

    meta: ClassVar[Dict[str, Field]] = {
        'currency': Field(validators=currency_code)
    }
