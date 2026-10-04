# Entregável 1 — 2° Fase PS Harpia

# Autor: Arthur Nascimento
# Github.com/leKisho

Programa simpĺes desenvolvido em Python para verificar se a bateria disponível de um robô é suficiente para realizar uma missão.

## Objetivo

O programa requisita três informações do usuário:

- **Bateria atual:** nível de bateria disponível, em porcentagem (0 a 100).
- **Duração da missão:** tempo estimado para realizar a missão, em minutos.
- **Consumo por minuto:** porcentagem da bateria consumida por minuto.

A partir desses valores, o programa calcula o consumo total da missão e verifica se a bateria disponível é suficiente. É considerado suficiente se, ao final da missão, a bateria restante for maior ou igual a 0%.

Caso seja suficiente, o programa informa a bateria restante. Caso contrário, informa quanto de bateria está faltando e as informações atuais.

O programa também identifica quando o consumo total da missão ultrapassa 100% da capacidade da bateria.

## Execução

A partir da raiz do repositório, execute:

python3 src/missao.py

E siga as instruções do programa para inserir as informações.

## Exemplo de Execução

Ao inserir:
- Nível de bateria = 50%
- Duração da missão = 20 min
- Consumo percentual por minuto = 2% / min

O resultado do consumo total será 20*2 = 40%
Como esse resultado é **menor** que o nível de bateria, será informado que a missão poderá ser realizada.
