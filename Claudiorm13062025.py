# print("Boa noite")
# print(5+10)
# print((5+10)/3)
# print(7 | 5)
# print(~10)
# print(~33)
# print(~9)
# print(~3)
# a=2
# b=3
# if a==b:
#     print("sim")
# elif(a!=b):
#     print("não")
# else:
#     print("Fim")
    # print("Boa noite")
# print(5+10)
# print((5+10)/3)
# print(7 | 5)
# print(~10)
# print(~33)
# print(~9)
# print(~3)
# a=2
# b=3
# if a==b:
#     print("sim")
# elif(a!=b):
#     print("não")
# else:
#     print("Fim")
# git clone \\caminho\ para copiar um arquivo
# git add .   
# git commit -m "Comentario"
# git push
# _nome = 'Jr'
# nome ='jr'
# nome2 = 'jr'
# nome_2 = 'jr'
# calculo = 5 ** 25 /2 - 2 + 10
# calculo1 = 10** 2 + 3
# print(calculo)
# print(calculo1)
# idade = int(input(' >> ')) # tipo texto
# tipo =  type(idade) 
# print(idade, tipo)
# idade =  float(input('2'))
# idade2 = float(input('3'))
# print("boa noite")

# Exrecicio 1
# nota1 =int(input("primeira nota"))
# print("Coloque a primeira nota")
# nota2 =int(input("segunda nota"))
# print("Coloque a segunda nota")
# nota3 =int(input("primeira nota"))
# print("Coloque a primeira nota")
# print((nota1+nota2+nota3)/3)
# media =((nota1+nota2+nota3)/3)
# if media >7:
#     print("Passou")
# else :
#     print("Reprovado")

# Exercicio 2
# IMC = peso / altura.2
# peso =int(input("Informe o peso"))
# print("coloque o peso")
# altura =int(input("Informe a altura"))
# print("Informe a altura")
# print(((altura*2) / peso))

# Exercicio 3
# print("* Seja bem vindo  *")
# valorcompra= float(input('Informe o valor da compra: '))
# desconto= 0.50
# print("desconto")
# valorfinal= float(valorcompra-(valorcompra*desconto))
# if valorcompra > 100:
#     print('Valor com desconto de: ', valorfinal)
# else:
#         print('Valor sem desconto: ', valorcompra)
# ValorDesconto = (valorcompra*desconto)
# print("Volte sempre")

# Exercicio 4
# print(" Papel Pedra Tesoura")
# Pedra= "Pedra"
# Tesoura= "tesoura"
# Papel= "papel"
# X = (input("papel pedra ou tesoura"))
# Y = (input("papel pedra ou tesoura"))
# if X == "papel" and Y == "pedra":
#     print("papel ganha")
# elif X == "papel" and Y == "papel":
#     print("empate")
# elif X == "papel" and Y == "tesoura":
#     print("tesoura ganha")
# elif X == "tesoura" and Y == "pedra":
#     print("pedra ganha")
# elif X == "tesoura" and Y == "tesoura":
#     print("empate")
# elif X == "tesoura" and Y == "papel":
#     print("papel ganha")
# elif X == "pedra" and Y == "papel":
#     print("papel ganha")
# elif X == "pedra" and Y == "tesoura":
#     print("pedra ganha")
# elif X == "pedra" and Y == "pedra":
#     print("empate")

# Exercicio 5
# a = int(input("escolher de 0 a 9"))

# match a:
#     case 1:
#         print("impar")
#     case 3:
#         print("impar")
#     case 5:
#         print("impar")
#     case 7:
#         print("impar")
#     case 9:
#         print("impar")
#     case 0:
#         print("par")
#     case 2:
#         print("par")
#     case 4:
#         print("par")
#     case 6:
#         print("par")
#     case 8:
#         print("par")




# a = int(input("escolher 1,2,3:"))


# match a:
#     case 1:
#         print("voce escolheu um")
#     case 2:
#         print("voce escolheu dois")
#     case 3:
#         print("voce escolheu tres")
#     case _:
#         print("opção errada")

# git commit - m "Salvar"

# a = int(input("Digite o dia da semana 1,2,3,4,5,6,7:"))

# match a:
#     case 1:
#          print("segunda")
#     case 2:
#         print("terça")
#     case 3:
#         print("quarta")
#     case 4:
#         print("quinta")
#     case 5:
#         print("sexta")
#     case 6:
#         print("sabado")
#     case 7:
#         print("domingo")

