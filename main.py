from csvconverter import csv_to_dict
from input import inputenz, inputdna
from restrictionsite import trova_siti_restrizione

if __name__ == "__main__":

    print()
    print("benvenuto nel programma DNAcut")
    print()

    enzdict = csv_to_dict() #dizionario enzimi

    myenz = inputenz(enzdict) #scelta enzima, #myenz è un vettore che contiene sia il nome che l'area di interesse
    
    mydna = inputdna() #inserimento dna 

    output = trova_siti_restrizione(myenz, mydna)

    print(output)