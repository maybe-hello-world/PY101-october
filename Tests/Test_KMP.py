import unittest
from Tasks.KMP import KMP_algo


class MyTestCase(unittest.TestCase):

	def test_begin(self):
		haystack = "Hello, tiny world!"
		needle = "Hell"
		self.assertEqual(KMP_algo(haystack, needle), 0, "Right index is 0")

	def test_end(self):
		haystack = "All these moments will be lost in time..."
		needle = "time..."
		self.assertEqual(KMP_algo(haystack, needle), 34, "'time...' is in the end")

	def test_middle(self):
		haystack = "Шел я лесом, вижу мост, на мосту ворона сохнет." \
				   " Взял ее за хвост, положил под мост, пускай ворона мокнет."
		needle = "Взял"
		self.assertEqual(KMP_algo(haystack, needle), haystack.index(needle), "Не взяли ворону, ворона вся и высохла.")

	def test_missing(self):
		haystack = "Because only a ginger can call another ginger ginger!"
		needle = "afroamerican"
		self.assertIsNone(KMP_algo(haystack, needle), "Фи, как некультурно, песня о рыжих вообще-то.")


if __name__ == '__main__':
	unittest.main()
