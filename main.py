import random
import time

senha = []

# Método para saber se o usuario quer escolher o tamanho da senha ou deixar aleatório
def tamanho_senha(escolha) -> int:
    tamanho_da_senha = 0
    while True:

        # Tamanho escolhido pelo usuário
        if escolha == 1:

            while tamanho_da_senha < 6 or tamanho_da_senha > 24:
                print(f"Digite o tamanho da senha desejado:")
                tamanho_da_senha = int(input())

                if  6 <= tamanho_da_senha <= 24:
                    return tamanho_da_senha

                if tamanho_da_senha < 6 or tamanho_da_senha > 24:
                    print(f"Tamanho de senha inválido! Mínimo: 6 e Máximo: 24")

        # Tamanho da escolha aleatória
        if escolha == 2:
            # Tamanho da senha pode ser de no mínimo 8 caracteres até 24
            tamanho_da_senha = random.randint(8,24)
            return tamanho_da_senha

# Método para gerar a senha aleatória
def gerador_senha(tamanho):
    print("Gerando sua senha....")
    time.sleep(2)

    strings = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","&","*")

    for string in range(0,tamanho):
        senha.append(random.choice(strings))


    for caracter in senha:
        print(caracter, end="")

def main():
    while True:
        try:
            escolha = int(input("Escolha uma opção:\n1 para escolher o tamanho da senha\n2 para o tamanho ser aleatório\n"))
            if escolha in [1,2]:
                tamanho = tamanho_senha(escolha)
                if tamanho != -1:
                    print(f"O tamanho escolhido foi {tamanho}")
                    break
            
            else:
                print("Escolha inválida! Escolha entre 1 e 2!!!")
        
        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro.")
    
    gerador_senha(tamanho)

if __name__ == "__main__":
    main()