"""
Module contain choices variation for models.py

ATTENTION! DO NOT USE IMPORT IN THIS MODULE

For add new choice:

    NEW_VAR: str = 'NEw_vAr'

    CURRENCY_TYPES: tuple = (
    (NEW_VAR, 'The text that the user sees in choice list')
)

______________________________
More info find: django choices
"""

CURRENCY_UAH: str = 'UAH'
CURRENCY_EUR: str = 'EUR'
CURRENCY_USD: str = 'USD'
CURRENCY_PLD: str = 'PLD'
CURRENCY_BTC: str = 'BTC'

CURRENCY_TYPES: tuple = (
    (CURRENCY_UAH, 'UAH'),
    (CURRENCY_EUR, 'EUR'),
    (CURRENCY_USD, 'USD'),
    (CURRENCY_PLD, 'PLD'),
    (CURRENCY_BTC, 'BTC'),
)

