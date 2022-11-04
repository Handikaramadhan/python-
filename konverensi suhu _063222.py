# latihan konverensi satuan temperatur

# program konversi celsius ke satuan lain

print("\nPROGRAM KONVERENSI TEMPERATUR\n")

print("\n========== KONVERENSI CELCIUS ==========\n")
celcius = float(input("masukan suhu dalam celsius : "))
print("suhu adalah ",celcius,"C")

# reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah ",reamur,"R")


# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah ",fahrenheit,"F")

# kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah ",kelvin,"K")

# program konversi reamur ke satuan lain

print("\n========== KONVERENSI REAMUR ==========\n")

reamur = float(input("masukan suhu dalam reamur : "))
print("suhu adalah ",reamur,"R")

# celcius
celcius = (5/4) * reamur
print("suhu dalam celcius adalah ",celcius,"C")

# fahrenhei

fahrenheit = ((9/4) * reamur) + 32
print("suhu dalam fahrenheit adalah ",fahrenheit,"F")

# kelvin
kelvin = ((5/4) * reamur) + 273
print("suhu dalam kelvin adalah ",kelvin,"K")

# program konversi fahrenheit ke satuan lain

print("\n========== KONVERENSI FAHRENHEIT==========\n")

fahrenheit = float(input("masukan suhu dalam fahrenheit : "))
print("suhu adalah ",fahrenheit,"F")

# celcius
celcius = 5/9 * (fahrenheit - 32)
print("suhu dalam celcius adalah ",celcius,"C")

# reamur
reamur = 4/9 * (fahrenheit - 32)
print("suhu dalam reamur adalah ",reamur,"R")

# kelvin
kelvin = ((5/9) * (fahrenheit - 32)) + 273
print("suhu dalam kelvin adalah ",kelvin,"K")

# program konveransi kelvin ke satuan lain
print("\n========== KONVERENSI KELVIN ==========\n")

kelvin = float(input("masukan suhu dalam kelvin : "))
print("suhu adalah ",kelvin,"K")

# celcius
celcius = kelvin - 273
print("suhu dalam celcius adalah",celcius,"C")

# reamur
reamur = 4/5 * (kelvin - 273)
print("suhu dalam reamur adalah ",reamur,"R")

# fahrenheit 
fahrenheit = (kelvin - 273) * 9/5 + 32
print("suhu dalam fahrenheit adalah ",fahrenheit,"F")