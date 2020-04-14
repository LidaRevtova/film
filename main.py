films = {}
actors = {}
all_actors_mn = set()

print('Список фильмов:')
with open("input.txt", encoding='utf-8') as inp:
    for i in inp:
        i = i[:-1]
        f = i.find('-')
        film = i[:f-1]
        print(film)
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

while choice_film_1 not in films or choice_film_2 not in films:
    choice_film_1 = input('Выберите первый фильм: ')
    choice_film_2 = input('Выберите второй фильм: ')

film_1 = set(films[choice_film_1])
film_2 = set(films[choice_film_2])
all_actors = ', '.join(film_1 | film_2)
actors_both = ', '.join(film_1 & film_2)
actors_only_first = ', '.join(film_1 - film_2)
if actors_both == '':
    actors_both = 'таких фильмов нет'
if actors_only_first == '':
    actors_only_first = 'таких фильмов нет'

print('Общий актерский состав, снимавшийся хотя бы в одном из этих двух фильмах: ', all_actors)
print('Актеры, снимавшиеся и в первом, и во втором фильме: ', actors_both)
print('Актеры, участвующие в съемках первого, но не участвующие в съемках второго: ', actors_only_first)
print('')

print('Список актеров:')
for i in all_actors_mn:
    print(i)
choice_actor_1 = input('Выберите первого актера: ')
choice_actor_2 = input('Выберите второго актера: ')

while choice_actor_1 not in actors or choice_actor_2 not in actors:
    choice_actor_1 = input('Выберите первого актера: ')
    choice_actor_2 = input('Выберите второго актера: ')

actor_1 = set(actors[choice_actor_1])
actor_2 = set(actors[choice_actor_2])
all_films = ', '.join(actor_1 | actor_2)
films_both = ', '.join(actor_1 & actor_2)
films_only_first = ', '.join(actor_1 - actor_2)
if films_both == '':
    films_both = 'таких фильмов нет'
if films_only_first == '':
    films_only_first = 'таких фильмов нет'

print('Названия фильмов, в которых снимался хотя бы в одном из актеров: ', all_films)
print('Названия фильмов, в которых снимались оба актера: ', films_both)
print('Названия фильмов, в которых снимался первый актер, но не участвовал в съемках второй: ', films_only_first)