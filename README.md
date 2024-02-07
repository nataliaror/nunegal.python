# nunegal.python
# Python tasks

Process arguments:
-c: clears mongodb tempo collection
-p: processes tempo files from configured directory


# -p TASKS:
1. Reads all .xlsx Tempo files from configured directory
2. Creates a JSON file from each Tempo with the following format:
{
  "_id": {
    "$oid": "65ba7a61b6bdda7425622356"
  },
  "Nombre completo": "Natalia Rodríguez Rodríguez",
  "Nombre de usuario": "nataliaror",
  "Período": {
    "$numberInt": "523"
  },
  "Registros": [
    {
      "Order": {
        "$numberInt": "13852846"
      },
      "Fecha de trabajo": {
        "$numberLong": "1685059200000"
      },
      "Clave de Proyecto": "BACINTTIEN",
      "Horas": {
        "$numberDouble": "6.0"
      },
      "Horas facturadas": {
        "$numberDouble": "6.0"
      }
    }
  ]
}
3. Persists JSON into MongoDB Atlas. Database "nunegal". Collection: "tempo"


