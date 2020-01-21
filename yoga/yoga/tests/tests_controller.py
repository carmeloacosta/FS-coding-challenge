#!/bin/python3


import os
from django.test import TestCase
from unittest.mock import MagicMock

from ..models import Posture, User
from ..controller import Controller
from ..settings import FIXTURE_DIRS


class ControllerTestCase(TestCase):

    maxDiff = None
    fixtures = [os.path.join(FIXTURE_DIRS[0], 'initial_state.json'), ]

    def setUp(self):
        self.logger = MagicMock()
        self.controller = Controller(self.logger)

        self.user_name = "albertmiro"
        self.user = User.objects.get(name=self.user_name)

    def test__get_all_postures__ok(self):

        # Test main
        postures = self.controller.get_all_postures()

        # Check results
        expected_posture_list = [
            {
                "id": "5df111bd23f72ffeefe0fa2f",
                "name": "Initial posture 1",
                "description": "Initial posture 1 description",
                "picture": "https://loremflickr.com/320/320/yoga,asana",
                "user": self.user_name
             },
            {
                "id": "5df111bd23f72ffeefe0fa30",
                "name": "Initial posture 2",
                "description": "Initial posture 2 description",
                "picture": "https://loremflickr.com/320/320/yoga,asana",
                "user": self.user_name
            },
            {
                "id": "5df111bd23f72ffeefe0fa2e",
                "name": "Initial posture 3",
                "description": "Initial posture 3 description",
                "picture": "https://loremflickr.com/320/320/yoga,asana",
                "user": "christianaranda"
            }

        ]

        self.assertEqual(postures, expected_posture_list)

    def test__get_user_postures__ok(self):

        # Test main
        postures = self.controller.get_all_postures(self.user_name)

        # Check results
        expected_posture_list = [
            {
                "id": "5df111bd23f72ffeefe0fa2f",
                "name": "Initial posture 1",
                "description": "Initial posture 1 description",
                "picture": "https://loremflickr.com/320/320/yoga,asana",
                "user": self.user_name
             },
            {
                "id": "5df111bd23f72ffeefe0fa30",
                "name": "Initial posture 2",
                "description": "Initial posture 2 description",
                "picture": "https://loremflickr.com/320/320/yoga,asana",
                "user": self.user_name
            }
        ]

        self.assertEqual(postures, expected_posture_list)

    def test__get_all_postures__wrong(self):

        # Test main
        postures = self.controller.get_all_postures("unknown_user")
        self.assertEqual(len(postures), 0)

    def test__add_user__ok(self):

        user_info = {
            "name": "carmeloacosta",
            "email": "carmelo.acosta@gmail.com",
            "password": "carmeloacosta2020",
        }

        # Test main
        result = self.controller.add_user(user_info)

        # Check results
        self.assertEqual(result, True)

        user = User.objects.get(name=user_info["name"])
        self.assertEqual(user.name, user_info["name"])
        self.assertEqual(user.email, user_info["email"])
        self.assertEqual(user.password, user_info["password"])

    def test__add_user__wrong(self):

        user_info_list = [{
                "name": "albertmiro",
                "email": "albert.miro@yogasolo.app",
                "password": "albertmiro2020",
            },
            {
                "email": "carmelo.acosta@gmail.com",
                "password": "carmeloacosta2020",
            }
        ]

        # Test main
        for user_info in user_info_list:
            result = self.controller.add_user(user_info)

            # Check results
            self.assertEqual(result, False)

    def test__add_posture__ok(self):

        posture_info = {
            "id": "5df111bd23f72ffeefe0ffff",
            "name": "Added posture 1",
            "description": "Added posture 1 description",
            "picture": "https://loremflickr.com/320/320/yoga,asana",
        }

        # Test main
        result = self.controller.add_posture(posture_info, self.user_name)

        # Check results
        self.assertEqual(result, True)

        posture = Posture.objects.get(id=posture_info["id"])
        self.assertEqual(posture.id, posture_info["id"])
        self.assertEqual(posture.name, posture_info["name"])
        self.assertEqual(posture.description, posture_info["description"])
        self.assertEqual(posture.picture, posture_info["picture"])
        self.assertEqual(posture.user, self.user)

    def test__add_posture__wrong(self):

        # (<posture_info>, <user_name)
        posture_info_list = [({
                "id": "5df111bd23f72ffeefe0fa2f",
                "name": "Added posture 1",
                "description": "Added posture 1 description",
                "picture": "https://loremflickr.com/320/320/yoga,asana",
            }, self.user_name),
            ({
                 "name": "Added posture 1",
                 "description": "Added posture 1 description",
                 "picture": "https://loremflickr.com/320/320/yoga,asana",
             }, self.user_name),
            ({
                 "id": "5df111bd23f72ffeefe0ffff",
                 "name": "Added posture 1",
                 "description": "Added posture 1 description",
                 "picture": "https://loremflickr.com/320/320/yoga,asana",
             }, "unknown_user"),
        ]

        # Test main
        for posture_info in posture_info_list:
            result = self.controller.add_posture(posture_info[0], posture_info[1])

            # Check results
            self.assertEqual(result, False)

    def test__is_valid_user__ok(self):

        user_list = ["albertmiro", "christianaranda"]

        # Test main
        for user_name in user_list:
            result = self.controller.is_valid_user(user_name)

            # Check results
            self.assertEqual(result, True)

    def test__is_valid_user__wrong(self):

        user_list = ["carmeloacosta", "unknownuser"]

        # Test main
        for user_name in user_list:
            result = self.controller.is_valid_user(user_name)

            # Check results
            self.assertEqual(result, False)

    def test__create_posture_hash__ok(self):

        # ((<posture_info>, <now>), <expected_hash>)
        now = 1579611302
        posture_info_list = [(({
                "name": "Added posture 1",
                "description": "Added posture 1 description",
                "picture": "https://loremflickr.com/320/320/yoga,asana",
                "user": self.user_name
            }, now), "780c11aa9212e666a45d9d4a"),
            (({
                  "name": "Added posture 2",
                  "description": "Added posture 1 description",
                  "picture": "https://loremflickr.com/320/320/yoga,asana",
                  "user": self.user_name
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
            result = self.controller.create_posture_hash(posture_info[0][0], posture_info[0][1])

            # Check results
            self.assertEqual(result, posture_info[1])

    def test__create_posture_hash__wrong(self):

        # ((<posture_info>, <now>), <expected_hash>)
        now = 1579611302
        posture_info_list = [(({
                "description": "Added posture 1 description",
                "picture": "https://loremflickr.com/320/320/yoga,asana",
                "user": self.user_name
            }, now), "000000000000000000000000"),
            (({
                  "name": "Added posture 2",
                  "description": "Added posture 1 description",
                  "picture": "https://loremflickr.com/320/320/yoga,asana",
              }, now), "000000000000000000000000"),
            (({
                  "name": "Added posture 1",
                  "description": "Added posture 1 description",
                  "picture": "https://loremflickr.com/320/320/yoga,asana",
                  "user": "christianaranda"
              }, "error!!!"), "000000000000000000000000")
        ]

        # Test main
        for posture_info in posture_info_list:
            result = self.controller.create_posture_hash(posture_info[0][0], posture_info[0][1])

            # Check results
            self.assertEqual(result, posture_info[1])
