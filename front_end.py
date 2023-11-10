from random import choice
from colorama import init, Fore, Back, Style
import words_data
import time
init(autoreset=True)



print('=' * 26)
print('|' + ' ' * 24 +'|')
print('|' + ' ' * 2 + 'Bem vindo ao Palavro' + ' ' * 2 + '|')
print('|' + ' '*24 +'|')
print('=' * 26 + '\n')



while True:

    quant_letras = 5 #quantidade de letras fixas
    sanitized_words = words_data.filtra(quant_letras) 
    info_dic = words_data.inicializa(sanitized_words)
    tentativas = info_dic['tentativas']
    
    print('Comandos: desisto' + '\n')
    print(' ' + 'Regras:'+'\n')
    print('  - Você tem '+ Fore.RED + f'{tentativas}' + Fore.RESET + ' tentativas para acertar uma palavra aleatória de '+f'{quant_letras}' + ' letras.')
    print('  - A cada tentativa, a palavra testada terá suas letras coloridas conforme:')
    print('    ♦ ' + Fore.BLUE+'Azul' + Fore.RESET + '   : a letra está na posição correta.')
    print('    ♦ ' + Fore.YELLOW+'Amarelo' + Fore.RESET + ': a palavra tem a letra, mas está na posição errada.')
    print('    ♦ ' + Fore.BLACK+'Preto' + Fore.RESET + '  : a palavra não tem a letra.')
    print('  - Os acentos são ignorados.')
    print('  - As palavras podem possuir letras repetidas.' + '\n')
    print('Sorteando uma palavra...\n')
    time.sleep(2)
    sorteada = info_dic['sorteada']
    print('Já tenho uma palavra! Tente adivinhá-la!')

    print(sorteada)

        
    def jogo(palpite):
        while True:
            
            retorno = ''

            cores = words_data.inidica_posicao(sorteada,palpite)
            for i in range(len(palpite)):
                if cores[i] == 0:
                    retorno += Fore.BLUE + palpite[i] + Fore.RESET
                elif cores[i] == 1:
                    retorno += Fore.YELLOW +  palpite[i] + Fore.RESET
                else:
                    retorno += Fore.BLACK + palpite[i] + Fore.RESET
            print(retorno)
            
            return retorno
            
            
    while True:
        if tentativas == 0:
            print('Você perdeu! ')
            break
        print('Voce tem {0} tentativas!'.format(tentativas))
        palpite = input('Qual o seu palpite? ').strip().lower()
        if palpite.lower() == 'desisto':
            break
        if len(palpite) != int(quant_letras):
            print('Somente palavras de {0} letras'.format(quant_letras))
        elif palpite not in words_data.PALAVRAS:
            print('Palavra desconhecida.')
        else:
            retorno = jogo(palpite)
            if palpite == sorteada:
                print('Você ganhou!')
                break
            tentativas -= 1
            
            

    rejogar = input('Deseja jogar novamente? (s/n): ').strip().lower()

    if rejogar in ['s','sim','claro']:
        continue
    else:
        print('Ate mais!')
        break

