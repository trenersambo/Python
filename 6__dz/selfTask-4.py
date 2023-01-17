# Сделать фильтр по условию

people = [
    ('Johnny', 22),
    ('Adam', 18),
    ('Mark', 12),
    ('Jack', 14),
    ('Sam', 20)
]

def is_adult(person):
    return person[1] >= 18

adults = filter(is_adult, people)

print(list(adults))




# ======== variable 2(lambda) ==============

is_adult = lambda person: person[1] >= 18

adults = filter(is_adult, people)
print(list(adults))