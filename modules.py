'''
Arquivo de Modulos
2024.08.13
Gabriel Borba
'''

# --> Bibliotecas
from random import choice # Importa o "choice" da blibioteca do Python, e usa ele para sortear qual vai ser o caracter utilizado para montar a estrutura do jogo
from time import sleep

# --> Constantes, Variáveis e Listas
TAM = 50 # Tamanho da Tela
CAR = choice(['=', '*', '|', '-']) # Caracter utilizado para desenho da tela
MAR = 4 # Tamanho da Margem

# --> Funções
def clrScreen(): # Função para limpar a tela
  print('\n'*TAM) # Mostra na tela \n == linha * TAM

def displayLine(): # Função para mostrar uma linha de caracteres
  print(CAR*TAM) # Mostra essa linha para formar a estrutura do jogo 

def displayMsg(msg): # Mostra uma msg alinhada a esquerda entre CAR
  print(f'{CAR} {msg:<{TAM-MAR}} {CAR}') # Mostra a respectiva mensagem de forma que esteja alinhada a esquerda

def displayMsgCenter(msg): # Funçao criada com o intuito de mostrar uma mensagem alinhada ao meio
  print(f'{CAR} {msg:^{TAM-MAR}} {CAR}') # Metodo utilizado para mostrar a mensagem no meio

def displayHeader(msgs): # Funçao para mostrar as mensagens de forma organizada 
  displayLine() # Usado para fazer a estrutura do jogo com os caracteres
  for item in msgs: # Enquanto "item" tiver mensagens repita:
    displayMsgCenter(item) # Usado para colocar as mensagens do "item" no centro
  displayLine() # Usado para fazer a estrutura do jogo com os caracteres

def displayHeaderT(msgs):
  displayLine()
  for item in msgs:
    displayMsgCenter(item)
    sleep(1)
  displayLine()




def getUserOption(msg): # Funçao utilizada para pegar a opçao do usu ario
  option = input(f'{CAR} {msg}: ').strip() # Pergunta ao usuario e pega sua resposta
  return option # Retorna a resposta do usuario

def validateUserOption(option, listOptions): # Funçao utilizada para validar a resposta do usuario
  if option in listOptions: # Verifica se a opçao do usuario e valida  
    return True # caso a opçao for valida retorna ela com o valor verdadeiro
  else: # Caso a resposta seja invalida:
    msgsErro = ['Opção Inválida!', 'Escolha Novamente...'] # Defini a mensagem que sera mostrada ao usuario
    displayHeader(msgsErro) # Mostra a "msgsErro" de forma organizada
    return False # Retorna o valor como falso
  
# --> main