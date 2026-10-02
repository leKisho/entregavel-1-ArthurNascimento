



def verificaMissao(bateria, duracao_missao, consumo_por_minuto):

    consumo_total = duracao_missao * consumo_por_minuto
    bateria_final = bateria - consumo_total

    
    if consumo_total > 100:
        print("\n\n\n\nO consumo total da missão é maior que 100%% da bateria. Impossivel realizar."
            "\nOtimize a missão ou reduza o consumo."
            "\nBateria disponível: %d%%"
            "\nConsumo total: %.2f%%\n"%(bateria, consumo_total))
    
    elif bateria_final < 0: 
        print("\n\n\n\nA bateria não é suficiente para a duração da missão e o consumo informado.\
            \nCarregue a bateria ou otimize a missao.\
            \nBateria necessária: %.2f%%\
            \nBateria disponível: %d%%\
            \nConsumo total: %.2f%%\n"%(-bateria_final, bateria, consumo_total))

    else:
        print("A bateria é suficiente para finalizar a missão.\
            \nBateria final após a missão: ", bateria_final)


    print("\nVerificacao finalizada.\n")
    input("Pressione Enter ou Ctrl+C para sair do programa...")


def main():

    bateria: int
    consumo_por_minuto: float
    duracao_missao: float


    bateria = int(input("Insira o nivel de bateria (% de 0 a 100): "))
    if  bateria < 0 or bateria > 100:
        print("Valor de bateria invalido.")
        return -1

    duracao_missao = float(input("Insira a duracao da missão, em minutos: "))
    if duracao_missao <= 0:
        print("Valor de duracao da missão invalido.")
        return -2
    
    consumo_por_minuto = float(input("Insira o consumo por minuto (em %): "))
    if consumo_por_minuto <= 0:
        print("Valor de consumo invalido.")
        return -3

    verificaMissao(bateria, duracao_missao, consumo_por_minuto)

    return 0

if __name__ == "__main__":
    main()