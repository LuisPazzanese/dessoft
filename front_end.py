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
    try:
        global valor_numerico
        quant_letras = input('Quantas letras voce deseja que a palavra tenha? ')
        valor_numerico = int(quant_letras)
        break
    except ValueError:
        print("O valor digitado não é numérico. Por favor, tente novamente.")


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
time.sleep(1)
sorteada = info_dic['sorteada']
print('Já tenho uma palavra! Tente adivinhá-la!')


