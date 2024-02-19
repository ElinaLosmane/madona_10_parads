#Izveidot Python programmu, kas nolasītu un izdrukātu tikai ceturtās kolonnas datus no CSV faila. 
import csv

def ceturtais_kolonnas_dati(csv_nosaukums):
    try:
        with open(csv_nosaukums, 'r') as f:
            lasitajs = csv.reader(f)
            for rinda in lasitajs:
                if len(rinda) >= 4:
                    print(rinda[3])
                else:
                    print("Rindai nav ceturtas kolonnas.")
    except FileNotFoundError:
        print("Noraditais fails nav atrasts.")
    except Exception as e:
        print("Radas kluda:", e)

# Testa izpildes piemērs
csv_faila_nosaukums = "otrais.csv"
ceturtais_kolonnas_dati(csv_faila_nosaukums)