let_var = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def let_to_num(let):
    if let in let_var:
        return int(let_var.index(let) + 10)
    else:
        return int(let)

def to_base_10(num):
    total = 0
    for i in range(0, len(num)):
        total += (starting_base**i)*let_to_num(num[i])
    print(f"total b10: {total}")
    return total

def to_targ_base(num):
    total = ''
    while num != 0:
        if num % end_base > 9:
            for i in range(0, len(let_var)):
                if i == (num % end_base)-10:
                    total += let_var[i]
        else:
            total += str(num % end_base)
        num = num // end_base
    total = total[::-1]
    print(f'total: {total}')

running = True
while running:
    init_number = input("what number do you want to convert? - ")
    init_number = init_number[::-1]

    starting_base = int(input("what base is your number in? - "))

    end_base = int(input("what base do you want to convert it to? - "))

    to_targ_base(to_base_10(init_number))
    ans = input('would you like to convert another number? (y/n) - ')
    if ans == 'y':
        pass
    else:
        running = False