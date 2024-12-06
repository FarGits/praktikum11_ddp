# memanggil file gempa dan import semua method/fungsi
from Gempa import *

# membuat objek dengan argumen
gempa1 = Gempa('banten', 1.2)
gempa2 = Gempa('palu', 6.1)
gempa3 = Gempa('cianjur', 5.6)
gempa4 = Gempa('jayapura', 3.3)
gempa5 = Gempa('garut', 4.0)


# informasi gempa
print('## info gempa masseh ##')
print()
gempa1.dampak()
gempa2.dampak()
gempa3.dampak()
gempa4.dampak()
gempa5.dampak()