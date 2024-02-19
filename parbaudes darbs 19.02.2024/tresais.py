# Izveidot Python programmu, kas nolasītu un izdrukātu trešās un ceturtās teksta faila rindas saturu.
def lasit_rindas(fails):
    with open(fails, 'r') as f:
        rindas = f.readlines()
        if len(rindas) >= 4:
            tresa_rinda = rindas[2].strip()
            ceturta_rinda = rindas[3].strip()
            print("Tresa rinda:", tresa_rinda)
            print("Ceturta rinda:", ceturta_rinda)
        else:
            print("Faila nav pietiekami daudz rindu.")

if __name__ == "__main__":
    fails = "pirmais.txt"
    lasit_rindas(fails)
