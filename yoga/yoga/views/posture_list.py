

import json

from django.views import View
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.template import loader

from ..controller import Controller

# For the sake of simplicity, in this test I will deactivate the CSRF protection for this test. In real production
# Cross Site Request Forgery Protection should be used.
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class PostureListView(View):
    """
        View that allows to retrieve all the postures
    """

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
        else:
            # HTML TEMPLATE VIEW
            template = loader.get_template('yoga/posture/get_all.html')
            context = {
                'posture_list': result
            }

            # Add session user name if available
            try:
                context["session_user"] = request.user.username
            except AttributeError:
                pass

            return HttpResponse(template.render(context, request))
