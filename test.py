import locale

locale.setlocale(locale.LC_ALL, '')
a = locale.atof('123,456.789')

print(a)
locale.atof('123456.789')