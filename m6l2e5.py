games = list()
game = input('Ingresar juego (0 - detener ingreso):')
game = game.lower()
while game != '0':
    if game in games:
        print('El juego ya está registrado')
    else:
        games.append(game)
    game = input('Ingresar juego (0 - detener ingreso):')
    game = game.lower()
games.sort()
print('Lista de juegos:', games)