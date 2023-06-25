from os import environ

# obter a letra da unidade do disco rígido no Windows
system_drive = environ.get('SYSTEMDRIVE')
print(system_drive)

# obter o nome do computador
computer_name = environ.get('COMPUTERNAME')  # No Windows
print(computer_name)

# odas as variáveis de ambiente disponíveis para o script Python em execução
for key, value in environ.items():
    print(f"{key} = {value}")
