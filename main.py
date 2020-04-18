films = {}
actors = {}
all_actors_mn = set()

print('Список фильмов:')
with open("input.txt", encoding='utf-8') as inp:
    for i in inp:
        i = i[:-1]
        f = i.find('-')
        # -1 перешагиваем серез пробел
        film = i[:f-1]
        print(film)
        # +2 перешагиваем через - и пробел
        artist = i[f+2:].split(', ')
        for j in artist:
            all_actors_mn.add(j)
            if j in actors:
                actors[j] += [film]
            else:
                actors[j] = [film]
        films[film] = artist

choice_film_1 = input('Выберите первый фильм: ')
choice_film_2 = input('Выберите второй фильм: ')

while choice_film_1 not in films:
    choice_film_1 = input('Ошибка. Выберите  еще раз первый фильм: ')
while choice_film_2 not in films:
    choice_film_2 = input('Ошибка. Выберите  еще раз второй фильм: ')
menu_1 = int(input('Что хотите выбрать?\n 1 - Актеры, снимавшиеся хотя бы в обном фильме.\n 2 - '
                   'Все актеры, снимавшиеся в сразу в 2ух фильмах.\n'
          ' 3 -Актеры, участвующие в съемках первого, но не участвующие в съемках второго '))

film_1 = set(films[choice_film_1])
film_2 = set(films[choice_film_2])

if menu_1 == 1:
    all_actors = ', '.join(film_1 | film_2)
    print('Общий актерский состав, снимавшийся хотя бы в одном из этих двух фильмах:', all_actors)
if menu_1 == 2:
    actors_both = ', '.join(film_1 & film_2)
    if actors_both == '':
        actors_both = 'таких фильмов нет'
    print('Актеры, снимавшиеся и в первом, и во втором фильме:', actors_both)
else:
    actors_only_first = ', '.join(film_1 - film_2)
    if actors_only_first == '':
        actors_only_first = 'таких фильмов нет'
    print('Актеры, участвующие в съемках первого, но не участвующие в съемках второго:', actors_only_first)
print('')

print('Список актеров:')
for i in all_actors_mn:
    print(i)

choice_actor_1 = input('Выберите первого актера: ')
choice_actor_2 = input('Выберите второго актера: ')

while choice_actor_1 not in actors:
    choice_actor_1 = input('Ошибка. Выберите  еще раз первого актера: ')
while choice_actor_2 not in actors:
    choice_actor_2 = input('Ошибка. Выберите  еще раз второго актера: ')

actor_1 = set(actors[choice_actor_1])
actor_2 = set(actors[choice_actor_2])
menu_2 = int(input('Что хотите выбрать?\n 1 - Фильмы, в которых снимался хотя бы один из актеров'
                   '.\n 2 - Фильмы, в которых снимались оба актера.\n'
          ' 3 -Фильмы, в которых снимался первый актер, но не участвовал в съемках второй '))

if menu_2 == 1:
    all_films = ', '.join(actor_1 | actor_2)
    print('Названия фильмов, в которых снимался хотя бы в одном из актеров:', all_films)
if menu_2 == 2:
    films_both = ', '.join(actor_1 & actor_2)
    if films_both == '':
        films_both = 'таких фильмов нет'
    print('Названия фильмов, в которых снимались оба актера:', films_both)
else:
    films_only_first = ', '.join(actor_1 - actor_2)
    if films_only_first == '':
        films_only_first = 'таких фильмов нет'
    print('Названия фильмов, в которых снимался первый актер, но не участвовал в съемках второй:', films_only_first)