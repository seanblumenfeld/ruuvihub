from rest_framework.reverse import reverse

from web.tests.helpers import BaseTestCase


class UserRegistrationTests(BaseTestCase):

    def test_can_register(self):
        response = self.client.post(
            path=reverse('rest_registration:register'),
            data={
                'username': 'test',
                'email': 'test@test.com',
                'password': 'jhop1234',
                'password_confirm': 'jhop1234',
            }
        )
        self.assertResponse201(response)

    def test_register_password_length(self):
        response = self.client.post(
            path=reverse('rest_registration:register'),
            data={
                'username': 'test',
                'email': 'test@test.com',
                'password': '1234',
                'password_confirm': '1234',
            }
        )
        self.assertResponse400(response)
        self.assertEqual(response.data['password'][0].code, 'invalid')
