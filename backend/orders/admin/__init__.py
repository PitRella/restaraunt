from .terminal_payment import TerminalPaymentAdmin
from .cash_payment import CashPaymentAdmin
from .card_payment import CardPaymentAdmin
from .orders import OrderAdmin

__all__ = [
    'TerminalPaymentAdmin',
    'CardPaymentAdmin',
    'CashPaymentAdmin',
    'OrderAdmin'
]
