#def decoreer (tekst=""):
#    lengte = len (tekst) + 4
#    print ()
#    print (lengte * "*")
#    print (f"* {tekst} *")
#    print (lengte * "*")
#    print ()

#def fooi_pp(bedrag, personen):
#    try:
#        bedrag_pp = bedrag / personen
#        return f"Het bedrag per persoon is {bedrag_pp:.2f} euro."
#    except ZeroDivisionError:
#        return "Het aantal personen kan niet 0 zijn."
#    except Exception as e:
#        return f"Er is een fout opgetreden: {e}"

#b = int(input("Welk bedrag zit er in de fooienpot? "))
#p = int(input("Over hoeveel mensen moet de pot verdeeld worden? "))

#print(fooi_pp(b, p))

def onderstreep(tekst=""):
    uit=[]
    uit.append(tekst)
    uit.append(len(tekst) * "=")
    return uit

    
def som(inkomsten):
    totaal = 0
    for waarde in inkomsten.values():
        if isinstance(waarde, (int, float)): 
            totaal += waarde
        else:
            print(f"Waarschuwing: {waarde} is geen getal en wordt overgeslagen.")
    return totaal    