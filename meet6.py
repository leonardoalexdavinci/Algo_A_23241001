# perbandingan >, <, >=, <=, ==, !=, =, is, isnot

x = 3
y = 4

# lebih besar >
hasil = y > x
print (x, '>', y, '=', hasil)

# lebih kecil <
hasil = y < x
print (x, '<', y, '=', hasil)

# lebih besar >=
hasil = y >= x
print (x, '>=', y, '=', hasil)
print (x, '>=', 3, '=', hasil)

# lebih kecil <=
hasil = y <= x
print (x, '<=', y, '=', hasil)
print (x, '<=', 3, '=', hasil)

# is (adalah)
hasil = x is 9
print(x, 'is', 9, '=', hasil)

# is-not (bukan)
hasil = x is not 9
print(x, 'is-not', 9, '=', hasil)

# sama dengan (==)
hasil = x == 9
print(x, '==', 9, '=', hasil)

# tidak sama dengan (!=)
hasil = x != 9
print(x, '!=', 9, '=', hasil)