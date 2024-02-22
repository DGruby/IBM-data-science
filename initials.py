def main():
    name = input("Imię i nazwisko: ")
    first_name = name.split()[0]
    last_name = name.split()[1]
    age = input("Wiek: ")
    code = f"{first_name[0]}{last_name[0]}{age}"
    diesease = input("Choroba: ")
    print(f"DANE PACJENTA\n\n\tImię: {first_name}\n\tNazwisko: {last_name}\n\tWiek: {age}\n\tChoroba: {diesease}\n\tKod pacjenta: {code}")

if __name__ == "__main__":
    main()
    