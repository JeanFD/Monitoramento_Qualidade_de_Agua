# Sistema de Monitoramento de Qualidade da Água em Tempo Real

Este projeto utiliza um **Arduino** e um **sensor de turbidez** para monitorar a qualidade da água em tempo real. Os dados do sensor são enviados pela porta serial para um **script Python**, que os processa e os envia para uma página web desenvolvida em **Flask**.

## Componentes Utilizados
- **Arduino Uno** ou similar
- **Sensor de Turbidez** (ex.: SEN0189)
- **Resistor** de 10kΩ (para o divisor de tensão)
- **Protoboard e Jumpers**
- **Cabo USB** para conexão do Arduino ao computador
- **Computador** com Python e Flask instalados

## Funcionalidades
- Monitoramento contínuo da turbidez da água.
- Exibição dos dados em tempo real em uma página web.
- Interface web amigável para visualização dos dados históricos.

## Estrutura do Projeto

