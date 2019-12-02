import math
import unittest


class ElectricChain:
    def __init__(self, distance, max_height_array):
        self.pillar_distance = distance
        self.max_heights = max_height_array

    def calculate_longest_wire(self):
        wire_length = 0
        lowest_height = 1.0
        min_wire_len = self.hypotenuse(lowest_height, lowest_height)
        for pillar in range(len(self.max_heights) - 1):
            # calculate when both have max heights
            guess_max_to_max = self.hypotenuse(self.max_heights[pillar], self.max_heights[pillar+1])
            # calculate when one has min height
            if self.max_heights[pillar] > self.max_heights[pillar+1]:
                guess_min_to_max = self.hypotenuse(self.max_heights[pillar], lowest_height)
            else:
                guess_min_to_max = self.hypotenuse(lowest_height, self.max_heights[pillar+1])
            # now find which option is the biggest
            longest_wire_chunk = max(min_wire_len, guess_max_to_max, guess_min_to_max)
            wire_length += longest_wire_chunk
        return wire_length

    def hypotenuse(self, max_height_pillar1, max_height_pillar2):
        return math.sqrt(self.pillar_distance**2 + (max_height_pillar1 - max_height_pillar2)**2)


def main():
    chain = ElectricChain(4, [100, 2, 10, 2, 100])
    print(chain.calculate_longest_wire())


class TestAlgorithm(unittest.TestCase):

    def test_chain1(self):
        chain = ElectricChain(2, [3, 3, 3])
        answer = chain.calculate_longest_wire()
        self.assertEqual(round(answer, 2), 5.66)

    def test_chain2(self):
        chain = ElectricChain(100, [1, 1, 1, 1])
        answer = chain.calculate_longest_wire()
        self.assertEqual(round(answer, 2), 300)

    def test_chain3(self):
        chain = ElectricChain(4, [100, 2, 100, 2, 100])
        answer = chain.calculate_longest_wire()
        self.assertEqual(round(answer, 2), 396.32)


unittest.main()
main()
