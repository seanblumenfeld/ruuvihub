from rest_framework.reverse import reverse

from web.tests.factories.user import UserFactory
from web.tests.helpers import BaseTestCase, get_api_token


class UserRegistrationTests(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.user = UserFactory()
        token = get_api_token(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token['access']}")

    def test_can_get_user(self):
        response = self.client.get(
            path=reverse('users-detail', kwargs={'pk': self.user.pk}),
        )
        self.assertResponse200(response, data_contains={'id': self.user.id_str})

    def test_cannot_get_different_user(self):
        user2 = UserFactory()
        response = self.client.get(
            path=reverse('users-detail', kwargs={'pk': user2.pk}),
        )
        self.assertResponse(response, 403)
