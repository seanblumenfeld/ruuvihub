from django.test import override_settings
from django.urls import path
from rest_framework.exceptions import NotAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from web.tests.helpers import BaseTestCase, get_api_token


class FakeView(GenericAPIView):
    def get(self, request, *args, **kwargs):
        return Response()

    def post(self, request, *args, **kwargs):
        return Response()


urlpatterns = [
    path('fake-view', FakeView.as_view()),
]


@override_settings(ROOT_URLCONF=__name__)
class ApiAuthTests(BaseTestCase):

    def test_default_for_all_views_should_require_jwt_auth(self):
        response = self.client.get(path='/fake-view')
        self.assertResponse(response, 401, detail=NotAuthenticated.default_detail)

    def test_can_use_api_token(self):
        token = get_api_token()
        response = self.client.get(
            path='/fake-view',
            HTTP_AUTHORIZATION=f"Bearer {token['access']}"
        )
        self.assertResponse200(response)
