#!/bin/python3


import os
from json import dumps
from django.test import TestCase

from ..models import Posture, User
from ..settings import FIXTURE_DIRS


class ModelsTestCase(TestCase):

    maxDiff = None
    fixtures = [os.path.join(FIXTURE_DIRS[0], 'initial_state.json'), ]

    def setUp(self):
        pass

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

