from .base import *

class Optimal(IPageReplacement):
    def findReplacementIndex(self, pages, idx):
        farthestUse, replaceIdx = -1, 0
        for i, memPage in enumerate(self.memory):
            try: nextUse = pages[idx + 1:].index(memPage)
            except ValueError: nextUse = float('inf')  # Página não será usada novamente
            
            if nextUse > farthestUse:
                farthestUse = nextUse
                replaceIdx = i

        return replaceIdx
