"""
Leia dois valores inteiros. A seguir, calcule o produto entre estes dois valores e atribua esta operação à variável PROD. A seguir mostre a variável PROD com mensagem correspondente.   

Entrada
O arquivo de entrada contém 2 valores inteiros.

Saída
Imprima a variável PROD conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade. Não esqueça de imprimir o fim de linha após o produto, caso contrário seu programa apresentará a mensagem: “Presentation Error”.
https://www.urionlinejudge.com.br/judge/pt/problems/view/1004


"""


def prod(x, y):
    PRODUTO = x * y
    return PRODUTO

def main():

    x = int(input())
    y = int(input())

    PRODUTO = prod(x, y)

    print("PROD = " + format(PRODUTO))
    
if __name__ == "__main__":
    main()
    