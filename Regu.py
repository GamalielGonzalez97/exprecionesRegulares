import re

#lista de tokens y las expresiones regulares 
texto='''
Gamaliel gonzalez
Jaime jesus
Tania ruby
'''
#nombre
print(re.findall(r'\w+\s\w+',texto))


#busca expreciones de numeros telefono 

texto='''
112-33-44-55
618-108-54-13
22251-233-44-55
618-125-13-67
618-332-05-41
123-44-5-6
'''
print(re.findall(r'\d{3}-\d{3}-\d{2}-\d{2}',texto))
#correo buscar expreciones
texto='''
gama_@hotmail.com
tania_@hotmail.com
jaime_@hotmail.com
'''
print(re.findall(r'\w+@\w+\.com',texto))