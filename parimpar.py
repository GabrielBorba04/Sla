'''
Jogo do Pedra-Papel-Tesoura
2024.08.20
Gabriel Borba
'''

# Bibliotecas
from modules import clrScreen, displayHeader, getUserOption, validateUserOption, displayLine, displayMsg, displayMsgCenter, displayHeaderT # funçoes exportadas dos outros arquivos do nosso codigo, como os modules.py
from random import randint
from time import sleep

# Constantes, Variáveis e Listas
msgsInicio = ['Seja bem vindo ao', 'Jogo do PEDRA-PAPEL-TESOURA', ' desenvolvido por: Gabriel Borba', 'BOA SORTE!'] # Mensagem mostradada no inicio do jogo
msgs = [] # Lista para armazenar mensagens temporarias
playAgain = '' # Aqui a variavel e definida como "nada" mas durante o codigo ela vai assumir um "valor"
playerScore = 0 # Variaveis utilizadas para armezenar a pontuaçao do jogador e do computador
computerScore = 0





# Funções
def startParImpar(): # Funçao utilizada para iniciar o jogo e rodar as demais funçoes
  while(True): # Enquanto a resposta do usuario for verdadeira:
    clrScreen() # Funçao utilizada para limpar a tela, deixa-la em branco
    displayHeader(msgsInicio) # Utilizado para mostrar a "msgsInicio" de forma organizada
    playParImpar()
    # Função pra começar o jogo
    playAgain = getUserOption('Deseja jogar novamente [s/n]') # A variavel "playAgain" recebe o valor de verdadeiro ou falso da funçao "getUserOption" para usa-la durante o codigo
    while not validateUserOption(playAgain, ['s', 'n', 'S', 'N']): # Enquanto a opçao do usuario for falsa pegar a opçao do usuario
      playAgain = getUserOption('Deseja jogar novamente [s/n]') # A variavel "playAgain" recebe as mesmas instruçoes da funçao "getUserOption" e assim executa essas instruçoes durante este codigo
    if playAgain.lower() != 's': # Caso a nossa resposta seja diferente de s:
      break # Quebre o codigo aqui, isso faz com que ele pare de ser executado



def displayMenu():
    msgs = ['Escolha:', # Defini uma lista de mensagens para o jogador escolher se vai jogar pelo par ou pelo impar
           '[0] --> Par',
           '[1] --> Impar']
    displayLine() # linha para a estrutura
    for msg in msgs:
      displayMsg(msg) # Realmente mostra a mensagem
    displayLine()



def displayScore(typeScore, playerScore, computerScore): # Recebe o placar das duas pontuaçoes
  msgs = [] # cria uma lista para armazenalas
  msgs.append(typeScore)
  msgs.append(f'Player: {playerScore} --- PC: {computerScore}') # faz o placar das pontuaçoes
  displayHeaderT(msgs) # Mostra esse placar

def determineWinner(playerChoice, playerNumber, computerNumber):
  result = ''
  choices = ['Par', 'Impar']
  sumNumbers = playerNumber + computerNumber # soma os numeros colocados pelo jogador e pelo computador
  if (sumNumbers % 2 == 0 and playerChoice == '0') or (sumNumbers % 2 != 0 and playerChoice == 1): # verifica se a soma e impar ou par
    result = 'Você Ganhou!' # defini o resultado como voce ganhou
  else:
    result = 'Você Perdeu!' # Defini o resultado como vc perdeu
  msgs = [f'Numero do player: {playerNumber}', # prepara e exibi uma mensagem com os detalhes da jogada e o resultado
          f'Numero do PC: {computerNumber}',
          f'Soma: {sumNumbers}',
          result]
  displayHeaderT(msgs)
  return result

def playParImpar():
  global playerScore, computerScore
  playerScore = 0 # Inicializa as pontuaçoes do jogador e do computador
  computerScore = 0
  while playerScore < 2 and computerScore < 2: # Execua um loop ate q uma das pontuaçoes assuma dois pontos
    displayMenu()
    playerChoice = getUserOption('Sua escolha') # Exibi o menu de escolha e valida sua resposta
    while not validateUserOption(playerChoice, ['0','1']): 
      displayMenu()
      playerChoice = getUserOption('Sua escolha')
    playerNumber = int(getUserOption('Escolha um numero de 1 a 10'))
    while not validateUserOption(str(playerNumber), [str(i) for i in range(1,11)]):
      playerNumber = int(getUserOption('Escolha um numero de 1 a 10'))
    computerNumber = randint(1,10) # Gera um numero alatorio para o computador
    result = determineWinner(playerChoice, playerNumber, computerNumber) # Determina o vencedor e atualiza as pontuaçoes
    if "Ganhou" in result:
      playerScore += 1
    elif "Perdeu" in result:
      computerScore += 1
    if playerScore < 2 and computerScore < 2:
        displayScore("PLACAR", playerScore, computerScore) # Exibi o placar
        sleep(1)
  displayScore("PLACAR FINAL", playerScore, computerScore) # Exibi o placar final
  if playerScore > computerScore:
    displayHeader(['Parabéns','YOU WIN!'])
  else:
    displayHeader(['Parabéns', 'YOU LOSE!'])

# Main