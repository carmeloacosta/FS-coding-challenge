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


class PostureViewTestCase(TestCase):

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
            #import ipdb; ipdb.set_trace() #DEBUGGING
            posture_info[0][0]["now"] = posture_info[0][1]
            response = self.client.post('/posture/add?json=true',
                                        dumps(posture_info[0][0]),
                                        content_type="application/json")

            # Check results
            self.assertEqual(response.content.decode(), dumps({"id": posture_info[1]}))

            #result = self.controller.create_posture_hash(posture_info[0][0], posture_info[0][1])

            # Check results
            #self.assertEqual(result, posture_info[1])



        # # Test main
        # response = self.client.post('/posture/add?json=true',
        #                             dumps(body),
        #                             content_type="application/json")
        #
        # # Check results
        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.content.decode(), "Added new user")
