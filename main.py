from algorithms.optimal import Optimal
from algorithms.lru import LRU
from algorithms.fifo import FIFO

def runOptimal(pages, capacity):
    print("Optimal Page Replacement Algorithm")
    print(f'Page Reference: {pages}')
    optimal = Optimal(capacity)
    optimalFaults = optimal.run(pages)
    print(f"Total Page Faults (Optimal): {optimalFaults}\n")

def runOthers(pages, capacity):
    print("LRU Page Replacement Algorithm")
    print(f'Page Reference: {pages}')
    lru = LRU(capacity)
    lruFaults = lru.run(pages)
    print(f"Total Page Faults (LRU): {lruFaults}\n")

    print("FIFO Page Replacement Algorithm")
    print(f'Page Reference: {pages}')
    fifo = FIFO(capacity)
    fifoFaults = fifo.run(pages)
    print(f"Total Page Faults (FIFO): {fifoFaults}\n")

def compare(pages, capacity):
    runOptimal(pages, capacity)
    runOthers(pages, capacity)

if __name__ == "__main__":
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 0, 1, 7, 0, 1]
    capacity = 3
    #runOptimal(pages, capacity)
    compare(pages, capacity)
