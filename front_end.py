from words_data import sanitized_words
from random import choice
from words_data import info_dic
from colorama import init, Fore, Back, Style
init(autoreset=True)

sorteada = info_dic['sorteada']
tentativas = info_dic['tentativas']

print('=' * 26)
print('|' + ' ' * 24 +'|')
print('|' + ' ' * 2 + 'Bem vindo ao Palavro' + ' ' * 2 + '|')
print('|' + ' '*24 +'|')
print('=' * 26 + '\n')

print('Comandos: desisto' + '\n')
print(' ' + 'Regras:')
print('  - Você tem '+ Fore.RED + f'{tentativas}' + Fore.RESET + ' tentativas para acertar uma palavra aleatória de 5 letras.')
print('  - A cada tentativa, a palavra testada terá suas letras coloridas conforme:')
print('    ♦ ' + Fore.BLUE+'Azul' + Fore.RESET + '   : a letra está na posição correta.')
print('    ♦ ' + Fore.YELLOW+'Amarelo' + Fore.RESET + ': a palavra tem a letra, mas está na posição errada.')
print('    ♦ ' + Fore.BLACK+'Preto' + Fore.RESET + '  : a palavra não tem a letra.')
print('  - Os acentos são ignorados.')
print('  - As palavras podem possuir letras repetidas.')
