import allure
import pytest
from http import HTTPStatus
from configs.config_API import base_url, common_headers, random_email, customer_payload
from answers.api_calls import ApiRequests


@pytest.mark.xdist_group(name="serial")
@allure.feature("API Tests")
@allure.story("Customer Management")
@pytest.mark.api
class TestApi:

    @pytest.fixture
    def customer_token(self):
        url = f"{base_url}/integration/customer/token/"
        token_payload = {
            "username": random_email,
            "password": "Password1"
        }
        response = ApiRequests.post(url, json=token_payload, headers=common_headers)
        assert response.status_code == HTTPStatus.OK, f"Failed to create customer token: {response.text}"
        return response.json()

    @allure.description("Test creating a customer via API.")
    def test_create_customer(self):
        url = f"{base_url}/customers"
        response = ApiRequests.post(url, json=customer_payload, headers=common_headers)
        assert response.status_code == HTTPStatus.OK, f"Failed to create customer: {response.text}"
        customer_id = response.json()["id"]
        print(response.json()["email"])
        assert customer_id is not None, "Customer ID not received"

    @allure.description("Test get customer info")
    def test_get_customer_info(self, customer_token):
        url = f"{base_url}/customers/me"
        headers = {
            **common_headers,
            "Authorization": f"Bearer {customer_token}",
        }
        response = ApiRequests.get(url, headers=headers)
        assert response.status_code == HTTPStatus.OK, f"Failed to get customer info: {response.text}"
        customer_info = response.json()
        print(customer_info["email"])
        assert customer_info["email"] == random_email, "Incorrect customer email"

    @allure.description("Test get customer info with wrong credentials")
    def test_get_customer_info_with_wrong_data(self):
        url = f"{base_url}/customers/me"
        headers = {
            **common_headers,
            "Authorization": f"Bearer {"12"}",
        }
        response = ApiRequests.get(url, headers=headers)
        assert response.status_code == HTTPStatus.UNAUTHORIZED, "Expected 400 Bad Request"
        assert response.json()["message"] == """The consumer isn't authorized to access %resources."""

    def test_create_customer_invalid_email(self, customer_token):
        invalid_email_payload = customer_payload.copy()
        invalid_email_payload["customer"]["email"] = "invalid_email"
        url = f"{base_url}/customers"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {customer_token}",
            "Host": "magento.softwaretestingboard.com",
            "Content-Length": "69",
            "Cookie": "PHPSESSID=827611b7d87be75f321673ab0c102a07",
            "User-Agent": "Chrome/111.0.5575.46"
        }
        response = ApiRequests.post(url, json=invalid_email_payload, headers=headers)
        assert response.status_code == HTTPStatus.BAD_REQUEST, ("Expected 400 Bad Request for invalid email but "
                                                                "received different status"
                                                                "code")
