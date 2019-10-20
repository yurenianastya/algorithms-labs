import math


class Farm:

    def __init__(self, boxes, crazy_cows):
        self.boxes = boxes
        self.crazy_cows = crazy_cows

    def generate_stables(self, boxes, crazy_cows, stables=[]):
        print("Crazy cows: ", crazy_cows, " Boxes: ", boxes)
        print("Insert boxes...")
        for element in range(0, boxes):
            stables.append(int(input()))
        stables.sort()
        return print("Available spaces: ", stables)

    def average_len(self, stables, crazy_cows):
        stables_length = stables[-1] - stables[0]
        average_length = math.trunc(stables_length / crazy_cows)
        return print("The expected average length is: ", average_length)

    def iterating_list(self, stables, average_length, crazy_cows):
        center = math.floor(len(stables)/2)
        crazy_cows_stable = [stables[0], stables[-1]]
        crazy_cows = crazy_cows - 2
        right_flag = -1
        right_flag1 = -2
        left_flag = 0
        left_flag1 = 1
        while crazy_cows > 0:
            for j in range(0, center-1, 1):  # left side loop
                if stables[left_flag1] - stables[left_flag] >= average_length:
                    crazy_cows_stable.append(stables[left_flag1])
                    left_flag = left_flag1
                    left_flag1 = left_flag1 + 1
                    crazy_cows = crazy_cows - 1
                    break
                else:
                    left_flag1 = left_flag1 + 1
            for k in range(len(stables), center, -1):  # right side loop
                if stables[right_flag] - stables[right_flag1] >= average_length:
                    crazy_cows_stable.append(stables[right_flag1])
                    right_flag = right_flag1
                    right_flag1 = right_flag1 - 1
                    crazy_cows = crazy_cows - 1
                    break
                else:
                    right_flag1 = right_flag1 - 1
        return print("Answer: ", crazy_cows_stable)


obj = Farm(17, 4)
obj.stables = [1, 3, 5, 10, 15, 16, 18, 20, 22, 24, 28, 33, 35, 39, 41, 49, 51]
obj.average_length = 12
print(len(obj.stables))
print(obj.stables[-1])
obj.iterating_list(obj.stables, obj.average_length, obj.crazy_cows)


