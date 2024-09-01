from algorithms.optimal import Optimal
from algorithms.lru import LRU
from algorithms.fifo import FIFO

def runOptimal(pages, capacity, verbose=False):
    optimal = Optimal(capacity, verbose=verbose)
    return optimal.run(pages)

def runOthers(pages, capacity, verbose=False):
    lru, fifo = LRU(capacity, verbose=verbose), FIFO(capacity, verbose=verbose)
    lruFaults, fifoFaults = lru.run(pages), fifo.run(pages)
    return lruFaults, fifoFaults

def compare(page_lists, capacities):
    optimal_faults = {capacity: [] for capacity in capacities}
    lru_faults = {capacity: [] for capacity in capacities}
    fifo_faults = {capacity: [] for capacity in capacities}
    
    # Executa os testes para cada lista de páginas e cada capacidade
    for pages in page_lists:
        for capacity in capacities:
            optimal_faults[capacity].append(runOptimal(pages, capacity))
            lru, fifo = runOthers(pages, capacity)
            lru_faults[capacity].append(lru)
            fifo_faults[capacity].append(fifo)
    
    # Calcula e imprime a média dos resultados para cada capacidade
    print("Médias de Faltas de Página por Capacidade:")
    for capacity in capacities:
        avg_optimal_faults = sum(optimal_faults[capacity]) / len(optimal_faults[capacity])
        avg_lru_faults = sum(lru_faults[capacity]) / len(lru_faults[capacity])
        avg_fifo_faults = sum(fifo_faults[capacity]) / len(fifo_faults[capacity])
        print(f"Capacidade: {capacity}")
        print(f" Média de Faltas de Página (Ótimo): {avg_optimal_faults:.2f}")
        print(f" Média de Faltas de Página (LRU): {avg_lru_faults:.2f}")
        print(f" Média de Faltas de Página (FIFO): {avg_fifo_faults:.2f}")
        print("-" * 40)
    
    # Acumula todas as faltas para calcular a média geral
    all_optimal_faults = [fault for faults in optimal_faults.values() for fault in faults]
    all_lru_faults = [fault for faults in lru_faults.values() for fault in faults]
    all_fifo_faults = [fault for faults in fifo_faults.values() for fault in faults]
    avg_general_optimal_faults = sum(all_optimal_faults) / len(all_optimal_faults)
    avg_general_lru_faults = sum(all_lru_faults) / len(all_lru_faults)
    avg_general_fifo_faults = sum(all_fifo_faults) / len(all_fifo_faults)
    print("Médias Gerais de Faltas de Página:")
    print(f" Ótimo: {avg_general_optimal_faults:.2f}")
    print(f" LRU: {avg_general_lru_faults:.2f}")
    print(f" FIFO: {avg_general_fifo_faults:.2f}")
    print("-" * 40)

if __name__ == "__main__":
    pageLists = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        [2, 3, 2, 1, 4, 2, 5, 6, 7, 8, 5, 2, 3, 1, 4],
        [10, 20, 10, 30, 20, 10, 40, 50, 30, 10, 20, 40, 30, 20, 50],
        [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 0, 1, 7, 0, 1],
        [3, 4, 3, 2, 1, 2, 4, 5, 2, 1, 3, 4, 5, 6, 7],
        [5, 6, 5, 7, 8, 5, 9, 10, 6, 5, 8, 7, 9, 10, 11],
        [1, 2, 3, 4, 2, 5, 6, 4, 3, 7, 8, 6, 5, 4, 3]
    ]
    capacities = [2, 3, 4, 5]

    # Exemplo de como testar cada algoritmo, neste caso o ótimo.
    #runOptimal([7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 0, 1, 7, 0, 1], 3, True)

    # Exibe o comparativo considerando todas a capacidades e as listas de paginas de referência.
    compare(pageLists, capacities)
