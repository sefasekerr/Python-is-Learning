from tabu import tabu_baslat
from _2048oyunu import baslat
def oyun_secimi():
    secenek= input(f"hangi oyunu oynamak isterseniz\n1-2048 oyunu\n2-Tabu oyunu\n")
    match secenek:
        case "1":
            baslat(callback=oyun_secimi)
            
        case"2":
            tabu_baslat(callback=oyun_secimi)
            