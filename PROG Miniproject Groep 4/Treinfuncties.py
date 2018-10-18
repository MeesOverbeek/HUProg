def standaardprijs(afstandKM):
    if afstandKM < 0:
        afstandKM = 0

    if afstandKM < 50:
        prijs = afstandKM * 0.80
    else:
        prijs = 15 + afstandKM * 0.60

    return prijs