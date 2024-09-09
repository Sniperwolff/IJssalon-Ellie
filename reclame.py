def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting=prijs*0,9
    print(f"vandaag in de aanbieding: Emmertje ijs (1liter) in de smaak {smaak} ,van {prijs} euro voor {prijs_na_korting}")
    return print

def inkomsten_totaal(ma=220,di=430,wo=125,do=160,vr=205,za=90,zo=345):
    return ma+di+wo+do+vr+za+zo
inkomsten=inkomsten_totaal()
btw = inkomsten*0.09


print (f"het totaal van alle inkomsten van deze week is {inkomsten} euro, waarover{btw} euro btw betaald dient te worden.")

def laag_en_hoog(ma=220,di=430,wo=125,do=160,vr=205,za=90,zo=345):
    return ma+di+wo+do+vr+za+zo

mijn_lijst=laag_en_hoog()

print (mijn_lijst)

    

    

    


