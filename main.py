from deep_translator import GoogleTranslator
import os
import time

def menu():
    print('\n1 - Traduzir texto')
    print('2 - Sair\n')

def menu_idioma():
    print('Para qual idioma gostaria a tradução')
    print('1 - Português')
    print('2 - Inglês')
    print('3 - Espanhol')


while True:
    menu()
    opcao = str(input('Digite a opção: '))
    
    match opcao:
        case '1':
            menu_idioma()
            opcao_idioma = int(input('\nEscolha opcao de idioma: '))
            idioma_escolhido=[]
                        
            if opcao_idioma == 1:
                idioma_escolhido.append('portuguese')
            elif opcao_idioma == 2:
                idioma_escolhido.append('english')
            elif opcao_idioma == 3:
                idioma_escolhido.append('spanish')
            elif opcao_idioma !=1 and opcao_idioma !=2 and opcao_idioma !=3:
                print('\nComo você digitou a opção diferente,\n automaticamente irá traduzipara português.')
                idioma_escolhido.append('portuguese')
            else:
                print('Opção invalida') 
                       
            text = str(input('Digite o texto a ser traduzido: '))
            translated = GoogleTranslator(source='auto', target=idioma_escolhido[0]).translate(text=text)
            print(f'\n{translated}')
            
            continue
        case '2':
            print('Saindo...')
            time.sleep(3)
            os.system('cls')
            break
        case _:
            print(" Opção invalida")
            continue
