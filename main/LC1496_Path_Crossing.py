class Solution:
    def isPathCrossing(self, path: str) -> bool:
        s = set()

        y, x = 0, 0
        s.add(f'{y}_{x}')

        for direction in path:
            if direction == 'N':
                y -= 1
            if direction == 'S':
                y += 1
            if direction == 'E':
                x -= 1
            if direction == 'W':
                x += 1

            currentPosition = f'{y}_{x}'

            if currentPosition in s:
                return True

            s.add(currentPosition)

        return False
