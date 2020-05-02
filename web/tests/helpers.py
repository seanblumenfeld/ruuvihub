import logging

from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_200_OK
from rest_framework.test import APITestCase
from testfixtures import LogCapture


class AssertResponseMixin:

    def assertResponse(self, response, status_code, data=None, data_contains=None, detail=None):
        self.assertEqual(response.status_code, status_code, msg=response.data)

        if data is not None:
            self.assertDictEqual(response.data, data)

        if data_contains is not None:
            self.assertResponseDataContains(response, data_contains)

        if detail is not None:
            self.assertEqual(response.data['detail'], detail)

    def assertResponseDataContains(self, response, data_contains):
        for k, v in data_contains.items():
            self.assertIn(k, response.data)
            self.assertEqual(response.data[k], v)

    def assertResponse200(self, response, data=None, data_contains=None, detail=None):
        self.assertResponse(
            response, HTTP_200_OK, data=data, data_contains=data_contains, detail=detail
        )

    def assertResponse201(self, response, data=None, data_contains=None, detail=None):
        self.assertResponse(
            response, HTTP_201_CREATED, data=data, data_contains=data_contains, detail=detail
        )

    def assertResponse400(self, response, data=None, data_contains=None, detail=None):
        self.assertResponse(
            response, HTTP_400_BAD_REQUEST, data=data, data_contains=data_contains, detail=detail
        )


class LogCaptureMixin:

    def setUp(self):
        super().setUp()
        self.log_capture = LogCapture(level=logging.DEBUG)

    def tearDown(self):
        super().tearDown()
        self.log_capture.uninstall()


class BaseTestCase(AssertResponseMixin, LogCaptureMixin, APITestCase):
    pass
