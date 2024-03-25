import requests
from requests import Response
from answers.allure_attachments import AllureAttachments


class ApiRequests:
    """
    wrapper class for api requests that includes built in allure logging.
    """

    @staticmethod
    def get(url: str, data=None, json=None, **kwargs) -> Response:
        headers = kwargs.get('headers', {})  # Get the headers from kwargs
        AllureAttachments.attach_request(url, request_method="GET",headers=headers)
        response = requests.get(url, **kwargs)
        try:
            AllureAttachments.attach_response(response)
        except Exception as e:
            print(e)
        return response

    @staticmethod
    def post(url: str, data=None, json=None, **kwargs) -> Response:
        headers = kwargs.get('headers', {})  # Get the headers from kwargs
        AllureAttachments.attach_request(url, request_method="POST", headers=headers, payload=json)
        response = requests.post(url, data=data, json=json, **kwargs)
        try:
            AllureAttachments.attach_response(response)
        except Exception as e:
            print(e)
        return response

    @staticmethod
    def delete(url: str) -> Response:
        AllureAttachments.attach_request(url, request_method="DELETE")
        response = requests.delete(url)
        try:
            AllureAttachments.attach_response(response)
        except Exception as e:
            print(e)
        return response

    @staticmethod
    def put(url: str, data=None, params=None) -> Response:
        AllureAttachments.attach_request(url, request_method="PUT", payload=data)
        response = requests.put(url, params=params, json=data)
        try:
            AllureAttachments.attach_response(response)
        except Exception as e:
            print(e)
        return response