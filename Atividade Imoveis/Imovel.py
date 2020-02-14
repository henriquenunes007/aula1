class Imovel():
    def __init__(self,cod,endereco,tamanho,valorMetro):
        self.cod = cod
        self.endereco = endereco
        self.tamanho = tamanho
        self.valorMetro = valorMetro
    def __str__(self):
        return self.cod
    
    def calcularValor(self):
        return self.tamanho * self.valorMetro
    
        
    
class ImovelDeLuxo(Imovel):
    def __init__(self,cod,endereco,tamanho,valorMetro,adicional):
        Imovel.__init__(self,cod,endereco,tamanho,valorMetro)
        self.adicional = adicional
    def __str__(self):
        return u'{}  {}  {}  {}  {}'.format(self.cod,self.endereco
                ,self.tamanho,self.valorMetro,self.adicional)
    
    def calcularValor(self):
        
        valor = super().calcularValor()
        
        return (valor + ((valor*self.adicional)/100))
    
'''a = Imovel(200,"906 sul",20,40)
b = ImovelDeLuxo(300,"204 sul",20,40,2)

print("Valor Imovel ", a.__str__() , " : " , a.calcularValor())
print("\n")
print("Valor Imovel de Luxo ", b.__str__(), " : " , b.calcularValor())
'''
