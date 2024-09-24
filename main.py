'''
Projeto Jogo Pedra-Papel-Tesoura
2024.08.13
Gabriel Borba
'''


# --> Bibliotecas
# Importa a funções do arquivo modules.py
from modules import clrScreen, displayLine, displayMsg, displayMsgCenter, displayHeader, getUserOption, validateUserOption, displayHeaderT # Importa essas funçoes do nosso arquivo "modules"
from ppt import startPPT # Importa essa funçao do nosso arquivo "ppt"
from parimpar import startParImpar

# --> Constantes, Variáveis e Listas

# --> Funções

# --> Main
msgs = ['Sejam Bem-vindo aos Jogos', 'PEDRA-PAPEL-TESOURA', 'PAR OU ÍMPAR']
displayHeader(msgs)
msgs = ['Digite 0 --> Sair', 'Digite 1 --> Pedra-Papel-Tesoura', 'Digite 2 --> Par ou Ímpar']
displayHeaderT(msgs)
opUser = getUserOption('Sua escolha')
while not validateUserOption(opUser, ['0','1','2']):
  opUser = getUserOption('Sua escolha')
if(opUser == '1'):
  startPPT()
elif(opUser == '2'):
  startParImpar()
else:
  displayMsg('Até a Próxima...')

  
  
  
  
  # Funçao utilizada paa iniciar o jogo e que nesse caso esta realmente executando-o
