import unittest
from main.LC0409_Longest_Palindrome import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_longestPalindrome(self):
        self.assertEqual(test.longestPalindrome("abccccdd"), 7)
        self.assertEqual(test.longestPalindrome("a"), 1)
        self.assertEqual(test.longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicated\
        canlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplac\
        eforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargers\
        ensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehavecons\
        ecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcannev\
        erforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavet\
        husfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadw\
        etakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesed\
        eadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeo\
        pleforthepeopleshallnotperishfromtheearth"), 983)
