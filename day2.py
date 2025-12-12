from files import files
from typing import List

day = 2
test = True

source, output = files(day, test)

with open(source, "r") as s:
    data = s.readline().strip().split(",")

all_ids: List[str] = []
for r in data:
    start_t, end_t = r.split("-")
    for n in range(int(start_t), int(end_t) + 1):
        all_ids.append(str(n))

def part_one():
    invalid_ids: List[int] = []
    total = 0
    for i in all_ids:
        if len(i) % 2 != 0: # impossible à diviser également en 2
            continue
        mid = len(i) // 2 # division entière
        if i[:mid] == i[mid:]:
            val = int(i)
            invalid_ids.append(val)
            total += val

    with open(output, "w", encoding="utf-8") as o:
        o.write(f"Duplicate digits : {total} from {invalid_ids[:20]}")

def part_two():
    total = 0
    parts = {
        2: [1],
        3: [1],
        4: [1,2],
        5: [1],
        6: [1,2,3],
        7: [1],
        8: [1,2,4],
        9: [1,3],
        10: [1,2,5],
    } # diviseurs possibles selon la longeur de la chaîne
    truly_invalid_ids: List[int] = []
    for i in all_ids:
        if len(i) < 2:
            continue
        for p in parts[len(i)]: # utiliser la longueur comme clé dans parts
            val = int(i)
            if val in truly_invalid_ids: # match déjà avec une plus petite partie
                break
            ref = i[:p] # première séquence de p chiffres
            seq_of_ref = True
            for j in range(p, len(i) - p + 1, p):
                if i[j:j+p] != ref:   # pas la même chose
                    seq_of_ref = False
                    break
            if seq_of_ref: # traversé sans passer par le chemin False
                truly_invalid_ids.append(val)
                total += val
    
    with open(output, "a", encoding="utf-8") as o:
        o.write("\n")
        o.write(f"Repeating sequences : {total} from {truly_invalid_ids[:30]}")

part_one()
part_two()
