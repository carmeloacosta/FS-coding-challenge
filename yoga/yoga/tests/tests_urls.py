#!/bin/python3


import os
from json import dumps
from django.test import TestCase

from ..settings import FIXTURE_DIRS


class UserViewTestCase(TestCase):

    maxDiff = None
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


class PostureViewTestCase(TestCase):

    maxDiff = None
    fixtures = [os.path.join(FIXTURE_DIRS[0], 'initial_state.json'), ]

    def setUp(self):
        pass

    def test__posture_add_json__ok(self):
        # ((<posture_info>, <now>), <expected_hash>)
        now = 1579611302
        posture_info_list = [(({
                "name": "Added posture 1",
                "description": "Added posture 1 description",
                "picture": "https://loremflickr.com/320/320/yoga,asana",
                "user": "albertmiro"
            }, now), "780c11aa9212e666a45d9d4a"),
            (({
                  "name": "Added posture 2",
                  "description": "Added posture 1 description",
                  "picture": "https://loremflickr.com/320/320/yoga,asana",
                  "user": "albertmiro"
              }, now), "419d59e5150da91b244d164a"),
            (({
                  "name": "Added posture 1",
                  "description": "Added posture 1 description",
                  "picture": "https://loremflickr.com/320/320/yoga,asana",
                  "user": "christianaranda"
              }, now), "e15c1d7734fa35e08ffe4871"),
            (({
                  "name": "Added posture 1",
                  "description": "Added posture 1 description",
                  "picture": "https://loremflickr.com/320/320/yoga,asana",
                  "user": "christianaranda"
              }, now + 10), "21f8369e60e80d3e3f5e1227"),
        ]

        # Test main
        for posture_info in posture_info_list:
            posture_info[0][0]["now"] = posture_info[0][1]
            response = self.client.post('/posture/add?json=true',
                                        dumps(posture_info[0][0]),
                                        content_type="application/json")

            # Check results
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content.decode(), dumps({"id": posture_info[1]}))

    def test__posture_add_json__wrong(self):
        # ((<posture_info>, <now>), <expected_hash>)
        now = 1579611302
        posture_info_list = [(({
                "description": "Added posture 1 description",
                "picture": "https://loremflickr.com/320/320/yoga,asana",
                "user": "albertmiro"
            }, now), {"error": "Bad Body. Expected json with 'name', 'picture', 'description', and 'user' fields"}),
            (({
                  "name": "Added posture 2",
                  "description": "Added posture 1 description",
                  "picture": "https://loremflickr.com/320/320/yoga,asana",
              }, now), {"error": "Bad Body. Expected json with 'name', 'picture', 'description', and 'user' fields"}),
            (({
                  "name": "Added posture 1",
                  "description": "Added posture 1 description",
                  "picture": "https://loremflickr.com/320/320/yoga,asana",
                  "user": "unknownuser"
              }, now), {"error": "Unknown user"})
        ]

        # Test main
        for posture_info in posture_info_list:
            posture_info[0][0]["now"] = posture_info[0][1]
            response = self.client.post('/posture/add?json=true',
                                        dumps(posture_info[0][0]),
                                        content_type="application/json")

            # Check results
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.content.decode(), dumps(posture_info[1]))

    def test__posture_get_json__ok(self):

        # Test main
        response = self.client.get('/posture/get?json=true')

        # Check results
        expected_postures = [
            {'id': '5df111bd23f72ffeefe0fa2f',
             'name': 'Initial posture 1',
             'picture': 'https://loremflickr.com/320/320/yoga,asana',
             'description': 'Initial posture 1 description',
             'user': 'albertmiro'},
            {'id': '5df111bd23f72ffeefe0fa30',
             'name': 'Initial posture 2',
             'picture': 'https://loremflickr.com/320/320/yoga,asana',
             'description': 'Initial posture 2 description',
             'user': 'albertmiro'},
            {'id': '5df111bd23f72ffeefe0fa2e',
             'name': 'Initial posture 3',
             'picture': 'https://loremflickr.com/320/320/yoga,asana',
             'description': 'Initial posture 3 description',
             'user': 'christianaranda'}
        ]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), dumps(expected_postures))


