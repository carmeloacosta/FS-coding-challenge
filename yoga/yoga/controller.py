
# Add logger
import logging
logger = logging.getLogger(__name__) #TODO: Replace logger with Dependency Injected global logger

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

        :return: (bool) True if the user was properly added. If there is another user with the same name it returns
            False, and the user is not added.
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
