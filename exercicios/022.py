nome = str(input("Seu nome: "))
print(nome.upper())
print(nome.lower())
nomese = nome.replace(' ','')
print("Qte de letras s/ espaços:",len(nomese))
nomepn = nome.split()
print("Qte de letras do 1º nome:",len(nomepn[0]))