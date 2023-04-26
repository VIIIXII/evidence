from pojistenec import Pojistenec


class Evidence:
    vyber = 0
    dalsi_zaznam = 1

    def __init__(self):
        self.evidence = []

    def vyber_akci(self):
        """Spustí akci podle zadaného čísla uživatelem."""

        while self.vyber != 4:
            try:
                if self.vyber != 4:
                    self.vyber = int(input("Vyberte si akci:"
                                           "\n1 - Přidat nového pojištěného"
                                           "\n2 - Vypsat všechny pojištěné"
                                           "\n3 - Vyhledat pojištěného"
                                           "\n4 - Konec\n"))

                    if self.vyber == 1:
                        return self.pridej_pojistene()
                    elif self.vyber == 2:
                        self.vypis_pojistene()
                    elif self.vyber == 3:
                        self.najdi_pojistene()
                    elif self.vyber == 4:
                        print("\nPřejeme hezký den.")
                    else:
                        print("\nZadejte platné číslo operace [1 - 4]:\n")
            except ValueError:
                print("\nZadejte platné číslo operace [1 - 4]:\n")

    def nacti_jmeno_prijmeni(self, zadani, text_chyby):
        """Načítá a kontroluje správnost zadání jména a příjmení."""
        chybne_zadani = True
        while chybne_zadani:
            zadany_text = str(input(zadani))
            if len(str(zadany_text)) < 2 or len(str(zadany_text)) > 30:
                print("\nJméno nebo příjmení musí být v rozsahu 2 až 30 písmen. Opakujte zadání.\n")
            elif not zadany_text.isalpha():
                print(text_chyby)
            else:
                return zadany_text

    def nacti_vek(self, zadani, text_chyby):
        """Načítá a kontroluje správnost zadání věku."""

        chybny_vek = True
        while chybny_vek:
            try:
                zadany_vek = int(input(zadani))
                if zadany_vek < 0:
                    print("\nVěk musí být kladným číslem. Opakujte zadání.\n")
                    continue
                chybny_vek = False
            except ValueError:
                print(text_chyby)
            else:
                return zadany_vek

    def nacti_telefon(self, zadani, text_chyby):
        """Načítá a kontroluje správnost zadání telefonního čísla."""
        chybny_telefon = True
        while chybny_telefon:
            try:
                zadany_telefon = int(input(zadani))
                if len(str(zadany_telefon)) != 9:
                    print("\nTelefonní číslo musí být uvedeno ve správném tvaru (123456789). Opakujte zadání.\n")
                    continue
                chybny_telefon = False
            except ValueError:
                print(text_chyby)
            else:
                return zadany_telefon

    def pokracuj(self):
        print(input("\nPokračujte stiskem klávesy ENTER..."))
        self.vyber_akci()

    def pridej_pojistene(self):
        """Přidá pojištěnce do evidence."""

        jmeno = self.nacti_jmeno_prijmeni("Zadejte jméno nového pojištěnce: ",
                                          "\nPovoleny jsou pouze znaky abecedy.\n").capitalize()
        prijmeni = self.nacti_jmeno_prijmeni("Zadejte příjmení nového pojištěnce: ",
                                             "\nPovoleny jsou pouze znaky abecedy.\n").capitalize()
        vek = self.nacti_vek("Zadejte věk pojištěnce: ", "Zadávejte pouze číselné znaky.")
        telefon = self.nacti_telefon("Zadejte telefonní číslo pojištěnce: ", "\nZadávejte pouze číselné znaky.\n")

        self.evidence.append(Pojistenec(jmeno, prijmeni, vek, telefon))
        self.dalsi_zaznam += 1
        print("\nData byla uložena.")

        self.pokracuj()

    def vypis_pojistene(self):
        """Vypíše všechny uložené pojištěné v evidenci."""

        print("Seznam pojištěných:\n")
        for pojisteny in self.evidence:
            print(
                str(f"{pojisteny._jmeno} {pojisteny._prijmeni}\t\tvěk: {pojisteny._vek}\t\ttelefon: {pojisteny._telefon}"))
        print(f"Počet pojištěných v databázi: {self.dalsi_zaznam - 1}")

        self.pokracuj()

    def najdi_pojistene(self):
        """Hledá konkrétní pojištěné podle jména a příjmené a vypíše jejich data."""

        jmeno = str(input("Zadejte jméno pojištěného: \n").capitalize())
        prijmeni = str(input("Zadejte příjmení pojištěného: \n").capitalize())
        najdi = [hledany for hledany in self.evidence if hledany._jmeno == jmeno and hledany._prijmeni == prijmeni]
        for hledany in najdi:
            print("\nNalezeno:")
            print(f"{hledany._jmeno} {hledany._prijmeni}\t\tvěk: {hledany._vek}\t\ttelefon: {hledany._telefon}")
        if len(najdi) < 1:
            print("\nNebyl nalezen žádný záznam.\n")

        self.pokracuj()
