from random import choice


def check_file():
    try:
        with open('senhas.txt', 'r') as s:
            s.read()
    except:
        with open('senhas.txt', 'wt+') as s:
            s.read()

def save(password):
    check_file()
    try:
        with open('senhas.txt', 'a') as s:
            s.write(f'{password}\n')
    except:
        print('Não foi possível salvar a senha!')

def verify(txt):
    op = str(input(txt)).strip()
    while op[0] not in 'SsNn':
        print('Digite Sim ou Não.')
        op = str(input(txt)).strip()
    return op[0]



chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 
'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', 
'7', '8', '9']

special_chars = ['_', '-', '@']

try:
    pass_amount = int(input('Quantidade de Senhas: '))
    pass_length = int(input('Tamanho das senhas: '))
    special = verify('Deseja utilizar caractéres especiais?[S/N] ')
    op = verify('Deseja salvar as senhas em um arquivo?[S/N] ')
    pass_list = []
    
    if special in 'Ss':
        for char in special_chars: # Adicionando Carácteres Especiais na lista principal
            chars.append(char)
    
    for amount in range(pass_amount):
        password = ''
        for char in range(pass_length):
            password += choice(chars)
        if op in 'Ss':
            save(password)
        print(password)
        pass_list.append(password)
    

except (TypeError, ValueError):
    print('ERRO! Valor inválido. Tente Novamente')
except KeyboardInterrupt:
    print('O usuário resolveu encerrar o programa.')
except:
    print('Tivemos algum problema ao executar o programa. Tente Novamente')
