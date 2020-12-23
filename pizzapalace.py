import os
import time


with open("upgrades.txt") as f:
    upgrades = f.readlines()

# Iterates over a sequence seq in size-big chunks
def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

levels = int(input("How many levels?    "))

print("This script displays pizza patterns in chunks.")
print(">>> During the game, press Enter to navigate to the next chunk. <<<")
print("After the level concludes, a recommended upgrade will be displayed.")

for level in range(levels):
    n = int(input("How many pizza makers?    "))
    with open("./levels/" + str(level+1) + ".txt") as f:
        pizzas = f.read().splitlines()
    chunkNum = 1
    for chunk in chunker(pizzas, n):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('[' + str(chunkNum) + ']')
        for c in chunk:
            if '0' in c or '3' in c:
                print('\033[1m' + c + '\033[0m')
            else: print(c)
        chunkNum += 1
        input()
    print(upgrades[level])
