from random import randint
def vez(jogadores_desafiados):
    vez_definida = False
    for index, jogador in enumerate(jogadores_desafiados):
        if jogador.get('vez') != None:
            vez_definida = True
            if jogador.get('vez') == True:
                jogador['vez'] = False
                if len(jogadores_desafiados) == index + 1:
                    jogadores_desafiados[0]['vez'] = True
                else:    
                    jogadores_desafiados[index + 1]['vez'] = True
                break
    if not vez_definida:
        posicao = randint(0, len(jogadores_desafiados) - 1)
        jogadores_desafiados[posicao]['vez'] = True
    return jogadores_desafiados


    