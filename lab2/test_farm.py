from unittest import TestCase
import script


class TestFarm(TestCase):

    def test_obj_1(self):
        print("----------Testing the case when 3 cows----------")
        object1 = script.Farm(8, 3)
        stables = [1, 5, 6, 7, 8, 9, 10, 11]
        the_len = object1.average_len(stables, object1.crazy_cows, object1.boxes)
        the_iter = object1.iterating_list(stables, the_len, object1.crazy_cows)
        the_distance = object1.lowest_distance(the_iter)
        self.assertEqual(the_distance, 4)

    def test_obj_2(self):
        print("----------Testing the case when cows equal the half of the boxes----------")
        object2 = script.Farm(12, 6)
        stables = [1, 5, 6, 7, 8, 9, 10, 11, 14, 17, 19, 22]
        the_len = object2.average_len(stables, object2.crazy_cows, object2.boxes)
        the_iter = object2.iterating_list(stables, the_len, object2.crazy_cows)
        the_distance = object2.lowest_distance(the_iter)
        self.assertEqual(the_distance, 3)

    def test_obj_3(self):
        print("----------Testing the case when many cows----------")
        object3 = script.Farm(24, 7)
        stables = [1, 5, 6, 7, 8, 9, 10, 11, 14, 18, 20, 21, 27, 30, 33, 34, 37, 40, 42, 48, 50, 55, 56, 63]
        the_len = object3.average_len(stables, object3.crazy_cows, object3.boxes)
        the_iter = object3.iterating_list(stables, the_len, object3.crazy_cows)
        the_distance = object3.lowest_distance(the_iter)
        self.assertEqual(the_distance, 7)

    def test_obj_4(self):
        print("----------Testing the random case----------")
        object4 = script.Farm(18, 8)
        stables = [1, 5, 8, 9, 10, 11, 25, 29, 34, 37, 40, 49, 50, 55, 60, 63, 70]
        the_len = object4.average_len(stables, object4.crazy_cows, object4.boxes)
        the_iter = object4.iterating_list(stables, the_len, object4.crazy_cows)
        the_distance = object4.lowest_distance(the_iter)
        self.assertEqual(the_distance, 6)

    def test_obj_5(self):
        print("----------Testing the the case----------")
        object4 = script.Farm(14, 10)
        stables = [1, 5, 9, 10, 25, 29, 34, 37, 40, 49, 50, 55, 60, 63]
        the_len = object4.average_len(stables, object4.crazy_cows, object4.boxes)
        the_iter = object4.iterating_list(stables, the_len, object4.crazy_cows)
        the_distance = object4.lowest_distance(the_iter)
        self.assertEqual(the_distance, 1)
