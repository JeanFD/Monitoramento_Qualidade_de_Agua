from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

db_config = {
  'user':'agua',
  'password':'arduino123',
  'host':'127.0.0.1',
  'database':'banco_agua'
}

def obter_dados():
    try:
      cnx = mysql.connector.connect(**db_config)
      cursor = cnx.cursor()
      query = "SELECT * FROM dados ORDER BY dados.data_hora DESC LIMIT 1"
      cursor.execute(query)
      dados = cursor.fetchone()
      cursor.close()
      cnx.close()
      return dados
    except mysql.connector.Error as err:
      print(f"Erro ao acessar o banco de dados: {err}")
      return None
      
@app.route('/')
def exibir_dados():
    dados = obter_dados()
    
    if dados:
      ph, turbidez, data = dados
      ph=float(ph)
      turbidez=float(turbidez)

      if 6.5 <= ph <= 8.5 and turbidez < 1500:
          mensagem = "Água Potável"
          cor = "#38CCCC"
      elif turbidez >= 1500:
          mensagem = "Água amarelada"
          cor = "#F96699"
      elif ph < 6.5:
          mensagem = "Ph abaixo do recomendado"
          cor = "#F96699"
      elif ph > 8.5:
          mensagem = "Ph acima do recomendado"
          cor = "#F96699"
    else:
        mensagem = "Dados não disponíveis"
        ph="--//--"
        turbidez="--//--"
        data="--//--"
        cor = "gray"

    return render_template('index.html', ph=ph, turbidez=turbidez, data=data,\
 mensagem=mensagem, cor=cor)

if __name__ == '__main__':
    app.run(debug=True, port="3000")

    