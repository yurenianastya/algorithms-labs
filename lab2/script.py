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
        print("Available spaces: ", stables)
        return stables


    def average_len(self, stables, crazy_cows):
        stables_length = stables[-1] - stables[0]
        average_length = math.trunc(stables_length / crazy_cows)
        print("The expected average length is: ", average_length)
        return average_length

    def iterating_list(self, stables, average_length, crazy_cows):
        crazy_cows_stable = [stables[0], stables[-1]]
        crazy_cows = crazy_cows - 2
        right_flag = -1
        right_flag1 = -2
        left_flag = 0
        left_flag1 = 1
        while crazy_cows > 0:
            for j in range(0, len(stables)-1, 1):  # left side loop
                if stables[left_flag1] in crazy_cows_stable:
                    left_flag1 = left_flag1 + 1
                    break
                if stables[left_flag1] - stables[left_flag] >= average_length:
                    crazy_cows_stable.append(stables[left_flag1])
                    left_flag = left_flag1
                    left_flag1 = left_flag1 + 1
                    crazy_cows = crazy_cows - 1
                    break
                else:
                    left_flag1 = left_flag1 + 1
            for k in range(len(stables), 0, -1):  # right side loop
                if stables[left_flag1] in crazy_cows_stable:
                    right_flag1 = right_flag1 + 1
                    break
                if stables[right_flag] - stables[right_flag1] >= average_length:
                    crazy_cows_stable.append(stables[right_flag1])
                    right_flag = right_flag1
                    right_flag1 = right_flag1 - 1
                    crazy_cows = crazy_cows - 1
                    break
                else:
                    right_flag1 = right_flag1 - 1
        print("The places where crazy cows are: ", sorted(crazy_cows_stable))
        return crazy_cows_stable

    def lowest_distance(self, crazy_cows_stable):
        add_array = []
        crazy_cows_stable.sort()
        for i in range(0, len(crazy_cows_stable)-1):
            number = crazy_cows_stable[i+1]-crazy_cows_stable[i]
            add_array.append(number)
        print("The smallest distance is: ", min(add_array))
        return min(add_array)


# def the objects
the_farm = Farm(8, 5)
stables1 = the_farm.generate_stables(the_farm.boxes, the_farm.crazy_cows)
the_len = the_farm.average_len(stables1, the_farm.crazy_cows)
the_iter = the_farm.iterating_list(stables1, the_len, the_farm.crazy_cows)
the_distance = the_farm.lowest_distance(the_iter)



