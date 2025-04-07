
def inputenz (diz):

    #la funzione chiede l'inserimento di un enzima gia presente nel csv, una volta inserito
    #la funzione controlla la sua presenza
    
    while True:
        selectedEnzyme = input("Inserire l'enzima di interesse : ")
        if selectedEnzyme in diz :
            print(f"hai scelto l'enzima {selectedEnzyme} : {diz[selectedEnzyme]}")
            return selectedEnzyme, diz[selectedEnzyme]



def controllaInputDna (sequenza):
    caratteri = "ACGT"

    for carattere in caratteri :
        sequenza = sequenza.replace(carattere, "")

    return len(sequenza) == 0


def inputdna ():
    while True:
        mydna = input("inserire il filamento di dna (in maiuscolo) : ")
        if controllaInputDna(mydna):
            return mydna
        else :
            print("la sequenza inserita contiene caratteri inusuali")


