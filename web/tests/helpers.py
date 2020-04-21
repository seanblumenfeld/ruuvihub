from rest_framework import status
from rest_framework.test import APITestCase


class APITestCaseHelper:

    def assertResponse(self, response, status_code, data=None, detail=None):
        self.assertEqual(response.status_code, status_code, msg=response.data)
        if data:
            self.assertDictEqual(response.data, data)
        if detail:
            self.assertEqual(response.data['detail'], detail)

    def assertResponse200(self, response, data=None):
        self.assertResponse(response, status.HTTP_200_OK, data=data)

    def assertResponse201(self, response, data=None):
        self.assertResponse(response, status.HTTP_201_CREATED, data=data)

    def assertResponse400(self, response, data=None, detail=None):
        self.assertResponse(response, status.HTTP_400_BAD_REQUEST, data=data, detail=detail)

    def assertResponse404(self, response, detail=None):
        self.assertResponse(response, status.HTTP_404_NOT_FOUND, detail=detail)


class BaseTestCase(APITestCaseHelper, APITestCase):
    pass
