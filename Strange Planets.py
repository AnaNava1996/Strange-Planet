from random import randint


def aEvent(pipol):
    pipol[0]=pipol[0]+2
    pipol[1]=pipol[1]-1
    pipol[2]=pipol[2]-1
    return pipol

def bEvent(pipol):
    pipol[0]=pipol[0]-1
    pipol[1]=pipol[1]+2
    pipol[2]=pipol[2]-1
    return pipol

def cEvent(pipol):
    pipol[0]=pipol[0]-1
    pipol[1]=pipol[1]-1
    pipol[2]=pipol[2]+2
    return pipol

def probandoPT(PT):
    moves=0
    if(PT==3):
        moves=1
    elif(PT==6):
        moves=5#mejor 3...
    elif(PT==9):
        moves=12
    elif(PT==12):#####
        moves=25
    elif(PT==15):
        moves=35
        pass
    else:
        print("asfasf")
    return moves

def probando(pipol,PT,piAux):
    extincion=False
    loop=False
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    if(PT==3 or PT==6 or PT==9 or PT==12 or PT==15):
        a=b=c=probandoPT(PT)
    else:
        a=b=c=PT*2#funciona, pero seria mejor disminuir el numero
    while(extincion!=True):
        while(loop!=True or extincion!=True):
            if((pipol[0]==0 and pipol[1]==0)or(pipol[1]==0 and pipol[2]==0)or(pipol[0]==0 and pipol[2]==0)):
                extincion=True
                loop=True# para que se detenga de una vez
                print("El planeta falla :D")
                c=open('Planetas.txt','a+')
                c.write("\nEl planeta falla :D\n\n")
                c.close()
            elif(pipol[0]==0):#a event
                d=d+1
                print(aEvent(pipol))
                imprimir(pipol)
                if(pipol==piAux):
                    loop=True
                    if(d>=a or e>=b or f>=c):
                        extincion=True# es la peor mentira porque en realidad en esta condicion nunca se extingue... pero es para que termine de correr
                        print("No fallara nunca")
                        c=open('Planetas.txt','a+')
                        c.write("\nNo fallara nunca\n\n")
                        c.close()
            elif(pipol[1]==0):#b event
                e=e+1
                print(bEvent(pipol))
                imprimir(pipol)
                if(pipol==piAux):
                    loop=True
                    if(d>=a or e>=b or f>=c):
                        extincion=True#mentira
                        print("No fallara nunca")
                        c=open('Planetas.txt','a+')
                        c.write("\nNo fallara nunca\n\n")
                        c.close()
            elif(pipol[2]==0):#c event
                f=f+1
                print(cEvent(pipol))
                imprimir(pipol)
                if(pipol==piAux):
                    loop=True
                    if(d>=a or e>=b or f>=c):
                        extincion=True#mentira
                        print("No fallara nunca")
                        c=open('Planetas.txt','a+')
                        c.write("\nNo fallara nunca\n\n")
                        c.close()
            else:###################################################### si a=b o b=c o a=c.... else lo que sigue... que es random...
                if(pipol[1]==pipol[2]):# b=c -> a event
                    d=d+1
                    print(aEvent(pipol))
                    imprimir(pipol)
                    if(pipol==piAux):
                        loop=True
                        if(d>=a or e>=b or f>=c):
                            extincion=True#mentira
                            print("No fallara nunca")
                            c=open('Planetas.txt','a+')
                            c.write("\nNo fallara nunca\n\n")
                            c.close()
                elif(pipol[0]==pipol[2]):# a=c -> b event
                    e=e+1
                    print(bEvent(pipol))
                    imprimir(pipol)
                    if(pipol==piAux):
                        loop=True
                        if(d>=a or e>=b or f>=c):
                            extincion=True#
                            print("No fallara nunca")
                            c=open('Planetas.txt','a+')
                            c.write("\nNo fallara nunca\n\n")
                            c.close()
                elif(pipol[0]==pipol[1]):# a=b -> c Event
                    f=f+1
                    print(cEvent(pipol))
                    imprimir(pipol)
                    if(pipol==piAux):
                        loop=True
                        if(d>=a or e>=b or f>=c):
                            extincion=True#mentira
                            print("No fallara nunca")
                            c=open('Planetas.txt','a+')
                            c.write("\nNo fallara nunca\n\n")
                            c.close()
                else:
                    random=randint(1,3)
                    if(random==1):# a event
                        d=d+1
                        print(aEvent(pipol))
                        imprimir(pipol)
                        if(pipol==piAux):
                            loop=True
                            if(d>=a or e>=b or f>=c):
                                extincion=True#mentira
                                print("No fallara nunca")
                                c=open('Planetas.txt','a+')
                                c.write("\nNo fallara nunca\n\n")
                                c.close()
                    elif(random==2):#b event
                        e=e+1
                        print(bEvent(pipol))
                        imprimir(pipol)
                        if(pipol==piAux):
                            loop=True
                            if(d>=a or e>=b or f>=c):
                                extincion=True#
                                print("No fallara nunca")
                                c=open('Planetas.txt','a+')
                                c.write("\nNo fallara nunca\n\n")
                                c.close()
                    else:# c event
                        f=f+1
                        print(cEvent(pipol))
                        imprimir(pipol)
                        if(pipol==piAux):
                            loop=True
                            if(d>=a or e>=b or f>=c):
                                extincion=True#mentira
                                print("No fallara nunca")
                                c=open('Planetas.txt','a+')
                                c.write("\nNo fallara nunca\n\n")
                                c.close()

