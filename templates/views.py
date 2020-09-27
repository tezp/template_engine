from django.http import JsonResponse

from TemplateEngine import settings
from templates import mongo_db


def result(func):
    def wrapper(*args, **kwargs):
        try:
            return_data = func(*args, **kwargs)
            result = {'result': return_data, 'status_code': 200}
        except Exception as e:
            if settings.DEBUG:
                result = {'result': repr(e), 'status_code': 500}
            else:
                # should not show exception msg in prod
                result = {'result': '', 'status_code': 500}
        return JsonResponse(result)

    return wrapper


@result
def template_api(request, customer_id):
    if request.method == 'POST':
        return insert(customer_id)
    else:
        return display(customer_id)


def insert(customer_id):
    mongo_db.insert(customer_id)
    return "success"


def display(customer_id):
    results = mongo_db.fetch_customer_template(customer_id)
    if not results:
        return "No Data Found"
    return results


def custom404(request, exception=None):
    return JsonResponse({
        'status_code': 404,
        'error': 'The resource was not found'
    })
