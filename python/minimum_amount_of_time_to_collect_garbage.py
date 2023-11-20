# no.2391
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        glass, paper, metal = [], [], []
        for i, g in enumerate(garbage):
            for j in g:
                if j == 'G':
                    glass.append(i)
                if j == 'P':
                    paper.append(i)
                if j == 'M':
                    metal.append(i)
        glass_time, metal_time, paper_time = len(glass), len(metal), len(paper)
        glass_time = glass_time + sum(travel[0:glass[-1]]) if glass else 0
        metal_time = metal_time + sum(travel[0:metal[-1]]) if metal else 0
        paper_time = paper_time + sum(travel[0:paper[-1]]) if paper else 0
        print(glass_time, metal_time, paper_time)
        return glass_time + metal_time + paper_time
