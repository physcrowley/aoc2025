from files import files

day = 3
test = False

source, output = files(day, test)

def part_one():
    with open(source, "r") as s:
        banks = map(lambda x : x.strip(), s.readlines())
    joltages = []
    for bank in banks:
        if len(bank) == 0:
            joltages.append(0)
            continue
        if len(bank) < 3:
            joltages.append(int(bank))
            continue
        best_joltage = bank[:2]
        for i in range(1,len(bank)):
            if bank[i] > best_joltage[0] and i != (len(bank) - 1):
                best_joltage = bank[i:i+2]
                continue
            if bank[i] > best_joltage[1]:
                best_joltage = best_joltage[0] + bank[i]                  
        joltages.append(int(best_joltage))
    total = 0
    for j in joltages:
        total += j
    result = f"total={total} from {joltages}"
    print(f"total={total} from {joltages}")
    with open(output, "w", encoding="utf-8") as o:
        o.write(result)


part_one()
