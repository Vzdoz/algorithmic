alemans = ['max123', 'happy_girl', 'funnyguy', 'crazy.cat']
amount_users = len(alemans)
alemans.sort()
i = 1 
print('Lista de usuarios:')
for aleman in alemans:
   print(i, '-', aleman)
   i += 1
print('Usuarios totales:', amount_users)