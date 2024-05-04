class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_int = version1.split(".")
        version2_int = version2.split(".")

        length = max(len(version1_int), len(version2_int))

        for i, s in enumerate(version1_int):
            version1_int[i] = int(s)

        for i in range(len(version1_int), length, 1):
            version1_int.append(0)

        for i, s in enumerate(version2_int):
            version2_int[i] = int(s)

        for i in range(len(version2_int), length, 1):
            version2_int.append(0)

        for i in range(length):
            if version1_int[i] == version2_int[i]:
                continue

            if version1_int[i] < version2_int[i]:
                return -1

            return 1

        return 0
