# NOT = !
# => = >
# si = -
# ori = + 



def verify_Expression(str, list_operators, list_operands):
    if len(str) <= 3: #observam ca nu poate exista nicio expresie logica valida cu o lungime mai mica decat 3. Cea mai scurta expresie fiind (!p)
        return False

    if str[0] != '(': #este obligatoriu ca o expresie logica valida sa inceapa cu (
        return False
    
    if str[len(str)-1] != ')': #este obligatoriu ca o expresie logica valida sa se termine cu )
        return False

    if len(str) == 4 and (str[1] != '!' or str[2] not in list_operands): #daca lungimea expresiei este 4, atunci aceasta trebuie sa fie (!p), fiind o operatie unara
        return False


    openBracket = 0
    closedBracket = 0
    i = 1 #expresia porneste de la pozitia 0, insa cum aceasta este deja evaluata, vom pleca de pe pozitia 1
    while i < len(str)-1:
        if str[i] =='(': #expresie compusa sau avem un !
            openBracket = openBracket + 1
        
        if str[i] == ')':
            closedBracket = closedBracket + 1

        if str[i] not in list_operands and str[i] not in list_operators:
            return False
        
        if str[i] in list_operands and str[i+1] in list_operands:#nu pot fi 2 operanzi consecutivi
            return False

        if str[i] in list_operators and str[i+1] in list_operators:#nu pot fi 2 operatori consecutivi
            return False
        
        if str[i] in list_operators and str[i+1] ==')':  #daca elementul este un operator(!, +, >, -) si elementul urmator este paranteza, atunci expresia este eronata
            return False
        
        #if str[i] not in list_operators or str[i] not in list_operands:
         #   return i

       # if str[i] in list_operands: #dupa un operand, obligatoriu trebuie sa vina un operator, altfel expresia va fi falsa ///// exceptie (!p)
        #    if str[i+1] not in list_operators  and  str[i-1] != '!':# daca acest caracter nu se afla in lista de operatori, rezulta fal
         #       return i
            
          
            
            if str[i+1] == '(':
                if str[i+2] == '!' :
                    if str[i+3] not in list_operands or str[i+4] != ')':
                        return "False8"
            


        i = i + 1
    
    if closedBracket != openBracket:
        return False

    return True

            
            






str = input()

n = int(input()) # number of operands


list_operators = ['!', ">", "+", "-"]
list_operands = []

for i in range(n):
    op = input()
    list_operands.append(op)


print(verify_Expression(str, list_operators, list_operands))
