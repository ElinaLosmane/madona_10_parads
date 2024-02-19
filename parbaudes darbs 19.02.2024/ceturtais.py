def lasit_failu(nosaukums):
    try:
        with open(nosaukums, 'r') as fails:
            saturs = fails.read()
            print("Faila saturs:")
            print(saturs)
    except FileNotFoundError:
        print("Kluda: Fails '{}' netika atrasts.".format(nosaukums))
    except Exception as e:
        print("Kluda: Neparedzeta kluda:", e)

def main():
    nosaukums = input("Ievadiet faila nosaukumu: ")
    paplasinajums = input("Ievadiet faila paplasinajumu (piemeram, txt, csv, utt.): ")
    faila_pilns_nosaukums = "{}.{}".format(nosaukums, paplasinajums)
    lasit_failu(faila_pilns_nosaukums)

if __name__ == "__main__":
    main()