def imprimir(pipol):#poner cada vez que se imprime un pipol
    f=open('Planetas.txt','a+')
    cad=" -> ("
    for i in pipol:
        cad=cad+str(i)+","
    cad=cad+")"
    f.write(cad)
    f.close()

op=str(input("\nm-Manual.\na-Automatico.\ng-Informacion general sobre los planetas.\ns-Salir: "))
while(op!='s'):
    if(op=='m'):
        c=open('Planetas.txt','a+')
        c.write("\n\nMODO MANUAL\n")
        c.close()
        PT=int(input("Introduzca la poblacion total n: "))
        for i in range(0,PT+1):
            for j in range(0,PT+1):
                for k in range(0,PT+1):
                    if((i+j+k)==PT):
                        pipol=[]
                        piAux=[]
                        pipol.append(i)
                        pipol.append(j)
                        pipol.append(k)
                        piAux.append(i)
                        piAux.append(j)
                        piAux.append(k)
                        print("\n.. .. .. .. .. .. .. .. .. .. .. .. ")
                        print(pipol)
                        imprimir(pipol)
                        probando(pipol,PT,piAux)
        op=str(input("\nm-Manual.\na-Automatico.\ng-Informacion general sobre los planetas.\ns-Salir: "))
    elif(op=='a'):
        c=open('Planetas.txt','a+')
        c.write("\n\nMODO AUTOMATICO\n")
        c.close()
        PT=randint(1,15)
        for i in range(0,PT+1):
            for j in range(0,PT+1):
                for k in range(0,PT+1):
                    if((i+j+k)==PT):
                        pipol=[]
                        piAux=[]
                        pipol.append(i)
                        pipol.append(j)
                        pipol.append(k)
                        piAux.append(i)
                        piAux.append(j)
                        piAux.append(k)
                        print("\n.. .. .. .. .. .. .. .. .. .. .. .. ")
                        print(pipol)
                        imprimir(pipol)
                        probando(pipol,PT,piAux)
        op=str(input("\nm-Manual.\na-Automatico.\ng-Informacion general sobre los planetas.\ns-Salir: "))
    elif(op=='s'):
        op='s'
    elif(op=='g'):
        print("\n\n  En general, los planetas de 2,4,5,7,8,10,11 y 13 y 14 estan destinados a fallar todos")
        print("  Planetas cuya cantidad de habitantes es multiplo de 3, hay 3 posibilidades:")
        print("Si todas las combinaciones las agrupara en planetas, 2 planetas nunca fallaran y 1 si,")
        print("...ese ultimo tiene las tres maneras de fallar en un solo planeta, y este programa")
        print("busca la manera mas rapida de llegar a cualquiera de esas opciones")
        print("  Pareciera que cuando la cantidad de habitantes es multiplo unicamente de numeros que ")
        print("siempre fallan, Ese planeta esta destinado a fallar tambien... se puede ver como")
        print("que los planetas con pocos habitantes son la representacion en pequegno de un gran conjunto")
        
        op=str(input("\nm-Manual.\na-Automatico.\ng-Informacion general sobre los planetas.\ns-Salir: "))
    else:
        op=str(input("\nm-Manual.\na-Automatico.\ng-Informacion general sobre los planetas.\ns-Salir: "))

