from files import files

day = 1
test = True

source, output = files(day, test)

zeros = 0
starting_pointer = 50
highest = 99


def spin(pointer, instruction, start=False):
    global zeros

    sign = instruction[:1]
    step = int(instruction[1:])

    if pointer == 0 and not start:
        zeros += 1
    if step == 0:
        return pointer
                
    if sign == "L":
        if pointer == 0:
            return spin(highest, sign + str(step - 1))
        if step < pointer:
            return pointer - step
        step -= pointer
        return spin(0, "L" + str(step))

    if sign == "R":
        if pointer == highest:
            return spin(0, sign + str(step - 1))
        delta = highest - pointer
        if step < delta:
            return pointer + step
        step -= delta
        return spin(highest, "R" + str(step))



def main():
    pointer = starting_pointer
    stopped_on_zero = 0

    with open(source, "r") as s:
        for ins in s.readlines():
            start0 = zeros
            ins = ins.strip()
            pointer = spin(pointer, ins, start=True)
            if pointer == 0:
                stopped_on_zero += 1            
            delta0 = zeros - start0
            # print(pointer, delta0)

    with open(output, "w", encoding="utf-8") as o:
        o.write(f"Fin est zero : {stopped_on_zero}, Tous les zéros passés : {zeros}")


main()
