nome = input('Digite o seu nome: ')
xp = int(input('Digite o seu nível de XP:\n'
               'Ferro = 1-1000 XP.\n'
               'Bronze = 1001-2000 XP.\n'
               'Prata = 2001-3000 XP.\n'
               'Ouro = 3001-4000 XP.\n'
               'Platina = 5001-6000 XP.\n'
               'Ascendente = 8001-9000 XP.\n'
               'Imortal = 9001-10000 XP.\n'
               'Radiante = 10001 XP ou mais: '))

def definir_nivel(xp):
    if xp <= 1000:
        return 'Ferro'
    elif xp <= 2000:
        return 'Bronze'
    elif xp <= 3000:
        return 'Prata'
    elif xp <= 4000:
        return 'Ouro'
    elif xp <= 6000:
        return 'Platina'
    elif xp <= 9000:
        return 'Ascendente'
    elif xp <= 10000:
        return 'Imortal'
    else:
        return 'Radiante'

nivel = definir_nivel(xp)
print(f'Nome: {nome}\nNível de XP: {nivel}')
