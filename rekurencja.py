"Dokumentaja modułu"
def flatten(nested):
    data = []
    for el in nested:
        if type(el) == list:
            for d in flatten(el):
                data.append(d)
        else:
            data.append(el)
    return data

print(dir())
print(__name__)

if __name__ == '__main__':
    nested = [1, 2, 3, [1, 2, 3, [4, [1], 1]]]
    flattened = [1, 2, 3, 1, 2, 3, 4, 1,]

    assert flatten(nested) == flattened