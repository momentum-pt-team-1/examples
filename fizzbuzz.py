# numbers 1 - 100
# divisible by 3 -> 'Pling'
# divisible by 5 -> 'Plang'
# divisible by 7 -> 'Plong'
# else, print out the number
# TODO handle numbers divisible by more than one of (3, 5, 7)

def rainbow():
    for i in range(1, 101):
        pling = "Pling"
        plang = "Plang"
        plong = "Plong"
        
        if i >= 105 and i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
            print(i, pling + plang + plong)
        elif i % 5 == 0 and i % 7 == 0:
            print(i, plang + plong)
        elif i % 3 == 0 and i % 5 == 0:
            print(i, pling + plang)
        elif i % 3 == 0 and i % 7 == 0:
            print(i, pling + plong)
        elif i % 3 == 0:
            print(i, pling)
        elif i % 5 == 0:
            print(i, plang) 
        elif i % 7 == 0:
            print(i, plong)
        else:
            print(i)

rainbow()


