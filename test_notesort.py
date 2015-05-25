import unittest
from notesort import create_instrument_map


class TestNoteSort(unittest.TestCase):

    def test_create_instrument_map_creates_soprano_cornet(self):
        instrument_map = create_instrument_map()
        self.assertEqual(instrument_map['01'], 'SopranoCn')

    def test_create_instrument_map_soprano_not_solo(self):
        instrument_map = create_instrument_map()
        self.assertNotEqual(instrument_map['01'], 'SoloCn')

if __name__ == '__main__':
    unittest.main()
