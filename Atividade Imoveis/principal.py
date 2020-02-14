import Imovel 
I = Imovel.Imovel(200,"906 sul",200,300)

print(I.__str__(),':' , I.calcularValor() )

I = Imovel.ImovelDeLuxo(300,"204 sul",200,300,2)

print(I.__str__(),':' , I.calcularValor() )
