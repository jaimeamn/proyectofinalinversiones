CREATED_MOVEMENT_QUERY="SELECT * FROM movimientos WHERE fecha=? and hora=? and moneda_to=? and cantidad_to=? and moneda_from=? and cantidad_from=?"
SAVE_MOVEMENT_QUERY="INSERT INTO movimientos(fecha,hora,moneda_from,cantidad_from,moneda_to,cantidad_to) VALUES (:fecha, :hora, :moneda_to, :cantidad_to, :moneda_from, :cantidad_from);"
GET_ALL_MOVEMENTS_QUERY="SELECT * FROM movimientos"
GET_BALANCE_EUROS_INVESTED="SELECT SUM(cantidad_to)-SUM(cantidad_from) AS balance FROM movimiento WHERE moneda_to=? and moneda_from=?"

COLUMN_ID=0
COLUMN_FECHA=1
COLUMN_HORA=2
COLUMN_MONEDA_FROM=3
COLUMN_CANTIDAD_FROM=4
COLUMN_MONEDA_TO=5
COLUMN_CANTIDAD_TO=6






