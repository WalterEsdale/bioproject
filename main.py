from csvconverter import csv_to_dict
from input import inputenz, inputdna
from restrictionsite import ricercazona

if __name__ == "__main__":

    output = []

    print("\nbenvenuto nel programma DNAcut\n")

    enzdict = csv_to_dict() #dizionario enzimi

    myenz = inputenz(enzdict) #scelta enzima, #myenz è un vettore che contiene sia il nome che l'area di interesse
    
    mydna = inputdna() #inserimento dna 

    output = ricercazona(myenz, mydna)

    if output is None:
        print("\nSiti di restrizione : 0")
        print("il filamento di Dna non ha siti di restrizione compatibili con l'enzima scelto")
    else:
        print("\nSiti di restrizione : ", end="")
        print(len(output))
        for sito in output:
            print(sito)
    print()