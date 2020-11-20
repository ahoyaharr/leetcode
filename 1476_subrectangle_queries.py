from typing import List

class SubrectangleQueries:
    class Rectangle:
        def __init__(self, row1, col1, row2, col2, value):
            self.row1 = row1
            self.col1 = col1
            self.row2 = row2
            self.col2 = col2
            self.value = value

        def contains(self, x, y):
            print(f'{self.row1}<={x}<={self.row2} and {self.col1}<={y}<={self.col2}')
            return self.row1 <= x <= self.row2 and self.col1 <= y <= self.col2

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle
        self.updates = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        # Instead of updating the base rectangle, maintain a list of updates.
        # This method of updating is O(1) instead of O(n^2) but makes it longer to look a value up.
        self.updates.append(self.Rectangle(row1, col1, row2, col2, newValue))

    def getValue(self, row: int, col: int) -> int:
        # To find the value of a rectangle, walk through the list of updates backwards.
        # If no update is found, then it is a member of the base rectangle.
        # This method of getting the value of O(n) on the number of updates.
        for rectangle in self.updates[::-1]:
            if rectangle.contains(row, col):
                return rectangle.value
        return self.rectangle[row][col]