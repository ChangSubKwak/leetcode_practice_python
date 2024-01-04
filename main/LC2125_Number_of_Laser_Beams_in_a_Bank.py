from typing import List


class LC2125_Number_of_Laser_Beams_in_a_Bank:
    def numberOfBeams(self, bank: List[str]) -> int:
        lineCount = [0] * len(bank)
        existBeamCount = 0

        for i in range(len(bank)):
            count = 0
            for j in list(bank[i]):
                if j == "1":
                    count += 1
            if count > 0:
                existBeamCount += 1
            lineCount[i] = count

        if existBeamCount <= 1:
            return 0

        i = 0
        while i < len(lineCount):
            if lineCount[i] == 0:
                del lineCount[i]
                continue
            i += 1

        result = 0
        for i in range(len(lineCount) - 1):
            result += lineCount[i] * lineCount[i + 1]

        return result
