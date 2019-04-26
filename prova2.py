matricula=[]
nome=[]
notafinal=[]
status=[]


def ler():                                                   #questões A,G e H
    em=-1
    while em!=0:
        em=int(input("Digite a matrícula do candidato "))
        l=len(matricula)
        j=False
        if em!=0:
            for i in range(l):
                if em==matricula[i]:
                    j=True
            if j!=True:
                matricula.append(em)
                nome.append(input("Digite a o nome do candidato "))
                notafinal.append(float(input("Digite a nota final do candidato ")))
            else:
                print("Essa matrícula já está concorrendo ")


def media():                                                 #faz parte da questão I e auxilia na D
    l=len(matricula)
    soma=0.0
    for i in range(l):
        soma+=notafinal[i]
    med=soma/l
    return med

def ordem():                                                 #auxilia na questão B
    l=len(matricula)
    for i in range(l):
        for j in range(l):
            if i!=j:
                if notafinal[i]>notafinal[j]:
                    tnf=notafinal[i]
                    tm=matricula[i]
                    tn=nome[i]
                    notafinal[i]=notafinal[j]
                    matricula[i]=matricula[j]
                    nome[i]=nome[j]
                    notafinal[j]=tnf
                    matricula[j]=tm
                    nome[j]=tn


def classificar():                                           #questão B, C, D, E e F
    ordem()
    med=media()
    l=len(matricula)
    for i in range(l):                                       #põe os acima da média na lista de espera
        if notafinal[i]>=med:
            status.append("lista de espera")
        else:
            status.append("não classificado")
    if l >10:
        c=10
    else:
        c=l
    for i in range(c):                                       #poe os dez primeiros da lista de espera como classificados
        if status[i]=="lista de espera":
            status[i]="classificado"
    for i in range (l):                                      #troque de lugar na classificação se a nota for igual a do proximo e a matricula for maior
        if i!=l-1:
            if notafinal[i]==notafinal[i+1]:                 #a intenção é fazer as menores matrículas estaremm na frente
                if matricula[i]>matricula[i+1]:
                    tnf=notafinal[i]
                    tm=matricula[i]
                    tn=nome[i]
                    notafinal[i]=notafinal[i+1]
                    matricula[i]=matricula[i+1]
                    nome[i]=nome[i+1]
                    notafinal[i+1]=tnf
                    matricula[i+1]=tm
                    nome[i+1]=tn


def exibir():                                                #Função para exibir na tela
    print("A média de notas foi: ",media())
    print(" ")
    print("A lista de candidatoe em ordem de classificação é: ")
    print(" ")
    print("*suspense*")
    print(" ")
    l=len(matricula)
    for i in range(l):
        print("Candidato número ",i+1)
        print("matrícula ",matricula[i])
        print("Nome ",nome[i])
        print("Nota Final ",notafinal[i])
        print("Status ",status[i])
        print("----------------------------------------------------------------------------------------------------------")


ler()
classificar()
exibir()
























































