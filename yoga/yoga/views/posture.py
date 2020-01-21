

import json
import time

from django.views import View
from django.http import HttpResponse, HttpResponseBadRequest

from ..controller import Controller

# For the sake of simplicity, in this test I will deactivate the CSRF protection for this test. In real production
# Cross Site Request Forgery Protection should be used.
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class PostureView(View):
    """
        View that allows to add and retrieve postures
    """

    @staticmethod
    def check_valid_body(body):
        """
            Checks that the input body contains the specified format. That is,

             - A posture name,
             - an url of the yoga picture,
             - a textual description,
             - the name of an existent user
             - (Optional) time for posture id hashing

             IMPLEMENTATION NOTE: THIS IS THE TYPICAL PLACE TO CHECK THE CORRECTNESS OF THE INPUTS, ASSURING THAT THE
             INPUT DATA MATCHES THE DATA MODEL REQUIREMENTS (TYPES, STRING LENGTH, ETC). IN ORDER TO KEEP THIS TEST
             SIMPLE I WILL NOT INCLUDE IT BUT IT SHOULD BE ADDED IN A REAL IMPLEMENTATION.

        :return: (dict/None) The info of the properly specified body using the specified format; None otherwise.

            {
                "name": <posture_name>,
                "picture": <picture>,
                "description": <description>
                "user": <user_name>
                ["now": <timestamp>]
            }

            with:

                    <posture_name>: (str) Posture name.
                    <picture>: (str) Url of the yoga picture.
                    <description>: (str) A textual description of the yoga posture.
                    <user_name> : (str) User name.
                    <timestamp> : (int) Timestamp (in seconds)
        """
        result = None
        message = ""

        try:
            body = json.loads(body)
            result = {"name": str(body["name"]),
                      "picture": str(body["picture"]),
                      "description": str(body["description"]),
                      "user": str(body["user"]),
                      }

            result["now"] = body["now"]

        except json.decoder.JSONDecodeError:
            message = {"error": "Bad Body. It must be a JSON"}

        except TypeError:
            message = {"error": "Bad Body. Expected json with 'name', 'picture', 'description', and 'user' fields"}

        except ValueError:
            message = {"error": "Bad Body. All input fields must be strings"}

        except KeyError as e:
            if len(e.args) == 1 and e.args[0] == "now":
                # ASSUMPTION: ALL MANDATORY FIELDS CHECKED (CODE CHALLENGE SIMPLIFICATION)
                # Optional "now" field not included
                pass
            else:
                message = {"error": "Bad Body. Expected json with 'name', 'picture', 'description', and 'user' fields"}

        return result, message

    @staticmethod
    def is_json_result(request):
        """
            Tells whether it is requested a json result or not.

        :param request: HTTP request
        :return: (bool) True if JSON result expected; False otherwise.
        """
        json_result = request.GET['json']
        result = bool(json_result)
        return result

    @staticmethod
    def get_time(request_info):
        """
            Retrieves a timestamp.

        :param request_info: (dict) The info of the properly specified body using the specified format; None otherwise.
            (see self.check_valid_body return value).
        :return: (int) UNIX Timestamp (in seconds)
        """
        try:
            result = request_info["now"]
        except KeyError:
            result = int(time.time())

        return result

    def post(self, request):
        """
            Adds a new posture to the system.

        :param request: HTTP request
        :return: HTTP response
        """
        result = False
        request_info, message = self.check_valid_body(request.body.decode())

        if request_info:
            controller = Controller()
            if controller.is_valid_user(request_info["user"]):
                # Get hash time
                now = self.get_time(request_info)

                # Create a unique hash for the new posture
                request_info["id"] = controller.create_posture_hash(request_info, now)
                new_posture = controller.add_posture(request_info, request_info["user"])

                if new_posture:
                    # New user created
                    result = True
                    message = json.dumps({"id": request_info["id"]})
                else:
                    # Could not create new posture
                    pass

            else:
                # Unknown user
                message = {"error": "Unknown user"}

        else:
            # Bad parameters
            pass

        # Responsive response
        if self.is_json_result(request):
            if result:
                return HttpResponse(message)
            else:
                return HttpResponseBadRequest(json.dumps(message))

    def get(self, request):
        """
            Retrieves all the postures in the system.

        :param request: HTTP request
        :return: HTTP response
        """
        controller = Controller()
        result = controller.get_all_postures() #TODO: Very easy to get all postures info for a specific "user_name"

        # Responsive response
        if self.is_json_result(request):
            return HttpResponse(json.dumps(result))
