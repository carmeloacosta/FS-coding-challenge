
# Add logger
import logging
logger = logging.getLogger(__name__)

from .models import User, Posture


class Controller():
    """
        Implements the Yoga bussiness logic. It access the underlying data base system in order to persist the
        required data.

        IMPLEMENTATION NOTE: IN ORDER TO KEEP THIS TECHNICAL CHALLENGE SIMPLE I WILL NOT ADD ALL CRUD FOR BOTH
        USERS AND POSTURES (I.E., CREATE/READ/UPDATE/DELETE), JUST THE MINIMAL OPERATIONS ASKED IN THE TEST. IN A REAL
        IMPLEMENTATION IT WILL BE NEEDED TO IMPLEMENT IT ALL.
    """
    def __init__(self, elogger=logger):
        self.logger = elogger

    def get_all_postures(self, user_only=None):
        """
            Returns all the

        :param user_only: (str) If any user name is specified, returns only the postures that belongs to the specified
            user.
        :return: (list of dict) List of all postures. Each posture is represented by a dictionary involving all the
            posture data. (see Posture.to_dict)
        """
        result = []

        if user_only is None:
            pqs = Posture.objects.all()

        else:
            pqs = Posture.objects.filter(user__name=user_only)

        for posture in pqs:
            result.append(posture.to_dict())

        self.logger.debug("user_only: {}, result: {}".format(user_only, result))

        return result

    def add_user(self, user_info):
        """
            Adds a new user to the system.

            IMPLEMENTATION NOTE: HERE I WILL BE ASSUMING HAPPY PATH ALWAYS. IN A REAL IMPLEMENTATION WE SHOULD ALSO
            HAVE TO HANDLE/CONSIDER ANY ERROR THAT COULD ARISE DUE TO DATA ERROR (I.E., TOO LONG DATA, INVALID TYPE,
            ETC).

        :param user_info: (dict) Info of the user to be added. Follows the following format:

                {
                    "name" : <user_name>
                    "email": <email>
                    "password": <password>
                }

                with:

                    <user_name> : (str) User name
                    <email> : (str) Email address
                    <password> : (str) Password

        :return: (bool) True if the user was properly added. If either there is another user with the same name or
            there is any user_info data error it returns False, and the user is not added.
        """
        result = False
        try:
            user = User.objects.get(name=user_info["name"])
            self.logger.debug("Trying to add already existent user {}".format(user.name))

        except KeyError:
            # Bad input
            self.logger.error("Error while adding new user: missing field 'name' in user_info={}".format(user_info))

        except User.DoesNotExist:
            # OK, it does not exists. Add it
            new_user = User(**user_info)
            new_user.save()

            result = True
            self.logger.info("Added new user {}".format(user_info["name"]))

        return result

    def add_posture(self, posture_info, user_name):
        """
            Adds a new posture to the system.

            IMPLEMENTATION NOTE: HERE I WILL BE ASSUMING HAPPY PATH ALWAYS. IN A REAL IMPLEMENTATION WE SHOULD ALSO
            HAVE TO HANDLE/CONSIDER ANY ERROR THAT COULD ARISE DUE TO DATA ERROR (I.E., TOO LONG DATA, INVALID TYPE,
            ETC).

        :param posture_info: (dict) Info of the posture to be added. Follows the following format:

                {
                    "id": <id>,
                    "name" : <user_name>,
                    "picture": <email>,
                    "description": <description>
                }

                with:

                    <id> : (str) Unique 24-character-long hash that identifies the yoga posture
                    <name> : (str) Name of the yoga posture
                    <picture> : (str) Url of the picture that represents the yoga posture
                    <description> : (str) Textual description of the yoga posture

        :param user_name: (str) Name of the user that introduced the yoga posture. Must match with an already
            registered user in the system.

        :return: (bool) True if the user was properly added. If either there is another posture with the same id or
            the specified user does not exists or there is any posture_info data error, it returns False, and the
            posture is not added.
        """
        result = False
        try:
            posture = Posture.objects.get(id=posture_info["id"])
            self.logger.debug("Trying to add already existent posture {}".format(posture.id))

        except Posture.DoesNotExist:
            # OK, it does not exists. Add it
            try:
                user = User.objects.get(name=user_name)
                posture_info["user"] = user

                new_posture = Posture(**posture_info)
                new_posture.save()

                del posture_info["user"]

                result = True
                self.logger.info("Added new posture {}".format(posture_info["id"]))

            except User.DoesNotExist:
                # Trying to add a posture for a non registered user
                self.logger.error("Error while adding new posture: unknown user {}".format(user_name))

        except KeyError:
            # Bad input
            self.logger.error("Error while adding new user: missing field 'id' in posture_info={}".format(posture_info))

        return result
