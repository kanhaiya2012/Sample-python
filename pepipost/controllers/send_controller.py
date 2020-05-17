# -*- coding: utf-8 -*-

"""
    pepipost

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from pepipost.api_helper import APIHelper
from pepipost.configuration import Configuration
from pepipost.controllers.base_controller import BaseController
from pepipost.http.auth.custom_header_auth import CustomHeaderAuth
from pepipost.exceptions.api_exception import APIException

class SendController(BaseController):

    """A Controller to access Endpoints in the pepipost API."""


    def create_generate_the_mail_send_request(self,
                                              body):
        """Does a POST request to /send.

        The endpoint send is used to generate the request to pepipost server
        for sending an email to recipients.

        Args:
            body (Send): New mail request will be generated

        Returns:
            list of string: Response from the API. API Response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/send'
        _query_builder = Configuration.get_base_uri(Configuration.Server.SERVER1)
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            return APIHelper.json_deserialize(_context.response.raw_body)
        if _context.response.status_code == 405:
            raise APIException('Invalid input', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)
