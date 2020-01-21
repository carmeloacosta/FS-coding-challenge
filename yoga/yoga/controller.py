
# Add logger
import logging
logger = logging.getLogger(__name__) #TODO: Replace logger with Dependency Injected global logger

from .models import User, Posture


class Controller():
    """
        Implements the Yoga bussiness logic. It access the underlying data base system in order to persist the
        required data.
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