# contador = 0
# fim=100
# while contador < fim :
#     print(contador)
#     #se contador % 2==0:
#     print("")
#     #senão:
#     print("") 

    # contador += 1

# contador = 0
# fim=100
# while contador < fim :
#     print(contador)
#     #se contador % 2==0:
#     print("")
#     #senão:
#     print("") 
    

#     contador += 1


# for com range()  repetição com numeros 
# esse é o mais comun para contagem:
# a = range(0,5)
# print(a)

# # 1° inicio
# # 2° fim
# # 3° contador 
# sacola_de_feira = ("maça", "laranja", "abacate", "banana")
# for i in sacola_de_feira:   
#    print(i)

# sacola_de_feira = ("1°","2°","3°","4°","5°")
# for i in sacola_de_feira:   
#    print(i)
# j=1
# sacola_de_feira = ["maça","banana","abacate","kiwi","melancia","cachorro", "papagaioa","teste"]
# sacola_de_feira.sort()# (sort.()) faz a lista em ordem alfabética 
# for i in sacola_de_feira:   
#    print("item n°"+str(j)+" = "+str(i))  
#    j+=1 


# Tupla 
# imutável
# a =(1,2,3,4,5,6,7,8,9)
# print(a) # busca o conjunto 

# for item in a: # busca item por item 
#     print(item)

# frutas = ("maça","bamana","uva","laranja")
# for i, frutas in enumerate(frutas):
#     print(f"{i}: {frutas}")

# nome = ("ana", "Paulo", "Claudio",)
# sobrenome = ("silva","souza","pereira")
# idade = (10,20,30)

# for nome, sobrenome, idade, \
#     in zip(nome,sobrenome,idade,): 
#     print(f"{nome} {sobrenome} tem  {idade} ")

# dados = {1:"ana",2: "paulo",3: "Claudio"}
# for  chave in (dados):
#     print(chave)

# for valor in dados.values():
#     print(valor)

# for chave, valor in dados.items():
#     print(f"{chave} - {valor} :)")

# lista = [0,1,2,3,4]

# dicionario = {1:"a" , 2:"b", 3:"c", 4:"d"}

# quadrados = [x for x in range(0,500,10)]

# quadrados = [(r,a) for r,a in dicionario.items()]
# print( quadrados)
# print (dicionario)

# print("ola")

# X=15
# Y=0
# for T in range(X,Y+1):
#     print(T)

# x=15
# y=0
# t=3
# for t in range (y,x+1,t):
#     print(t)

# x=15
# y=0
# t=3
# for t in range (15+1):
#     print(t)

# x=[15,1,2,5,10,17]
# for i in x:
#     print(i)

# salada_de_fruta=("banana","uva","laranja","melão")
# for i in salada_de_fruta:
#     print(i)

# salada_de_fruta=("banana,uva","laranja,melão")
# for i in salada_de_fruta:
#     print(i)

# salada_de_fruta=("banana","uva","laranja","melão")
# for i in enumerate(salada_de_fruta):
#     print(i)

# salada_de_fruta=("banana","uva","laranja","melão")
# for i in reversed(salada_de_fruta):
#     print(i)

# salada_de_fruta=("banana","uva","laranja","melão")
# etiqueta=[1,2,3,4]
# cor=("preto","amarelo","vermelho","branco")
# for i,j,l in zip(salada_de_fruta,etiqueta,cor):
#     print(i,j,l)

# Exercicio 1
# a=201
# b=0
# for num in range(0,201,11):
#     if num % 2==0:
#       print(num)

# # Exercicio 2
# Animais=("gato","cachorro","pássaro","tigre")
# Frase=("Animal","Aminal","Animal","Animal")
# for i,j in zip(Frase,Animais):
#     print(i,j)

# # #Exercicio 3
# Nomes=("Ana", "Bruno", "Carlos")
# for i in reversed(Nomes):
#     print(i)

# # Exercio 4
# produtos= ["Arroz","Feijão","cafe","leite"]
# preço=[5.20, 4.50, 4.57,5.3]
# for i,j in zip(produtos,preço):
#     print(i,j)

# #Exercio 5
# Frase="Python é a melhor linguagem do mundo"
# for i in zip(Frase):
#     print(i)

