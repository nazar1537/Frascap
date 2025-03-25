import base64
import hashlib

def szyfr_cezara(tekst, przesuniecie=3):
    wynik = ""
    for znak in tekst:
        if znak.isalpha():
            baza = 65 if znak.isupper() else 97
            wynik += chr((ord(znak) - baza + przesuniecie) % 26 + baza)
        else:
            wynik += znak
    return wynik

def koduj_base64(tekst):
    zakodowane_bajty = base64.b64encode(tekst.encode("utf-8"))
    return zakodowane_bajty.decode("utf-8")

def dekoduj_base64(tekst_zakodowany):
    odkodowane_bajty = base64.b64decode(tekst_zakodowany.encode("utf-8"))
    return odkodowane_bajty.decode("utf-8")

def szyfr_md5(tekst):
    return hashlib.md5(tekst.encode()).hexdigest()

def szyfr_sha256(tekst):
    return hashlib.sha256(tekst.encode()).hexdigest()

def menu():
    print("==============================")
    print("     PROGRAM SZYFRUJĄCY     ")
    print("==============================")
    print("1. Szyfr Cezara")
    print("2. Base64")
    print("3. MD5")
    print("4. SHA-256")
    print("5. Wyjście")
    print("==============================")

if __name__ == "__main__":
    while True:
        menu()
        wybor = input("Wybierz metodę szyfrowania: ")
        
        if wybor == "5":
            print("Zamykanie programu...")
            break
        
        tekst = input("Wpisz tekst do zaszyfrowania: ")
        
        if wybor == "1":
            przesuniecie = int(input("Podaj przesunięcie dla Cezara (domyślnie 3): ") or 3)
            zaszyfrowany_tekst = szyfr_cezara(tekst, przesuniecie)
            print(f"Zaszyfrowany tekst (Cezar): {zaszyfrowany_tekst}")
        elif wybor == "2":
            zaszyfrowany_tekst = koduj_base64(tekst)
            print(f"Zaszyfrowany tekst (Base64): {zaszyfrowany_tekst}")
            print(f"Odszyfrowany tekst (Base64): {dekoduj_base64(zaszyfrowany_tekst)}")
        elif wybor == "3":
            zaszyfrowany_tekst = szyfr_md5(tekst)
            print(f"Zaszyfrowany tekst (MD5): {zaszyfrowany_tekst}")
        elif wybor == "4":
            zaszyfrowany_tekst = szyfr_sha256(tekst)
            print(f"Zaszyfrowany tekst (SHA-256): {zaszyfrowany_tekst}")
        else:
            print("Nieprawidłowy wybór! Spróbuj ponownie.")
#szeben 
