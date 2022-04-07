
a = 'a'
b = 'b'
listik = ['asdasd','asdasd']
spis = [a,listik]
print(spis)
listik[1] = "Aleh"
print(spis)


def func(list):
    list[1] = 'boba'

func(listik)

print(listik)