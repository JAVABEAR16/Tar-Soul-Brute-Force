import random

caracteres_possíveis = [ # possíveis strings
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d",
    "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
    "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
    "y", "z", "0", "1", "2", "3", "4", "5", "6", "7",
    "8", "9", "!", "@", "#", "$", "%", "^", "&", "*",
    "(", ")", "-", "_", "=", "+", "[", "]", "{", "}",
    "\\", "|", ";", ":", "'", "\"", ",", ".", "/", "<",
    ">", "?", "ç", "Ç", "á", "Á", "à", "À", "ã", "Ã",
    "â", "Â", "é", "É", "ê", "Ê", "í", "Í", "ó", "Ó",
    "õ", "Õ", "ô", "Ô", "ú", "Ú", "ü", "Ü", "~", "`",
    "´", "¨", "º", "ª"
]

print("-"*40)
print("TAR SOUL BRUTE FORCE 👨‍💻".center(40))
print("-"*40)
print()
print("Digite uma senha, e vamos ver quantas tentativas até ela ser quebrada pelo \"Tar Soul\"!")
print()
senha = input("Digite uma senha: ".strip())
print()
mensurador = len(senha) # contagem de caracteres (int)
tentativa = ''.join(random.choices(caracteres_possíveis, k=mensurador)) #O ''.join junta tudo em uma string, o "random choices" permite randomiza as letras, e o "k" faz a função de randomizar aleatóriamente as letras correspondentes ao tamanho do mensurador.
contador = 0
while senha != tentativa:
    contador += 1
    tentativa = ''.join(random.choices(caracteres_possíveis, k=mensurador))
    print(tentativa)
print()
print(f"A senha é {tentativa}, e demorou {contador} tentativas para que o código fosse quebrado pelo Tar Soul!")
print()
