def verificar_revisao(ano_producao, codigo_motor, distancia_percorrida):
    if 1901 <= ano_producao <= 2000 and (codigo_motor == 100 or codigo_motor == 101):
        return True
    elif 2001 <= ano_producao <= 2020 and distancia_percorrida > 5000:
        return True
    elif ano_producao == 2021 and (codigo_motor == 200 or codigo_motor == 201) and distancia_percorrida > 200:
        return True
    else:
        return False
def main():
    ano_producao = int(input())
    codigo_motor = int(input())
    distancia_percorrida = float(input())
    precisa_revisao = verificar_revisao(ano_producao, codigo_motor, distancia_percorrida)
    if precisa_revisao:
        print("SIM")
    else:
        print("NAO")
main()