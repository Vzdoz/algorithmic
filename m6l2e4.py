games = ['dota 2', 'cs go', 'warface', 'minecraft']
searching = input('Solicitud:')
searching = searching.lower()
if searching in games:
    print('Solucitud encontrada an deseos')
else:
    print('Deseo no existe')