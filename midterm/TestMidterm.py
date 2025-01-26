"""
    CS 5001 Midterm Test Suite FALL 2024

"""

import unittest
import io, contextlib
import os
from os.path import exists

import midterm


class TestMidterm(unittest.TestCase): 
    def test_fps_to_mph(self):
        self.assertAlmostEqual(midterm.fps_to_mph(10), 6.81818,
                               msg="failed 10fps", delta=0.1)

        self.assertAlmostEqual(midterm.fps_to_mph(22.2), 15.13636,
                               msg="Failed 22.2 fps", delta=0.1)

        self.assertAlmostEqual(midterm.fps_to_mph(0), 0,
                               msg="Failed 0 fps", delta=0.1)

        self.assertAlmostEqual(midterm.fps_to_mph(-1), 0.681818,
                               msg="Failed -1 fps", delta=0.1)

    def test_hero_team(self):
        team = []
        midterm.update_hero_team("FlaSH", midterm.fps_to_mph(3669.6), team)
        compare = ["FLASH", 2502.0]
        self.assertEqual(team, compare)
        
        midterm.update_hero_team("superman", midterm.fps_to_mph(1474), team)
        compare += ["SUPERMAN", 1005.0]
        self.assertEqual(team, compare)

        midterm.update_hero_team("The Sloth", midterm.fps_to_mph(0), team)
        compare += ["THE SLOTH", 0.0]
        
        midterm.update_hero_team("WONDER WOMAN", midterm.fps_to_mph(900), team)
        compare += ["WONDER WOMAN", 613.6]
        self.assertEqual(team, compare)

        midterm.update_hero_team("Superman", midterm.fps_to_mph(3669.6), team)
        compare[3] = 2502.0 # update entry, no duplicates!
        self.assertEqual(team, compare)

    def test_conga_line(self):
        a = [[]]
        result = midterm.conga_line(a)
        self.assertEqual(result, [[],[0]])
        self.assertEqual(a, [[]], msg="Original List Mutated!")

        a = [[1], [2,3]]
        result = midterm.conga_line(a)
        self.assertEqual(result, [[1], [2,3], [6]])
        self.assertEqual(a, [[1], [2,3]], msg="Original List Mutated!")

        a = [[1], [2,3,4], [6], []]
        result = midterm.conga_line(a)
        self.assertEqual(result, [[1], [2,3,4], [6], [], [16]])
        self.assertEqual(a, [[1], [2,3,4], [6], []], msg="Original List Mutated!")

    def test_uniques(self):
        """using a set() so order of letters will not matter"""
        
        self.assertEqual(set(midterm.uniques("Hello", "Mom")), set("HelMm"))
        self.assertEqual(set(midterm.uniques("Mummy", "Yummy Tummy!")), set("MY T!"))
        self.assertEqual(midterm.uniques("Hello", "Hello"), "")
        self.assertEqual(set(midterm.uniques("Hello", "hello")), set("Hh"))
        self.assertEqual(set(midterm.uniques("", "Mom")), set("Mom"))
        self.assertEqual(midterm.uniques("", ""), "")


    def test_count_odds(self):
        self.assertEqual(midterm.count_odds([]), 0, msg="No odds")
        self.assertEqual(midterm.count_odds([3]), 1, msg="1 odds")
        self.assertEqual(midterm.count_odds([1,3,45, 7, 9]), 5, msg="5 odds")
        self.assertEqual(midterm.count_odds([1,2,3,4,5]), 3, msg="3 odds")
        self.assertEqual(midterm.count_odds([2,4,6,8,10]), 0, msg="No odds")
        self.assertEqual(midterm.count_odds([0]), 0, msg="No odds")


    def test_bin_flip(self):
        self.assertEqual(midterm.bin_flip("1001"), "0110")
        self.assertEqual(midterm.bin_flip("0010"), "1101")
        self.assertEqual(midterm.bin_flip("1101"), "0010")
        self.assertEqual(midterm.bin_flip("0"), "1")
        self.assertEqual(midterm.bin_flip(""), "")
        self.assertEqual(midterm.bin_flip("111111"), "000000")
        self.assertEqual(midterm.bin_flip("000000"), "111111")


        
        
        
        
        
if __name__ == "__main__":
    unittest.main()
