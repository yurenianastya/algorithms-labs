import unittest


def read_data(file):
    data = []
    with open(file, "r") as f:
        for line in f:
            line = [int(i) for i in line.split()]
            data.append(line)
    return data


def find_max(row):
    shrinked_row = []
    for i in range(0, len(row)-1):
        if row[i] > row[i+1]:
            shrinked_row.append(row[i])
        else:
            shrinked_row.append(row[i+1])
    return shrinked_row


def adding_rows(ancestor, descendant):
    updated_list = [x + y for x, y in zip(ancestor, descendant)]
    return updated_list


def career_path_algo(file):
    positions = read_data(file)
    positions.reverse()
    for i in range(0, len(positions)-1):
        positions[0] = find_max(positions[0])
        positions[1] = adding_rows(positions[1], positions[0])
        positions.pop(0)
    output = open("career.out", "w+")
    output.write("The max experience which you can get is: %d" % positions[0][0])
    output.close()
    return positions[0][0]


class TestAlgorithm(unittest.TestCase):

    def test_input(self):
        self.assertEqual(career_path_algo("career_1.in"), 3)

    def test_input_1(self):
        self.assertEqual(career_path_algo("career_2.in"), 9999)

    def test_input_2(self):
        self.assertEqual(career_path_algo("career_3.in"), 12)


# unittest.main()
print(career_path_algo("career.in"))

