# Sistema de Monitoramento de Qualidade da Água em Tempo Real

Este projeto utiliza um **Arduino** com sensor de pH e turbidez para monitorar a qualidade da água em tempo real. Os dados do sensor são enviados para um **script Python**, que armazena as leituras em um banco de dados MySQL. Um **servidor Flask** exibe os dados em uma página web.

## Componentes Utilizados
- **Arduino Uno** ou similar
- **Sensor de pH**
- **Sensor de Turbidez** (ex.: SEN0189)
- **Protoboard e Jumpers**
- **LEDs** para indicação visual de valores de pH e turbidez
- **Resistores**
- **Cabo USB** para conexão do Arduino ao computador
- **Computador** com Python, Flask e MySQL instalados

## Funcionalidades
- Monitoramento contínuo do pH e da turbidez da água.
- Exibição dos dados em tempo real em uma página web.
- Armazenamento das leituras no banco de dados MySQL.
- Interface web com cores indicativas da qualidade da água.

## Instruções de Uso

### 1. Configuração do Arduino

1. Conecte os **sensores de pH** e **turbidez** ao Arduino conforme as portas especificadas no código `turbidez_ph_monitor.ino`:
   - Sensor de pH → Porta A0
   - Sensor de Turbidez → Porta A1
   - LEDs para visualização dos valores

2. Faça o upload do código `turbidez_ph_monitor.ino` para o Arduino. O código lê os valores dos sensores e envia os dados pela porta serial para o computador.

### 2. Configuração do Ambiente Python

1. Certifique-se de ter o **Python 3.x** instalado.
   
3. Instale as dependências necessárias:
   ```bash
   pip install flask mysql-connector-python pyserial

4. Configure o banco de dados MySQL:
    - Crie um banco de dados chamado banco_agua.
    - Crie uma tabela dados com as colunas ph, turbidez e data_hora.
      
5. Execute o script Python serial_to_mysql.py para começar a coletar dados da porta serial e armazená-los no banco de dados:
   ```
   python3 python_script/serial_to_mysql.py
   ```

### 3. Executando a Aplicação Flask

1. Na pasta web_app, execute o servidor Flask:
   ```
   python3 app.py
   ```

## Futuras Melhorias
- Adicionar gráficos para monitorar a evolução dos dados ao longo do tempo.
- Implementar um sistema de alertas para avisar quando a qualidade da água estiver fora dos padrões.
- Permitir a configuração de limites de pH e turbidez diretamente pela interface web.

Abra o navegador e acesse http://localhost:3000 para visualizar os dados da qualidade da água em tempo real.

![Imagem do WhatsApp de 2024-10-19 à(s) 14 54 41_eb9a7f46](https://github.com/user-attachments/assets/5d52a9f5-32bc-4558-aa1e-058f1a1dff60)

![Imagem do WhatsApp de 2024-10-19 à(s) 14 56 04_6231089d](https://github.com/user-attachments/assets/be55e139-fe1c-475e-bafb-8c68390edbac)



