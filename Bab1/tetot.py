"""Bagels, by Al Sweigart al@inventwithpython.com
A deductive logic game where you must guess a number based on clues.
View this code at https://nostarch.com/big-book-small-python-projects
A version of this game is featured in the book "Invent Your Own
Computer Games with Python" https://nostarch.com/inventwithpython
Tags: short, game, puzzle"""

import random
DIGITS = 3 #ini jumlah digitnya
MAX_TEBAK = 10 #maksimum tebakan

def main():
    print('''Permainan ini diadaptasi dari permainan Bagels, Sebuah Permainan Logika Deduktif oleh Al Sweigart al@inventwithpython.com
    Saya memikirkan sebuah angka. Berikut adalah petunjuk-petunjuk mengenai angka tersebut:
    Ketika saya jawab:        Artinya:
    WADUH                      Satu digit benar tapi di posisi yang salah.
    OKRE                     Satu digit benar dan di posisi yang benar.
    TETOT                    Tidak ada yang benar.

    Sebagai contoh, jika angka rahasianya adalah 248 dan tebakan kamu adalah 843, maka saya akan teriak FERMI PICO.'''.format(DIGITS))
    while True: #Loop permainan utama.
        #men-generate angka rahasia yang akan ditebak oleh pemain:
        angkaRahasia = ambilAngkaRahasia()
        print('Saya memikirkan sebuah angka.')
        print(' Kamu punya {} kesempatan menebaknya.'.format(MAX_TEBAK))
        
        kesempatanTebak = 1
        while kesempatanTebak <= MAX_TEBAK:
            tebak = ''
            #tetap berulang hingga menjawab dengan benar:
            while len(tebak) != DIGITS or not tebak.isdecimal():
                print('Tebakan #{}: '.format(kesempatanTebak))
                tebak = input('> ')

            petunjuk = ambilPetunjuk(tebak, angkaRahasia)
            print(petunjuk)
            kesempatanTebak += 1
                
            if tebak == angkaRahasia:
                break #karena jawabannya benar maka perulangan berhenti.
            if kesempatanTebak > MAX_TEBAK:
                print('Sayang banget, kamu sudah kehabisan kesempatan menebak.')
                print('Angka rahasianya adalah {}.'.format(angkaRahasia))
                
        
        #tanyakan pemain apakah mereka mau main lagi atau tidak
        print('Kamu mau coba bermain lagi? (ya atau tidak)')
        if not input('>').lower().startswith('y'):
            break
    print('Terima kasih sudah bermain!')

def ambilAngkaRahasia():
    """Mengembalikan nilai string yang tersusun dari varibel DIGITS angka acak sekaligus unik."""
    angka = list('0123456789') #Membuat susunan angka dari 0 hingga 9.
    random.shuffle(angka) #menyusun angka dengan urutan acak.

    #ambil angka pertama dari variabel DIGITS dari list angka rahasia:
    angkaRahasia =''
    for i in range(DIGITS):
        angkaRahasia += str(angka[i])
    return angkaRahasia

def ambilPetunjuk(tebak, angkaRahasia):
    """Mengembalikan nilai string berupa petunjuk PICO, FERMI, BAGELS untuk tebakan dan pasangan angka rahasia."""
    if tebak == angkaRahasia:
        return 'Wah kamu benar!'

    petunjuk = []

    for i in range(len(tebak)):
        if tebak[i] == angkaRahasia[i]:
            #angka yang benar pada tempat yang benar.
            petunjuk.append('Okre')
        elif tebak[i] in angkaRahasia:
            #angka yang benar pada tempat yang salah.
            petunjuk.append('Waduh')
    if len(petunjuk) == 0:
        return 'Tetot' #Tidak ada yang benar baik angka maupun tempat.
    else:
        #urut petunjuk menjadi urutan alfabet sebagaimana urutan aslinya
        #jangan memberikan info apa2.
        petunjuk.sort()
        #buat satu string dari list string petunjuk.
        return ' '.join(petunjuk)

#jika program berjalan, jalankan permainan:
if __name__ == '__main__':
    main()