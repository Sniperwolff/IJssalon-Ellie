def presenteer(dictionary, totaal):
    
    for product, prijs in dictionary.items():
        print(f"{product} : {prijs} euro")
    
    print("=" * 20)
    
    print(f"totaal : {totaal} euro")