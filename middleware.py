from django.utils.cache import patch_vary_headers
from django.utils import translation

class LanguageParamMiddleware(object):
    """
	Use lang param to force a language
    """
    def process_request(self, request):
        lang = request.GET.get('lang', None)
        if lang:
            translation.activate(lang)
            request.LANGUAGE_CODE = translation.get_language()


    def process_response(self, request, response):
        patch_vary_headers(response, ('Accept-Language',))
        translation.deactivate()
        return response

# vim:set ts=4 sw=4 et:
