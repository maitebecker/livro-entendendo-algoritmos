estados_abranger = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"]) #lista dos estados que deseja abranger

estacoes = {} #lista de estações que podem ser escolhidas e os estados que elas abrangem
estacoes["kum"] = set(["id", "nv", "ut"])
estacoes["kdois"] = set(["wa", "id", "mt"])
estacoes["ktres"] = set(["or", "nv", "ca"])
estacoes["kcinco"] = set(["ca", "az"])

estacoes_final = set()

while estados_abranger:
    melhor_estacao = None
    estados_cobertos = set() #conjunto de todos os estados que essa estação abrange que ainda não foram cobertos
    for estacao, estados_por_estacao in estacoes.items():
        cobertos = estados_abranger & estados_por_estacao
        if len(cobertos) > len(estados_cobertos):
            melhor_estacao = estacao
            estados_cobertos = cobertos
    estados_abranger -= estados_cobertos
    estacoes_final.add(melhor_estacao)

print(estacoes_final) #{'ktres', 'kdois', 'kum', 'kcinco'}