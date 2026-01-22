from pydantic import BaseModel, Field
from typing import List, Optional

class AddressInfo(BaseModel):
    name: str = "NA"
    address: str = "NA"
    phone: Optional[str] = "NA"

class InvoiceItem(BaseModel):
    item_name: str = "NA"
    item_number: str = "NA"
    unit: str = "NA"
    per_case_count: str = "NA"
    size: str = "NA"
    unit_price: float = 0.0
    unit_disc: float = 0.0
    unit_net: float = 0.0
    upc: str = "NA"
    crv_amount: float = 0.0
    promo: str = "NA"
    quantity_ordered: int = 0
    quantity_delivered: int = 0
    itemcount_delivered: int = 0
    tax: float = 0.0
    total: float = 0.0

class Totals(BaseModel):
    total_ordered_items: int = 0
    total_cs_items: int = 0
    total_items: int = 0
    total_gross_amount: float = 0.0
    total_discounts: float = 0.0
    total_net_amount: float = 0.0
    total_taxes: float = 0.0
    amount_due: float = 0.0
    payment_due_date: str = "NA"

class InvoiceSchema(BaseModel):
    invoice_number: str = "NA"
    invoice_date: str = "NA"
    delivery_date: str = "NA"
    sold_to: AddressInfo
    ship_to: AddressInfo
    Vendor: AddressInfo
    items: List[InvoiceItem]
    totals: Totals