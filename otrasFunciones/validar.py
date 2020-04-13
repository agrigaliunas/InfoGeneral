def validar(val1,val2,div,num):
    if val1 >= val2:
        mayor = val1
        menor = val2
    elif val1 <= val2:
        mayor = val2
        menor = val1
    if num%div == 0 and (num >=menor and num <=mayor):
        return True
    else:
        return False
    

def main():
    val1 = int(input("Ingrese val1: "))
    val2 = int(input("Ingrese val2: "))
    div = int(input("Ingrese div: "))
    num = int(input("Ingrese num: "))
    print(validar(val1,val2,div,num))
    
main()