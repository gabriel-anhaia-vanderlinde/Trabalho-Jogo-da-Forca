from arquivos.tela import entrada_de_dados, saida_de_dados
from arquivos.regras_jogo import regras
print('Bem vindo ao jogo da forca')
saida_de_dados.regras()
erros = 0
acertos = 0
letras_acertadas = []

jogadores = entrada_de_dados.q_jogadores_nomes()
jogardor_desafiador, jogadores_desafiados = entrada_de_dados.divisao_de_jogadores(jogadores)
print(f'O jogador {jogardor_desafiador} será o desafiador')

palavra = entrada_de_dados.palavra_chave()
saida_de_dados.q_erros(erros)


print(entrada_de_dados.palavra_escondida(palavra, letras_acertadas))
jogadores_desafiados = regras.vez(jogadores_desafiados)
print(jogadores_desafiados)
acertado = 0
while erros < 6:
    erros, letras_acertadas = entrada_de_dados.escolha_das_letras(jogadores_desafiados, palavra, erros, letras_acertadas)
    saida_de_dados.q_erros(erros)
    print(entrada_de_dados.palavra_escondida(palavra, letras_acertadas))
    acertado = entrada_de_dados.acerto_da_palavra(letras_acertadas, palavra)
    jogadores_desafiados = regras.vez(jogadores_desafiados)
    if acertado == len(palavra):
        print('Parabéns Acertaram a palavra')
        break