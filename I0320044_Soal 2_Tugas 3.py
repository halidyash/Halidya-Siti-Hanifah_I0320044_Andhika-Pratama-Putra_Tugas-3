#Dictionary

dict = {'Nama':'Halidya Siti Hanifah', 'Hobi 1':'Bermain musik', 'Hobi 2':'Design', 'Hobi 3':'Menonton film',
        'Sosial media 1':'Instagram @halidyash','Sosial media 2':'Line : halidyaash','Sosial media 3':'Whatsapp : 087884754527',
        'Lagu kesukaan 1':'To The Bone - Pamungkas','Lagu kesukaan 2':'ILYSB - LANY','Lagu kesukaan 3':'Positions - Ariana Grande','Lagu kesukaan 4':'Little Things - 1D',
        'Makanan Favorit 1':'Cheesecake','Makanan Favorit 2':'Lasagna','Makanan Favorit 3':'Batagor'}
print(dict)
print("")

#Mengubah hobi dan sosial media
dict['Hobi 2'] = ('Memasak')
dict['Sosial media 2'] = ('Twitter : @halidyash6')

#menghapus dua makanan favorit
del dict['Makanan Favorit 1']
del dict['Makanan Favorit 2']

#menambah satu hobi
dict['Hobi 4'] = ('Mendengarkan lagu')

#mencetak hasil
print(dict)
