def complemento_de_dois(binario):
    # inverte os bits do número
    invertido = binario.translate(str.maketrans('01', '10'))
    
    # adiciona 1 ao número invertido
    resultado = ''
    carry = 1
    for bit in invertido[::-1]:
        if bit == '0' and carry == 1:
            resultado += '1'
            carry = 0
        elif bit == '1' and carry == 1:
            resultado += '0'
        else:
            resultado += bit
            
    return resultado[::-1]
    

def subtrair_binarios(minuendo, subtraendo):
    # complemento de dois do subtraendo
    complemento = complemento_de_dois(subtraendo)
    
    # adição do minuendo com o complemento de dois
    resultado = bin(int(minuendo, 2) + int(complemento, 2))[2:]
    
    # descarta o bit mais significativo (se houver overflow)
    if len(resultado) > len(minuendo):
        resultado = resultado[1:]
    
    # se o resultado for negativo (bit mais significativo = 1), converte para complemento de dois
    if resultado[0] == '1':
        resultado = complemento_de_dois(resultado)
    
    return resultado

minuendo= input("escreva o numero binario que voce deseja diminuir ")
subtraendo= input("escreva o outro numero que ira diminuir o primeiro ")
print(subtrair_binarios(minuendo,subtraendo))
