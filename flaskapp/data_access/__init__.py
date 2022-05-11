CREATED_MOVEMENT_QUERY="SELECT * FROM movimientos WHERE fecha=? and hora=? and moneda_from=? and cantidad_from=? and moneda_to=? and cantidad_to=?"
SAVE_MOVEMENT_QUERY="INSERT INTO movimientos(fecha,hora,moneda_from,cantidad_from,moneda_to,cantidad_to) VALUES (:fecha, :hora, :moneda_from, :cantidad_from, :moneda_to, :cantidad_to);"
GET_ALL_MOVEMENTS_QUERY="SELECT * FROM movimientos"
GET_BALANCE_EUROS_INVESTED="SELECT SUM(cantidad_to)-SUM(cantidad_from) AS balance FROM movimientos WHERE moneda_to=? and moneda_from=?"
CURRENT_VALUE_CRIPTO_TO_EURO="SELECT SUM(cantidad_to)-(SELECT SUM(cantidad_from)FROM movimientos WHERE Moneda_from=?) AS value FROM movimientos WHERE Moneda_to=?"
GET_TOTAL_EUROS_INVESTED="SELECT SUM(cantidad_from) FROM movimientos WHERE moneda_from=?"
CURRENCIES=[
    "BTC",
    "ETH",
    "BNB",
    "LUNA",
    "SOL",
    "BCH",
    "LINK",
    "ATOM",
    "USDT"
]


COLUMN_ID=0
COLUMN_FECHA=1
COLUMN_HORA=2
COLUMN_MONEDA_FROM=3
COLUMN_CANTIDAD_FROM=4
COLUMN_MONEDA_TO=5
COLUMN_CANTIDAD_TO=6






