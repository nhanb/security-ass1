import unittest
import ceasar
import subst


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ .,()-!?\n0123456789'


class CeasarTest(unittest.TestCase):

    def testInvalidInput(self):
        args = ['', 'e', 'input.txt']
        result = ceasar.run(args)
        self.assertEquals("Invalid number of arguments.", result)

        args = ['']
        result = ceasar.run(args)
        self.assertEquals("Invalid number of arguments.", result)

        args = ['', 'e', 'inputs.txt', '1']
        result = ceasar.run(args)
        self.assertEquals("Error reading inputs.txt", result)

        args = ['', 'e', 'illegal_chars.txt', '1']
        result = ceasar.run(args)
        self.assertEquals("Input can't contain character '&'.", result)

    def testCeasarLogic(self):
        cases = [
            ["123", 1, "e", "234"],
            ["789", 1, "e", "89A"],
            ["89A", 1, "d", "789"],
            ["ABCD", 2, "e", "CDEF"],
            ["ABCD", 2, "d", "89AB"],
            ["I AM AWESOME!\n()--", 45, "e", "I AM AWESOME!\n()--"],
            ["789A", 46, "e", "89AB"],
        ]

        for case in cases:
            result = ceasar.ceasar(case[0], case[1], alphabet, case[2])
            self.assertEquals(result, case[3])


class RandomSubsTest(unittest.TestCase):
    def test(self):
        return subst

if __name__ == "__main__":
    unittest.main()
