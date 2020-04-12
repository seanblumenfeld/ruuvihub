from rest_framework import status
from rest_framework.test import APITestCase


class APITestCaseHelper:

    def assertResponseStatusCode(self, response, status_code):
        self.assertEqual(response.status_code, status_code, msg=response.data)

    def assertResponse200(self, response):
        self.assertResponseStatusCode(response, status.HTTP_200_OK)

    def assertResponse201(self, response, data=None):
        self.assertResponseStatusCode(response, status.HTTP_201_CREATED)
        if data:
            self.assertDictEqual(response.data, data)

    def assertResponse400(self, response, detail=None):
        self.assertResponseStatusCode(response, status.HTTP_400_BAD_REQUEST)
        if detail is not None:
            self.assertEqual(response.data['detail'], detail, msg=response.data)

    def assertResponse404(self, response, detail=None):
        self.assertResponseStatusCode(response, status.HTTP_404_NOT_FOUND)
        if detail is not None:
            self.assertEqual(response.data['detail'], detail, msg=response.data)


class BaseTestCase(APITestCaseHelper, APITestCase):
    pass
