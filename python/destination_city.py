#no. 1436
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start, end = paths[0][0], paths[0][1]
        del paths[0]
        while(paths):
            for i, path in enumerate(paths):
                if path[0] == end:
                    end = path[1]
                    del paths[i]
                    break
            for i, path in enumerate(paths):
                if path[1] == start:
                    start = path[0]
                    del paths[i]
                    break
        return end
