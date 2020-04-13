def main():
    pares = 0
    impares = 0
    incorrectas = 0
    num = int(input("[primero]"))
    if num%2 == 0 and num !=0:             #Numero par
        pares +=1
        while num != 0:
            if num !=0:
                num = int(input("[imPar]"))
                while num%2 == 0 and num != 0:
                    incorrectas +=1
                    num = int(input("[imPar]"))
                if num !=0:
                    impares +=1
            if num !=0:
                num = int(input("[Par]"))
                while num%2 != 0 and num != 0:
                    incorrectas +=1
                    num = int(input("[Par]"))
                if num !=0:
                    pares +=1
    
    elif num%2 != 0 and num !=0:
        impares +=1
        while num != 0:
            if num !=0:
                num = int(input("[Par]"))
                while num%2 != 0 and num !=0:
                    incorrectas +=1
                    num = int(input("[Par]"))
                if num !=0:
                    pares +=1
            if num !=0:
                num = int(input("[imPar]"))
                while num%2 == 0 and num !=0:
                    incorrectas +=1
                    num = int(input("[imPar]"))
                if num !=0:
                    impares +=1
                    
    print("\n Se ingresaron: \n Pares: {} \n Impares: {} \n Paridad Incorrecta: {}".format(pares,impares,incorrectas))
        
main()
            