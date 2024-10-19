import serial
import mysql.connector
from datetime import datetime

cnx = mysql.connector.connect(
  user='agua',
  password='arduino123',
  host='127.0.0.1',
  database='banco_agua'
)

cursor = cnx.cursor()
add_sinais = "INSERT INTO dados (ph, turbidez, data_hora) VALUES (%s, %s, %s)"
#print(cursor.execute(verifica))

#configuração porta serial
comport = serial.Serial('COM9', 9600) 
print ('Serial Iniciada...\n')

while (True):
    serialValue = str(comport.readline())
    c1 = "b'"
    c2 = "\\r\\"
    for x in range(len(c1)):
        serialValue = serialValue.replace(c1[x], "")
        serialValue = serialValue.replace(c2[x], "")
    serialValue = serialValue.replace("n", "")
    data_sinais = serialValue.split("|")
    data_e_hora  = datetime.now()    
    data_e_hora_str = str(data_e_hora.strftime('%d/%m/%Y %H:%M:%S'))
    data_sinais.append(data_e_hora_str)

    cursor.execute(add_sinais, data_sinais)
    cnx.commit()
    print(data_sinais)

cursor.close()
cnx.close()