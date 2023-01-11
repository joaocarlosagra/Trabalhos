sentenca = "Esta é uma string"

print(len(sentenca))

for i in range(len(sentenca)):
    print(sentenca[i])
    
for caractere in sentenca:
    print(caractere)
    

print(sentenca[0:5])
print(sentenca[0:4])
print(sentenca[10:])
print(sentenca[11:])
    
nova_sentenca = "Aquela " + sentenca[5:]
print(nova_sentenca)
print(nova_sentenca.replace(" ", "*"))
print(nova_sentenca.replace(" ", "_"))
print(nova_sentenca.lower())
indice = nova_sentenca.find("uma")
print(indice)