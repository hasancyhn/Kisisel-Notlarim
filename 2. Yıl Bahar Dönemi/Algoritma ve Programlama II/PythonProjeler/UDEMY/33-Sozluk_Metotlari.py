
players = {
    '1':
        {
            'name': 'Cristiano Ronaldo', 'yearOfBirth': '1985', 'nationality': 'Portugal', 'current_team': 'Portugal', 'history': ['Juventus', 'Real Madrid', 'Portugal']
        },
    '2':
        {
            'name': 'Lionel Messi', 'yearOfBirth': '1987', 'nationality': 'Argentina', 'current_team': 'Barcelona', 'history': ['Barcelona', 'Argentina', 'Portugal']}
        }


# 1- id' e göre arama yapınız.
# id = input('aramak istediğiniz oyuncu id: ')
# player = players.get(id)
# print(f'name: {player.get("name")}')

# 2- id' e göre bilgi kayıt siliniz.

id = input('silmek istediğiniz oyun id: ')
players.pop(id)

print(players)
