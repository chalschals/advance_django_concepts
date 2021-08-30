from rest_framework.test import APITestCase


class MyTestClass(APITestCase):
    def test_custom_functions(self):
        self.assertEqual('a', 'a')
