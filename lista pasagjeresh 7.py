
pasagjeret_fillestare = ["Ana", "Leo", "Miri", "Ardit", "Renea", "Jord", "Elvira"]
file_name = "pasagjere.txt"


def ruaj_ne_file(lista):
    with open(file_name, "w") as f:
        for p in lista:
            f.write(p + "\n")


pasagjere = []

try:
    with open(file_name, "r") as f:
        for line in f:
            emri = line.strip()
            if emri != "":
                pasagjere.append(emri)

    if len(pasagjere) == 0:
        pasagjere = pasagjeret_fillestare.copy()
        ruaj_ne_file(pasagjere)

except FileNotFoundError:
    pasagjere = pasagjeret_fillestare.copy()
    ruaj_ne_file(pasagjere)


while True:
    print("\n--- Airline Reservation Menu ---")
    print("1. Shfaq pasagjerët")
    print("2. Kontrollo rezervim")
    print("3. Shto pasagjer")
    print("4. Hiq pasagjer")
    print("5. Statistika")
    print("6. Dil")

    zgjedhja = input("Zgjidh opsionin (1-6): ")

    if zgjedhja == "1":
        if len(pasagjere) == 0:
            print("Nuk ka pasagjerë.")
        else:
            for p in pasagjere:
                print("-", p)

    elif zgjedhja == "2":
        emri = input("Shkruaj emrin: ").strip().capitalize()
        if emri in pasagjere:
            print("Rezervimi u gjet për", emri)
        else:
            print("Nuk u gjet rezervim.")

    elif zgjedhja == "3":
        emri = input("Shkruaj emrin e pasagjerit: ").strip().capitalize()

        if emri == "":
            print("Emri nuk mund të jetë bosh.")
        elif emri in pasagjere:
            print("Pasagjeri ekziston tashmë.")
        else:
            pasagjere.append(emri)
            ruaj_ne_file(pasagjere)
            print("Pasagjeri u shtua dhe u ruajt automatikisht.")

    elif zgjedhja == "4":
        emri = input("Shkruaj emrin për ta hequr: ").strip().capitalize()
        if emri in pasagjere:
            pasagjere.remove(emri)
            ruaj_ne_file(pasagjere)
            print("Pasagjeri u hoq dhe u ruajt automatikisht.")
        else:
            print("Emri nuk u gjet.")

    elif zgjedhja == "5":
        print("Numri total i pasagjerëve:", len(pasagjere))

    elif zgjedhja == "6":
        print("Programi u mbyll.")
        break

    else:
        print("Opsion i pavlefshëm.")


