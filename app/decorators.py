from django.utils.decorators import method_decorator

def teste (function_decorator):
    def decorator(view_object):
        view_object.dispatch =method_decorator(function_decorator)
        return view_object
    
    return decorator
    