#!/bin/python3


import os
from json import dumps
from django.test import TestCase

from ..settings import FIXTURE_DIRS


class UserViewTestCase(TestCase):

    fixtures = [os.path.join(FIXTURE_DIRS[0], 'initial_state.json'), ]

    def setUp(self):
        pass

    def test__user_add_json__ok(self):
        body = {
            "name": "carmeloacosta",
            "email": "carmelo.acosta@gmail.com",
            "password": "carmeloacosta2020"
        }

        # Test main
        response = self.client.post('/user/add?json=true',
                                    dumps(body),
                                    content_type="application/json")

        # Check results
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "Added new user")
