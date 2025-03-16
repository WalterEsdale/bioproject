
def inputenz (diz):

    #la funzione chiede l'inserimento di un enzima gia presente nel csv, una volta inserito
    #la funzione controlla la sua presenza
    
    while True:
        selectedEnzyme = input("Inserire l'enzima di interesse : ")
        if selectedEnzyme in diz :
            print(f"hai scelto l'enzima {selectedEnzyme} : {diz[selectedEnzyme]}")
            return selectedEnzyme, diz[selectedEnzyme]


def inputdna ():
    mydna = input("inserire il filamento di dna : ")
    return mydna


