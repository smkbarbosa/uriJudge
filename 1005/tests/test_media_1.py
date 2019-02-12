from unittest import TestCase

class MediaTest(TestCase):
    def test_media(self):
        from med_1005 import med

        result = med(5.0, 7.1)

        self.assertEqual(6.43182, result)