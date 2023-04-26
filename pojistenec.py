class Pojistenec:
    """K vytvoření dat nového pojištence."""

    def __init__(self, jmeno, prijmeni, vek, telefon):
        self._jmeno = jmeno
        self._prijmeni = prijmeni
        self._vek = vek
        self._telefon = telefon

    def __str__(self):
        return f"{self._jmeno}, {self._prijmeni}, {self._vek}, {self._telefon}"
