from django.test import TestCase

# Create your tests here.
class modeltest(TestCase):
    def test_string_representation(self):
        instance=modeltest(name='Test')
        self.assertEqual(str(instance),("Test"))