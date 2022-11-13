print ("""
        ==========================================
                      >>KALKULATOR<<
                        SEDERHANA
        ==========================================""")

print ("==================")
print ("       menu       ")
print ("==================")

print(""" 
    pilihan operator
 1. pertambahan (+)
 2. pengurangan (-)
 3. pembagian   (/)
 4. perkalian   (*)
 5. pangkat     (**)
 6. modulus (sisa bagi) (%)
 7. floor division (//)
""")

a = float(input("masukan bilangan pertama = "))
b = float(input("masukan bilangan kedua   = "))

operator = input("masukan no operator      = ")

if operator == "1":
  print("hasil dari {} + {} = {} ".format(a, b, a + b))
elif operator == "2":
  print("hasil dari {} - {} = {} ".format(a, b, a - b))
elif operator == "3":
  print("hasil dari {} / {} = {} ".format(a, b, a / b))
elif operator == "4":
  print("hasil dari {} * {} = {} ".format(a, b, a * b))
elif operator == "5":
  print("hasil dari {} ** {} = {} ".format(a, b, a ** b))
elif operator == "6":
  print("hasil dari {} % {} = {} ".format(a, b, a % b))
elif operator == "7":
  print("hasil dari {} // {} = {} ".format(a, b, a // b))
else :
    print("maaf oprator yang anda masukan salah")