
def regras():
    print('=-'*20)
    print('As Regras são muito simples:')
    print('''
    Para o desafiador:
    - Escolha uma palavra apenas
    - Não utilize acentos
    
    Para o(s) desafiado(s):
    - Escolha apenas uma letra por vez
    - Não utilize acentos

    Ultima regra se divirtam
    ''') 
    print('=-'*20)   
    print('''
        |--------
        |       |
        |     
        | 
        |
        |
    ____|_____
    ''')




def q_erros(erros):
    if erros == 0 or erros == None:
        print('''
        |--------
        |       |
        |       
        | 
        |
        |
    ____|_____
    ''')
    elif erros == 1:
        print('''
        |--------
        |       |
        |       O
        | 
        |
        |
    ____|_____
    ''')
    elif erros == 2:
        print('''
        |--------
        |       |
        |       O
        |       |
        |
        |
    ____|_____
    ''')
    elif erros == 3:
        print('''
        |--------
        |       |
        |       O
        |      /|
        |
        |
    ____|_____
    ''')
    elif erros == 4:
        print('''
        |--------
        |       |
        |       O
        |      /|\\
        |
        |
    ____|_____
    ''')
    elif erros == 5:
        print('''
        |--------
        |       |
        |       O
        |      /|\\
        |      /
        |
    ____|_____
    ''')
    elif erros == 6:
        print('''
        |--------
        |       |
        |       O
        |      /|\\      /_O_/  /_O_/
        |      / \\        |      |
        |                 //     //
    ____|_____           
    ''')
        print('Jogo acabou o vencedor foi o desafiante')

    
    