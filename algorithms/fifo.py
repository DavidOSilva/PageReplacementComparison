from .base import *
from collections import deque

class FIFO(IPageReplacement):
    def __init__(self, capacity, verbose=False):
        super().__init__(capacity, verbose)
        self.queue = deque()  # Para rastrear a ordem de chegada das páginas

    def findReplacementIndex(self, pages, idx):
        oldestPage = self.queue.popleft()
        return self.memory.index(oldestPage)

    def accessPage(self, page, pages, idx):
        """Acessa uma página, adicionando-a à fila se necessário."""
        if page not in self.memory:
            super().accessPage(page, pages, idx)
            self.queue.append(page)