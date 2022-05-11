CREATE TABLE "movimientos" (
	"id"	INTEGER,
	"Fecha"	TEXT NOT NULL,
	"Hora"	TEXT NOT NULL,
	"Moneda_from"	TEXT NOT NULL,
	"Cantidad_from"	REAL NOT NULL,
	"Moneda_to"	TEXT NOT NULL,
	"Cantidad_To"	REAL NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
)