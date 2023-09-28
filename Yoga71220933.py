# contoh
nama = input('Masukan nama lengkap Anda: ')
umur = input('Masukan umur anda:')
print('1. laki-laki  ')
print('2. perempuan  ')
operasi = input('Pilih jenis kelamin anda(1/2): ')
nomortelpon = input('nomor telpon:')
email = input('email anda:')
print('------------------------------------------------')
print('nama:             ', nama,'')
print('umur:             ', umur,'')
if operasi == '1':
    print('jenis kelamin:     laki-laki')
elif operasi == '2':
    print('jenis kelamin:     perempuan')
print('nomor telpon:     ', nomortelpon,'')
print('email:            ', email,'')
print('------------------------------------------------')