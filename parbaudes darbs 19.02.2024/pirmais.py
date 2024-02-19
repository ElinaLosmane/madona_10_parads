#Izveidot Python programmu, kas nolasītu un izdrukātu visu teksta faila saturu (txt formātā).
def lasit_teksta_failu(nosaukums):
    try:
        with open(nosaukums, 'r') as f:
            saturs = f.read()
            print(saturs)
    except FileNotFoundError:
        print("Noraditais fails nav atrasts.")
    except Exception as e:
        print("Radas kluda:", e)

# Testa izpildes piemērs
faila_nosaukums = "pirmais.txt"
lasit_teksta_failu(faila_nosaukums)
