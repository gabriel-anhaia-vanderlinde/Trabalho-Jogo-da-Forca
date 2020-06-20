    
def q_jogadores_nomes(): 
    jogadores = []
    while True:
        n_jogadores = input('Informe o numero de jogadores: ')
        if n_jogadores.isnumeric():
            n_jogadores = int(n_jogadores)
            if n_jogadores >= 2:
                break
            else:
                print('Informe Quantos jogadores i~rao jogar no mínimo 2')
        else:
            print('Informe um Número!!!')

    for n in range(0, n_jogadores):
        jogador = {}
        jogador['nome'] = input('Informe o nome do jogador:')
        jogadores.append(jogador)
    return jogadores

def divisao_de_jogadores(jogadores):
    jogadores_desafiados = []
    while True:
        jogardor_desafiador = input('Informe quem será o jogador desafiador ? ')
        jogador_encontrado = False
        for jogador in jogadores:
            if jogador.get('nome') == jogardor_desafiador:
                jogador_encontrado = True
            else:
                jogadores_desafiados.append(jogador)
        if not jogador_encontrado:
            jogadores_desafiados.clear()
            print(f'Informe um desafiador dentre os seguintes jogadores: {nomes_jogadores(jogadores)}')
        else:
            break
    return jogardor_desafiador, jogadores_desafiados

def nomes_jogadores(jogadores):
    nomes = []
    for jogador in jogadores:
        nomes.append(jogador.get('nome'))
    return nomes

    


def palavra_chave():
    c_acento = True
    while c_acento:
        palavra = input('Informe uma palavra: ')
        if palavra.isalpha:
            c_acento = palavra_contem_acento(palavra)
            if c_acento:
                print('Informe uma palavra sem acento!!')
        else:
            print('Informe uma palavra valida!! ')
    return palavra

def palavra_contem_acento(palavra):
    contem_acento = False
    for i in palavra:
        if i in '-çãõàáèéìíòóùú':
            contem_acento = True
    return contem_acento


def palavra_escondida(palavra, letras_acertadas):
    resultado = ''
    for l in palavra:
        if l in letras_acertadas:
            resultado += l + ' '
        else:
            resultado += '_ '
    return resultado

def acerto_da_palavra(letras_acertadas, palavra):
    acertos = 0 
    for l in palavra:
        if l in letras_acertadas:
            acertos += 1
    return acertos
    


def escolha_das_letras(jogadores_desafiados, palavra_chave, erros, letras_acertadas):
    letras = []
    jogar = True
    while jogar:
        for jogador in jogadores_desafiados:
            jogador_no_momento = jogador.get('nome')
            if jogador.get('vez') == True :
                letra = input('informe uma letra:  ')
                if not letra in letras:
                    if len(letra) == 1: 
                        letras.append(letra)
                        if letra in palavra_chave:
                            print(f'O jogador {jogador_no_momento} acertou a letra!! ')
                            letras_acertadas.append(letra)
                            break
                        else:
                            print(f'O jogador {jogador_no_momento} errou!! ')
                            erros += 1
                            break
                    else:
                        print('Informe apenas uma letra!! ')
                else:
                    print('Digite uma letra que não foi usada ainda')
        jogar = False
        return erros, letras_acertadas


