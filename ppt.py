'''
Jogo do Pedra-Papel-Tesoura
2024.08.13
Gabriel Borba
'''

# Bibliotecas
from modules import clrScreen, displayHeader, getUserOption, validateUserOption, displayLine, displayMsg, displayMsgCenter, displayHeaderT # funçoes exportadas dos outros arquivos do nosso codigo, como os modules.py
from random import randint
from time import sleep

# Constantes, Variáveis e Listas
msgsInicio = ['Seja bem vindo ao', 'Jogo do PEDRA-PAPEL-TESOURA', ' desenvolvido por: Gabriel Borba', 'BOA SORTE!'] # Mensagem mostradada no inicio do jogo
msgs = []
playAgain = '' # Aqui a variavel e definida como "nada" mas durante o codigo ela vai assumir um "valor"
playerScore = 0
computerScore = 0





# Funções
def startPPT(): # Funçao utilizada para iniciar o jogo e rodar as demais funçoes
  while(True): # Enquanto a resposta do usuario for verdadeira:
    clrScreen() # Funçao utilizada para limpar a tela, deixa-la em branco
    displayHeader(msgsInicio) # Utilizado para mostrar a "msgsInicio" de forma organizada
    playPPT()
    # Função pra começar o jogo
    playAgain = getUserOption('Deseja jogar novamente [s/n]') # A variavel "playAgain" recebe o valor de verdadeiro ou falso da funçao "getUserOption" para usa-la durante o codigo
    while not validateUserOption(playAgain, ['s', 'n', 'S', 'N']): # Enquanto a opçao do usuario for falsa pegar a opçao do usuario
      playAgain = getUserOption('Deseja jogar novamente [s/n]') # A variavel "playAgain" recebe as mesmas instruçoes da funçao "getUserOption" e assim executa essas instruçoes durante este codigo
    if playAgain.lower() != 's': # Caso a nossa resposta seja diferente de s:
      break # Quebre o codigo aqui, isso faz com que ele pare de ser executado
      
    

def displayMenu():
    msgs = ['Escolha:',
           '[0] --> Pedra',
           '[1] --> Papel',
           '[2] --> Tesoura']
    displayLine()
    for msg in msgs:
      displayMsg(msg)
    displayLine()



def displayScore(typeScore, playerScore, computerScore):
  msgs = []
  msgs.append(typeScore)
  msgs.append(f'Player: {playerScore} --- PC: {computerScore}')
  displayHeaderT(msgs)
  
def determineWinner(playerChoice, computerChoice):
  play = ''
  result = ''
  choices = ['PEDRA', 'PAPEL', 'TESOURA']
  playerChoiceStr = choices[int(playerChoice)]
  computerChoiceStr = choices[int(computerChoice)]
  if playerChoice == computerChoice:
    result = 'Empate!'
  elif (playerChoice == '0' and computerChoice == '2') or (playerChoice == '1' and computerChoice == '0') or ( playerChoice =='2' and computerChoice == '1'):
    play = f"{playerChoiceStr} vence {computerChoiceStr}"
    result = 'Você Ganhou!'
  else:
    play = f"{computerChoiceStr} vence {playerChoiceStr}"
    result = 'Você Perdeu!'
  msgs = ['Jogada do Player: ' + playerChoiceStr, 'Jogada do PC: ' + computerChoiceStr, play, result]
  displayHeaderT(msgs)
  return result
  
def playPPT():
  playerScore = 0
  computerScore = 0
  while playerScore < 2 and computerScore < 2:
    displayMenu()
    playerChoice = getUserOption('Sua escolha')
    while not validateUserOption(playerChoice, ['0','1','2']):
      displayMenu()
      playerChoice = getUserOption('Sua escolha')
    computerChoice = str(randint(0,2))
    result = determineWinner(playerChoice, computerChoice)
    if "Ganhou" in result:
      playerScore += 1
    elif "Perdeu" in result:
      computerScore += 1
    if playerScore < 2 and computerScore < 2:
        displayScore("PLACAR", playerScore, computerScore)
        sleep(1)
  displayScore("PLACAR FINAL", playerScore, computerScore)
  if playerScore > computerScore:
    displayHeader(['Parabéns','YOU WIN!'])
  else:
    displayHeader(['Parabéns', 'YOU LOSE!'])
  
# Main