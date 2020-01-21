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
