import csv

def csv_to_dict():

    #la funzione si occupa di convertire il file csv in un dizionario 
    #le chiavi sono il nome dell'enzima mentre i valori sono la zona di restrizione
    
    filepath='enzymesequences.csv'
    diz={}
    with open(filepath,'r',encoding='utf-8') as csvfile:
      reader=csv.DictReader(csvfile) #lettura del file csv
      for row in reader:
        diz[row['Sequenza']] = row['Enzima'] #i nomi sono le chiavi
    return diz
