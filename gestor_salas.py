#Etapas - cadastro das empresas de seus projetos
startups = {
    "nome": "flare solution",
    "etapa": "aceleração",
    "início": "abril de 2026"
}
projetos_ativos = ["app mobile", "signal foud"]

print("startup: ",startups["nome"],"fase",startups["etapa"])
print("projetos em andamentos: " ,projetos_ativos[0], "inicio:",startups["inicio"])

#etapa 2 - mapeamento de sala
#aula ocupada = 1 e sala livre = 0
salas = {
    [1,0],
    [0,1]
}
print("status da sala a1", salas[0][0])
print("status da sala a2", salas[0][1])
print("status da sala b1", salas[1][0])
print("status da sala b2", salas[1][1])
print("classificação de status: 1 = ocupada, 0 = livre")

#etapa 3 - leitura de dados operacionais
with open("Dados.csv", "r", encodig="utf-8") as arquivo:
    cabecalho = arquivo.readline()
    linha1 = arquivo.readline()
    linha2 = arquivo.readline()
    linha3 = arquivo.readline()
    linha4 = arquivo.readline()

print(cabecalho)
print(linha1)
print(linha2)
print(linha3)
print(linha4)