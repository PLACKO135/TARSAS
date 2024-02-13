

with open("dobasok.txt", "r") as file:dobasokfile=[line.rstrip() for line in file][0]
with open("osvenyek.txt", "r") as file:osvenyekfile=[line.rstrip() for line in file]
   
print(f"2.feladat\n A dobások száma: {len(dobasokfile.replace(' ',''))}\n Az ösvények száma: {len(osvenyekfile)}")
print()

sorszama=0
large_line_len = 0
for line in osvenyekfile:
    if len(line) > large_line_len:
        large_line_len = len(line)
        sorszama+=1

print(f"3.feladat\n Az egyik leghosszabb a(z) {sorszama}. ösvény hossza: {large_line_len}")
print()

print("4.feladat")


osvenysorszama=int(input("Adja meg egy ösvény sorszámát! "))
jatekosokszama=int(input("Adja meg a játékosok számát!  "))

print()

m=0
v=0
e=0

thisdict = {
  "M": 0,
  "V": 0,
  "E": 0
}


for i in osvenyekfile:
    if osvenyekfile[osvenysorszama] == "M":
        m+=1
        thisdict.update({"M": m})
    elif osvenyekfile[osvenysorszama] == "V":
        v+=1
        thisdict.update({"V": v})
    elif osvenyekfile[osvenysorszama]== "E":
        e+=1
        thisdict.update({"E": e})

print(f"5.feladat\n{thisdict}")


print()

különleges=open("különleges.txt","w")
for i in range(osvenyekfile.count(osvenyekfile[osvenysorszama])):
    if osvenyekfile[osvenysorszama]== "E"or osvenyekfile[osvenysorszama]=="V":
        különleges.write(f"{i}\t{osvenyekfile[osvenysorszama]}\n")
különleges.close()
print()

print("7.feladat")
print()
print("8.feladat")