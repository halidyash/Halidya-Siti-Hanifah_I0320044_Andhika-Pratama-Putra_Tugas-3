#Nama Teman

#List 10 teman
list = ["Rhima Rachman", "Reyhan Fauzan", "Syifa Salsabila", "Nisrina Ayunda", "Azka Ghozi", "Bassam Al-az", "Lubna Mufida", "Tsabitha Nabilla", "Tarisya Syaula", "Alayda Rindu"]
print("List 10 teman: ","\n",list)
print("")

#Menampilkan list indeks nomor 4,6,7
print("List keempat : ",list[4])
print("List keenam  : ",list[6])
print("List ketujuh : ",list[7])
print("")

#Mengganti nama teman pada list 3,5,9
list[3] = "Alifiana Rahma"
list[5] = "Danendra Dimas"
list[9] = "Rafli Ridwan"
print("Mengganti nama teman: ",list)
print("")

#Menambah dua teman
list.append("Abel Alambana")
list.append("Nadiya Salma")
print("Menambah teman: ",list)
print("")

#Menampilkan semua teman
for x in list:
    print(x)
print("")

#Menampilkan panjang list
print(len(list))