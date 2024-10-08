from abc import ABC, abstractmethod

class IPageReplacement(ABC):
    def __init__(self, capacity, verbose=False):
        self.capacity = capacity
        self.memory = []
        self.page_faults = 0
        self.verbose = verbose  # Flag para controle da impressão do passo a passo

    @abstractmethod
    def findReplacementIndex(self, pages, idx):
        """ Encontra o índice da página que será substituída. """
        pass

    def accessPage(self, page, pages, idx):
        """Acessa uma página e realiza substituição se necessário."""
        if page not in self.memory:
            if len(self.memory) < self.capacity:
                self.memory.append(page)
            else:
                replaceIdx = self.findReplacementIndex(pages, idx)  # Encontra o índice para substituição
                # Remove a página no índice encontrado e insere a nova página no mesmo local
                self.memory.pop(replaceIdx)
                self.memory.insert(replaceIdx, page)

            self.page_faults += 1

    def run(self, pages, verbose=None):
        """Executa o algoritmo de substituição de páginas."""
        if verbose is not None: self.verbose = verbose  # Permite ajustar a flag durante a execução

        for i, page in enumerate(pages):
            self.accessPage(page, pages, i)
            if self.verbose:
                self._print_state(page, i)

        return self.page_faults

    def _print_state(self, page, step):
        print(f"Step {step + 1}: Reference Page: {page}, Memory: {self.memory}, Page Faults: {self.page_faults}")
