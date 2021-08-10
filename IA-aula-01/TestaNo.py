from No import No
from Estado import Estado

estadoInicial = Estado('/home/ec2-user/environment/DiretorioInicial')
raiz = No(estadoInicial)

estadosFilhos = estadoInicial.funcaoSucessora()
for estadoFilho in estadosFilhos:
    noFilho = No(Estado(estadoFilho))
    raiz.addFilho(noFilho)
    
raiz.printArvore()
