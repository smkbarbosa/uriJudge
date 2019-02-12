from unittest import TestCase

class MediaTest(TestCase):
    def test_media(self):
        from med_1006 import med

        result = med(10.0, 10.0, 5.0)

        self.assertEqual(7.5, result)
