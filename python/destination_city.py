#no. 1436
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        route = [paths[0]]
        del paths[0]
        while(paths):
            for i, path in enumerate(paths):
                if path[0] == route[-1][1]:
                    route.append(path)
                    del paths[i]
                    break
            for i, path in enumerate(paths):
                if path[1] == route[0][0]:
                    route.insert(0, path)
                    del paths[i]
                    break
        return route[-1][1]
