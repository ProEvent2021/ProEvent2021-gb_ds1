catalog_2 = [1, 3, 6, 7, 9, 10]
if len(catalog_2) % 2 == 0:
    i = 0
    while i < len(catalog_2):
        el = catalog_2[i]
        catalog_2[i] = catalog_2[i + 1]
        catalog_2[i + 1] = el
        i += 2
else:
    i = 0
    while i < len(catalog_2) - 1:
        el = catalog_2[i]
        catalog_2[i] = catalog_2[i + 1]
        catalog_2[i + 1] = el
        i += 2
print(catalog_2)