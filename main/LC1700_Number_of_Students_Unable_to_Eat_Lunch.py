from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i = 0

        while True:
            if i >= len(students):
                break

            if students[0] != sandwiches[0]:
                i += 1
                students = students[1:] + students[:1]
                continue

            if students[0] == sandwiches[0]:
                students = students[1:]
                sandwiches = sandwiches[1:]
                i = 0
                continue

        return len(students)