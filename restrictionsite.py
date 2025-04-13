
def ricercazona(enz,dna):

    #la funzione immagazzina la posizione dello / nella area di interesse dell'enzima con la funzione .find
    #successivamente va a trovare la posizione (sempre con find) dell'area di interesse
    #infine con i due dati citati è in grado di stampare la zona precisa dove l'enzima taglia il filamento 

    zonevalide = []
    start = 0
    posiztaglio = enz[1].find("/")
    posiztaglio = posiztaglio + 1 #dato che inizia a contare da 0
    zonarestrizione = enz[1].replace('/', '')


    if zonarestrizione in dna:
        while start < len(dna):
            posizionezona = dna.find(zonarestrizione, start)
            if posizionezona == -1:
                break
            zonevalide.append(f"l'enzima {enz[0]} : {enz[1]} può eseguire un taglio nella posizione : {posizionezona + posiztaglio - 1} - {posizionezona + posiztaglio}")
            start = posizionezona + 1
        return zonevalide


