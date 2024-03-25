import json
import allure
from allure_commons.types import AttachmentType
from requests import Response


class AllureAttachments:
    """
    Attach allure request, parameters:
    URL
    request method
    headers
    payload
    query parameters
    If payload is None or dictionary we will add it as a value to the request data dictionary.
    Else if it's a list we will call to string and encode it as UTF8 string.
    """

    @staticmethod
    def attach_request(url, request_method, headers=None, payload=None, q_params=None) -> None:
        filename = f"[{request_method}] request"
        request_data = {
            "RequestMethod": request_method,
            "RequestURL": url,
            "headers": headers,  # Assign headers directly
            "q_params": q_params,
            "payload": payload
        }
        request_data_str = json.dumps(request_data, indent=4).encode('utf-8')
        allure.attach(request_data_str, name=filename, attachment_type=allure.attachment_type.JSON)

    """
    Attach allure response, parameters:
    Response
    filename
    """

    @staticmethod
    def attach_response(r: Response, filename=None):
        filename = filename or f"response [{r.status_code}]"
        response_data = r.content
        data_type = AllureAttachments.get_attachment_type(r)
        if data_type == AttachmentType.JSON:
            response_data = {
                "URL": r.url,
                "Headers": dict(r.headers),
                "Response": r.json()
            }
            response_data = json.dumps(response_data, indent=4).encode('utf-8')
        elif data_type is None:
            data_type = AttachmentType.TEXT
            response_data = r.text
        allure.attach(response_data, name=filename, attachment_type=data_type)

    @staticmethod
    def get_attachment_type(r: Response):
        """
        This function checks the content type of the response and
        returns the appropriate allure attachment type (from AttachmentType enum)
        :param r: Response object
        :return: AttachmentType value if content_type exists in the list, otherwise, return None
        """
        content_type = r.headers['Content-Type'].split(';')[0]  # split and remove the encoding type
        return next(
            (
                AttachmentType(data.value)
                for data in AttachmentType
                if content_type in data.value
            ),
            None,
        )
