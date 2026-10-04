# Entregável 1 - Aprendendo a ser um programador
#
# Programa para verificar se a bateria disponível é suficiente
# para realizar uma missão com duração e consumo informados.
#
# Autor: Arthur Nascimento
# Github.com/leKisho
# ============================================================


def verificaMissao(bateria, duracao_missao, consumo_por_minuto):

    consumo_total = duracao_missao * consumo_por_minuto #dado em %
    bateria_final = bateria - consumo_total #caso o valor seja negativo, a
                                            #missão não poderá ser realizada

    
    #caso o consumo seja maior que 100%, é impossível que a missão seja
    #realizada nas condições de duração e consumo informadas.
    if consumo_total > 100:
        print("\n\nO consumo total da missão é maior que 100%% da bateria. Impossivel realizar."
            "\nOtimize a missão ou reduza o consumo."
            "\nCarga necessária: +%.2f%%"
            "\nBateria disponível: %.2f%%"
            "\nConsumo total: %.2f%%\n"%(-bateria_final, bateria, consumo_total))
    
    elif bateria_final < 0: 
        print("\n\nA bateria não é suficiente para a duração da missão e o consumo informado.\
            \nCarregue a bateria ou otimize a missao.\
            \nCarga necessária: +%.2f%%\
            \nBateria disponível: %.2f%%\
            \nConsumo total: %.2f%%\n"%(-bateria_final, bateria, consumo_total))

    else:
        print("\n\nA bateria é suficiente para finalizar a missão.\
            \nBateria final após a missão: %.2f%% "%(bateria_final))


    print("\nVerificacao finalizada.\n")
    input("Pressione Enter ou Ctrl+C para sair do programa...")


def main():

    bateria: float
    consumo_por_minuto: float
    duracao_missao: float

    # O usuário informa a porcentagem da bateria, que deve estar
    #entre 0% e 100%
    bateria = float(input("Insira o nivel de bateria (% de 0 a 100): "))
    if  bateria < 0 or bateria > 100:
        print("Valor de bateria invalido.")
        return -1

    # O usuário fornece a duração da missão, em minutos
    duracao_missao = float(input("Insira a duracao da missão, em minutos: "))
    if duracao_missao <= 0:
        print("Valor de duracao da missão invalido.")
        return -2
    
    # O usuário fornece a consumo percentual por minuto
    consumo_por_minuto = float(input("Insira o consumo por minuto (em %): "))
    if consumo_por_minuto <= 0:
        print("Valor de consumo invalido.")
        return -3

    verificaMissao(bateria, duracao_missao, consumo_por_minuto)

    return 0

if __name__ == "__main__":
    main()