# produtos=("Arroz","Feijão","Cafe", "Leite")
# preços = ( 5.20,  4.50,  4.57,  5.3)
# real=("R$", "R$","R$","R$")
# qualidade= ("alta", "média", "baixa","sub")          
# for i,a,j,t in zip (produtos,real,preços, qualidade,):
#      print(f"{i:<100}, {a:<1} , {j:<5},{t:<5}")    #i:<100 é oespasamento

# a=3
# def imprimir():
#      a=4
#      print(a)

# imprimir()
# print(a)

# a=3
# b=4
# def soma (a,b):
#      c =a+b
#      print(c)

# def  subtracao (a,b):
#      c=a-b
#      print(c)

# def  multiplicacao (a,b):
#      c=a*b
#      print(c)
#      return c

# def  divisao (a,b):
#      c=a/b
#      print(c)


# resultado=multiplicacao(a,b)
# print(resultado)

# Exercicio2 Use input() para receber os horários de entrada e saída. Calcule as horas
# trabalhadas e diga se bateu a carga horária mínima (8h).


# Entrada =int(input("Entrada"))
# print("Digite a hora de entrada")
# Saida =int(input("Saida"))
# print("Digite a hora de saida")
# print(Saida-Entrada)
# media =()
# if media >8:
#     print("Bateu")
# else :
#     print("Nao bateu")

# print(((10+5)+(20-10))/5)

# Variavel e um espaço na memoria
# [0.1.2] lista tambem aloca um espaço na memoria  começa sempre no zero
# append  extend copy clear +=
# dicionario  

# apend adiciona um dado por vez
# extend adciona varias dados por vez []
# += ()
# insert

# variaveis 


# nome  =  10
# nome   = 'texto'

# # lista 

# lista  =  ['a','b','c']

# print(lista[0])

# print(dir(lista))

# # funções para alterar a lista

# # append(+ adicionar algoa a lista) -  extend  -  =+  clear 
# # del remove pop insert

# # APPEND ADIOCINAR 1  DADO POR VEZ

# lista  =  []

# print(lista)

# nome1 =  input('nome')
# nome2 =  input('nome')
# nome3 =  input('nome')


# lista.append(nome1)
# lista.append(nome2)
# lista.append(nome3)


# print('LISTA 1', lista)


# lista2 = []


# EXTEND ADICIONA VÁRIOS DADOS DE UMA VEZ 


# lista2.extend([nome1,nome2,nome3])

# pop -  del -  remove


# lista  =  ['a',20,30, 40, 50]
# del lista[0]
# print(lista)



# lista.remove(50)
# print(lista)


# lista.pop()
# lista.pop(0)
# print(lista)


# l = list(range(1,20))

# if 15 in l:
#     l.insert(0,11)

# print(l)

#  dicionario {}

# lista_chaves = []
# lista_valores = []


# dic  =  {
# 'idade':[25,20,30],
# 'endereço':[],
# 'email':'@gmail'
# }


# dic['endereço'].append('Rua 20')
# dic['endereço'].append('Rua 30')
# print(dic)


# for chave,valores in dic.items():
#     lista_chaves.append(chave)
#     lista_valores.append(valores)



# print(lista_chaves, lista_valores)

# for variavel in range(0,11):

#     print(variavel)

# e-commerce

# # cadastrar

# dados = {}
# print('CAdastre-se: ')
# email = input('E-mail: ')
# senha = input('senha: ')

# dados['e-mail'] = email
# dados['senha'] = senha

# # acesso ao sistema

# print('-----||------||-------||-------')
# print('Seja bem vindo(a) ao e-commerce ZZZ')
# print('Acesse a aplicação')

# chances = 3

# carrinho = []
# meu_total = []
# lista_prod = ['','pipoca','arroz','milho','quentão']
# valor_prod = ['',2.0,10.0,20.0,15.50]

# while chances > 0:
#     email_acesso = input('Digite seu e-mail')
#     senha_acesso = input('Digite sua senha')

#     if email_acesso == dados['e-mail'] and senha_acesso == dados['senha']:
#         print('Sejam bem vindo a sua conta ')
#         acesso  = input('Deseja pedir? s/n')
#         print(lista_prod)
#         # escolher produto
#         while acesso == 's':
#             pedido = int(input('Digite o ID do produto 1 -2 -3 -4')) 
#             carrinho.append(lista_prod[pedido])
#             meu_total .append(valor_prod[pedido])
#             print(carrinho)
#             soma =  sum(meu_total)
#             print('R$',soma)
#             acesso  = input('Deseja pedir? s/n')
#         else:
#             print('Obrigado volte sempre')
#             print('Total  -  R$',soma)
                    
