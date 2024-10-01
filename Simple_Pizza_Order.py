print("Welcome to Amba Pizza!")
size = input("What size pizza do you want? S, M, or L: ")
peperoni = input("Do You want ad peperoni on your pizza? Y or N: ")
extra_cheese = input("Mau ekstra keju dari mr amba? Y or N: ")
bill = 0

if size == "S":
 bill = 15
 print(f"Pizza Size {size}: ${bill}")
 
elif size == "M":
 bill = 20
 print(f"Pizza Size {size}: ${bill}")

elif size == "L":
 bill = 25
 print(f"Pizza Size {size}: ${bill}")
 
else:
 print("Ukuran Tidak Tersedia")

if peperoni == "Y":
   if size == "S":
       bill += 2
       print(f"with peperoni: ${bill}")
   elif size == "M":
        bill += 3
        print(f"with peperoni: ${bill}")
   elif size == "L":
        bill += 3
        print(f"with peperoni: ${bill}")
   else:
        print("Ukuran Tidak Tersedia")

if extra_cheese == "Y":
    bill += 1
    print(f"with extra cheese: ${bill}")
