
import json
from django.views import View
from django.urls import reverse
from django.template import loader
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect

from ..forms import UserForm
from ..controller import Controller

# For the sake of simplicity, in this test I will deactivate the CSRF protection for this test. In real production
# Cross Site Request Forgery Protection should be used.
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class UserView(View):
    """
        View that allows to register new users
    """

    @staticmethod
    def check_valid_body(body):
        """
            Checks that the input body contains the specified format. That is,

             - A unique user name,
             - an email address,
             - and a password.

             IMPLEMENTATION NOTE: THIS IS THE TYPICAL PLACE TO CHECK THE CORRECTNESS OF THE INPUTS, ASSURING THAT THE
             INPUT DATA MATCHES THE DATA MODEL REQUIREMENTS (TYPES, STRING LENGTH, ETC). IN ORDER TO KEEP THIS TEST
             SIMPLE I WILL NOT INCLUDE IT BUT IT SHOULD BE ADDED IN A REAL IMPLEMENTATION.

        :return: (dict/None) The info of the properly specified body using the specified format; None otherwise.

            {
                "name": <user_name>,
                "email": <email>,
                "password": <password>
            }

            with:

                    <user_name> : (str) User name.
                    <email> : (str) User email address.
                    <password> : (int) User password.

        """
        result = None
        message = ""

        try:
            body = json.loads(body)
            result = {"name": str(body["name"]),
                      "email": str(body["email"]),
                      "password": str(body["password"])
                      }

        except json.decoder.JSONDecodeError:
            message = "Bad Body. It must be a JSON"

        except TypeError:
            message = "Bad Body. Expected json with 'name', 'email', and 'password' fields"

        except ValueError:
            message = "Bad Body. All input fields must be strings"

        return result, message

    @staticmethod
    def is_json_result(request):
        """
            Tells whether it is requested a json result or not.

        :param request: HTTP request
        :return: (bool) True if JSON result expected; False otherwise.
        """
        try:
            json_result = request.GET['json']
            result = bool(json_result)
        except MultiValueDictKeyError:
            result = False

        return result

    def post(self, request):
        """
            Adds a new user to the system.

        :param request: HTTP request
        :return: HTTP response with the number of sunlight hours of the specified apartment (as specified in the Code
            Challenge)
        """
        if self.is_json_result(request):
            #
            # JSON
            #
            result = False
            request_info, message = self.check_valid_body(request.body.decode())

            if request_info:
                controller = Controller()
                new_user = controller.add_user(request_info)

                if new_user:
                    # New user created
                    result = True
                    message = "Added new user"
                else:
                    # Could not create new user
                    pass
            else:
                # Bad parameters
                pass

            if result:
                return HttpResponse(message)
            else:
                return HttpResponseBadRequest(message)

        else:
            #
            # HTML TEMPLATE VIEW
            #

            # Create a form instance and populate it with data from the request:
            form = UserForm(request.POST)

            # check whether it's valid:
            if form.is_valid():
                # Create the new posture
                request_info = form.cleaned_data

                # Add the new user
                controller = Controller()
                new_user = controller.add_user(request_info)

                #TODO
                if new_user:
                    # New user created
                    pass
                else:
                    # Could not create new user
                    pass

                # redirect to a new URL
                return HttpResponseRedirect(reverse('login'))

    def get(self, request):
        """
            Allows to Add a new user.

        :param request: HTTP request
        :return: HTTP response
        """
        # Responsive response
        if not self.is_json_result(request):
            # HTML TEMPLATE VIEW
            form = UserForm()
            template = loader.get_template('yoga/user/add.html')
            context = {
                'form': form,
            }
            return HttpResponse(template.render(context, request))
