from typing import List


def flipAndInvertImage(image: List[List[int]]) -> List[List[int]]:
    for i in range(len(image)):  # rows
        image[i] = image[i][::-1]  # flipping each row
        for n in range(len(image[0])):  # iterating thru each row element
            if image[i][n] == 1:  # inverting
                image[i][n] = 0
            else:
                image[i][n] = 1
    return image


image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
print(flipAndInvertImage(image))
