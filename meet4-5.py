# inputan
# aritmatika + - * /

#coba = input ("Masukan Nama :")
#print(coba)

#bilangan_random = input("Masukan bilangan acak :")
#print(bilangan_random)

#ARITMATIKA
x = 12
y = 3

# penjumlahan +
hasil = x + y
print(x, '+', y, '=', hasil)

# pengurangan -
hasil = x - y
print(x, '-', y, '=', hasil)

# perkalian *
hasil = x * y
print(x, 'x', y, '=', hasil)

# pembagian /
hasil = x / y
print(x, ':', y, '=', hasil)

# perpangkatan **
hasil = x ** y
print(x, '^', y, '=', hasil)

# modulus %
hasil = x % y
print(x, 'mod', y, '=', hasil)

# floor division //
hasil = x // y
print(x, 'floor', y, '=', hasil)

# skala prioritas (), **, */:, +/-
x = 3
y = 4
z = 5

hasil = ( x  ** y * (z + x) / y - z % x // y )
print(hasil)
print(x, '**', y, '*', z, '+', x, '/', y, '-', z, '%', x, '//', y, hasil)