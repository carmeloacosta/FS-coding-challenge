#!/bin/python3


import os
from django.test import TestCase

from ...models import Posture, User
from ...settings import FIXTURE_DIRS


class ModelsTestCase(TestCase):

    maxDiff = None
    fixtures = [os.path.join(FIXTURE_DIRS[0], 'initial_state.json'), ]

    def setUp(self):
        self.user_name = "albertmiro"
        self.user = User.objects.get(name=self.user_name)

    def test__get_all_users__ok(self):

        # Test main
        uqs = User.objects.all()

        # Check results
        expected_user_list = [
            {
                "name": "albertmiro",
                "email": "albert.miro@yogasolo.app",
                "password": "albertmiro2020"
            },
            {
                "name": "christianaranda",
                "email": "christian.aranda@yogasolo.app",
                "password": "christianaranda2020"
            }
        ]

        self.assertEqual(len(uqs), 2)
        for user in uqs:
            found = False
            for user_info in expected_user_list:
                if user_info["name"] == user.name and \
                        user_info["email"] == user.email and \
                        user_info["password"] == user.password:

                    found = True
                    break

            self.assertEqual(found, True)

    def test__get_all_postures__ok(self):

        # Test main
        pqs = Posture.objects.all()

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

        self.assertEqual(len(pqs), 3)
        for posture in pqs:
            found = False
            for posture_info in expected_posture_list:
                if posture_info["id"] == posture.id and \
                        posture_info["name"] == posture.name and \
                        posture_info["description"] == posture.description and \
                        posture_info["picture"] == posture.picture and \
                        posture_info["user"] == posture.user.name:

                    found = True
                    break

            self.assertEqual(found, True)

    def test__get_all_postures_to_dict__ok(self):

        # Test main
        pqs = Posture.objects.all()

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

        self.assertEqual(len(pqs), 3)
        for posture in pqs:
            found = False
            for posture_info in expected_posture_list:
                posture_dict = posture.to_dict()
                if posture_info == posture_dict:
                    found = True
                    break

            self.assertEqual(found, True)

    def test__new_user__ok(self):

        user_name = "carmelo"
        email = "carmelo.acosta@gmail.com"
        password = "carmeloyoga"

        # Test main
        new_user = User(name=user_name, email=email, password=password)
        new_user.save()

        # Check results
        uqs = User.objects.filter(name=user_name)
        self.assertEqual(len(uqs), 1)
        self.assertEqual(uqs[0].name, user_name)
        self.assertEqual(uqs[0].email, email)
        self.assertEqual(uqs[0].password, password)

    def test__new_posture__ok(self):

        id = "5df111bd23f72ffeefe0fa89"
        name = "Lotus flower"
        picture = "https://loremflickr.com/320/320/yoga,asana"
        description = "Basic yoga posture"
        user_name="albertmiro"
        user = User.objects.get(name=user_name)

        # Test main
        new_posture = Posture(id=id, name=name, picture=picture, description=description, user=user)
        new_posture.save()

        # Check results
        pqs = Posture.objects.filter(id=id)
        self.assertEqual(len(pqs), 1)
        self.assertEqual(pqs[0].name, name)
        self.assertEqual(pqs[0].picture, picture)
        self.assertEqual(pqs[0].description, description)
        self.assertEqual(pqs[0].user, user)