#             lista_pag = ('','PIX','CC','CD')
#             print(lista_pag)
#             forma_pag = int(input('Digite o ID forma de pagamento'))
#             print(lista_pag[forma_pag])
#         break    
#     else:
#         print('Erro de digitação')
#         chances = chances -1    
# else:
#     print('Bloqueio de conta ')


# e-commerce

# cadastrar
# def e_commerce():
#     dados = {}
#     print('CAdastre-se: ')
#     email = input('E-mail: ')
#     senha = input('senha: ')

#     dados['e-mail'] = email
#     dados['senha'] = senha

#     # acesso ao sistema

#     print('---' * 20)
#     print('Seja bem vindo(a) ao e-commerce ZZZ')
#     print('Acesse a aplicação')

#     chances = 3

#     carrinho = []
#     meu_total = []
#     lista_prod = ['','pipoca','arroz','milho','quentão']
#     valor_prod = ['',2.0,10.0,20.0,15.50]
#     while chances > 0:
#         email_acesso = input('Digite seu e-mail')
#         senha_acesso = input('Digite sua senha')

#         if email_acesso == dados['e-mail'] and senha_acesso == dados['senha']:
#             print('Sejam bem vindo a sua conta ')
#             acesso  = input('Deseja pedir? s/n')
#             print(lista_prod)
#             # escolher produto
#             while acesso == 's':
#                 pedido = int(input('Digite o ID do produto 1 -2 -3 -4')) 
#                 carrinho.append(lista_prod[pedido])
#                 meu_total .append(valor_prod[pedido])
#                 print(carrinho)
#                 soma =  sum(meu_total)
#                 print('R$',soma)
#                 acesso  = input('Deseja pedir? s/n')
#             else:
#                 print('Obrigado volte sempre')
#                 print('Total  -  R$',soma)
                        
#                 lista_pag = ('','PIX','CC','CD')
#                 print(lista_pag)
#                 forma_pag = int(input('Digite o ID forma de pagamento'))
#                 print(lista_pag[forma_pag])
#             break    
#         else:
#             print('Erro de digitação')
#             chances = chances -1    
#     else:
#         print('Bloqueio de conta ')


# while True:
#       e_commerce()


# y = input('digite para sair')

# def somar(a,b):
#     return a+b

# def subtar(a,b):
#     return a-b

# def mult(a,b):
#     return a*b

# def div(a,b):
#     return a/b

# def calculadora():
#     n1 = float(input('='))
#     escolha =  input('operação - + | - | * | /')
#     if escolha == '+':
#         n2 = float(input('='))
#         soma = somar(n1,n2)
#         print('=',soma)
#     elif escolha == '-':
#         n2 = float(input('='))
#         sub = subtar(n1,n2)
#         print('=',sub)  
#     elif escolha == '*':
#         n2 = float(input('='))
#         mul = mult(n1,n2)
#         print('=',mul)   
#     elif escolha == '/':
#         n2 = float(input('='))
#         di = div(n1,n2)
#         print('=',di) 
#     else:
#         print('Digite algo válido')       

# while True:                               
#       calculadora()


# def hora_normal(salario,carga):
#     calculo  = salario/carga
#     return calculo

# def hora_extra(hora_normal):
#     calculo = hora_normal * 1.5
#     return calculo

# def quantas_horas_extras(quantidade, hora_extra):
#     calculo =  quantidade * hora_extra
#     return calculo

# def salario_total(salario, quantidade_extra):
#     calculo =  salario + quantidade_extra
#     return calculo

# def sistema_sal():
#     salario = float(input('Digite seu salario: '))
#     carga = float(input('Digite sua carga: '))
#     hora_colaborador  = hora_normal(salario,carga)
#     print('R$', round(hora_colaborador,2) )
#     hora_extra1 = hora_extra(hora_colaborador)
#     print('R$', round(hora_extra1,2))
#     quantidade_extra = float(input('Horas extras:  '))
#     quantas = quantas_horas_extras(quantidade_extra, hora_extra1)
#     print('R$', round(quantas,2))
#     salario_total_ = salario_total(salario, quantas)
#     print('R$', round(salario_total_,2))


# sistema_sal()



# Exercicio 2

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b:"))
c = float(input("Digite o valor de c:"))
Multiplicar = (a*b*c)
print(Multiplicar)

      



















