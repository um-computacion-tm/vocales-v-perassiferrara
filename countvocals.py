import unittest

def count_vocals(word):
    tuple_vocals = ("a","e","i","o","u")
    result = {}
    for letter in word.lower():
        if letter in tuple_vocals:
            if letter not in result:
                result[letter] = 0
            result[letter] += 1
    return result

class TestCountVocals(unittest.TestCase):

    def test_jjjj(self):
        result = count_vocals("jjjj")
        self.assertEqual(result, {})

    def test_aaa(self):
        result = count_vocals("aaa")
        self.assertEqual(result, {"a":3})

    def test_palta(self):
        result = count_vocals("palta")
        self.assertEqual(result, {"a":2})

    def test_murcielago(self):
        result = count_vocals("murcielago")
        self.assertEqual(result, {"a":1, "e":1, "i":1, "o":1, "u":1})

    def test_electroencefalografista(self):
        result = count_vocals("electroencefalografista")
        self.assertEqual(result, {"a":3, "e":4, "i":1, "o":2})

    def test_palta_mayus(self):
        result = count_vocals("pAlta")
        self.assertEqual(result, {"a":2})

    def test_murcielago_mayus(self):
        result = count_vocals("MURcielAgo")
        self.assertEqual(result, {"a":1, "e":1, "i":1, "o":1, "u":1})

    def test_electroencefalografista_mayus(self):
        result = count_vocals("elEctrOEncefAlogrAfista")
        self.assertEqual(result, {"a":3, "e":4, "i":1, "o":2})

    def test_ornitorrinco_mayus(self):
        result = count_vocals("OrnItorrinco")
        self.assertEqual(result, {"i":2, "o":3})
    
if __name__ == "__main__":
    unittest.main()