def controllaInputEnz (enz):
    #le informazioni sul csv degli enzimi con i numeri non so come implementarle nel programma quindi vengono scartate
    #insieme a quelle che non hanno lo / per individuare la posizione precisa del taglio 

    has_numbers = any(char.isdigit() for char in enz[1])
    
    if has_numbers:
        print("has numbers")
        return False
    else :
        if '/' in enz:
            return True
        else :
            print("no /")
            return False


def inputenz (diz):

    #la funzione chiede l'inserimento di un enzima gia presente nel csv, una volta inserito
    #la funzione controlla la sua presenza
    
    while True:
        selectedEnzyme = input("Inserire l'enzima di interesse : ")
        if selectedEnzyme in diz and controllaInputEnz(diz[selectedEnzyme]):
            print(f"hai scelto l'enzima {selectedEnzyme} : {diz[selectedEnzyme]}")
            return selectedEnzyme, diz[selectedEnzyme]



def controllaInputDna (sequenza):
    caratteri = "ACGT"

    for carattere in caratteri :
        sequenza = sequenza.replace(carattere, "")

    return len(sequenza) == 0


def inputdna ():
    while True:
        mydna = input("\ninserire il filamento di dna (in maiuscolo) : ")
        if controllaInputDna(mydna):
            return mydna
        else :
            print("la sequenza inserita contiene caratteri inusuali")


