from .base import *

class LRU(IPageReplacement):
    def __init__(self, capacity, verbose=False):
        super().__init__(capacity, verbose)
        self.pageIndices = {}  # Para rastrear o índice mais recente de uso das páginas

    def findReplacementIndex(self, pages, idx):
        oldestPage = min(self.pageIndices, key=self.pageIndices.get)
        return self.memory.index(oldestPage)

    def accessPage(self, page, pages, idx):
        """Acessa uma página, atualizando seus índices de uso."""
        if page not in self.memory:
            if len(self.memory) < self.capacity: self.memory.append(page)
            else:
                # Encontra o índice para substituição
                replaceIdx = self.findReplacementIndex(pages, idx)

                # Remove a página antiga dos índices
                oldPage = self.memory[replaceIdx]
                self.memory.pop(replaceIdx)
                self.memory.insert(replaceIdx, page)

                # Remove a página substituída do dicionário de índices
                if oldPage in self.pageIndices: del self.pageIndices[oldPage]
                
            # Incrementa a contagem de page faults
            self.page_faults += 1

        self.pageIndices[page] = idx  # Atualiza o índice de acesso da página atual