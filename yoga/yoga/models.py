#!/bin/python3

"""
    Data models
"""

from django.db import models


class User(models.Model):
    """
        API User Entity. There will be a row in this table for each registered API user.
    """
    # User name
    name = models.CharField(max_length=64, primary_key=True)
    # User email address
    email = models.CharField(max_length=256)
    # Password
    password = models.CharField(max_length=16)

    def __str__(self):

        return "< name={}, email={}, password={} >".format(self.name, self.email, self.password)


class Posture(models.Model):
    """
        Yoga Posture Entity. There will be a row in this table for each yoga posture.

    """
    # Unique hash per yoga posture
    id = models.CharField(max_length=24, primary_key=True, blank=False, null=False)
    # Name of the yoga posture
    name = models.CharField(max_length=128)
    # Url of the picture that represents the yoga posture
    picture = models.CharField(max_length=256)
    # Textual description of the yoga posture
    description = models.CharField(max_length=256)
    # The user the posture belongs to
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):

        return "< id={}, name={}, picture={}, user={}, description={} >".format(self.id, self.name, self.picture,
                                                                       self.user.name, self.description[:20])
