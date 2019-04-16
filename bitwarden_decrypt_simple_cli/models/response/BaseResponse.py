class BaseResponse:
    response = None

    def __init__(self, response):
        self.response = response

    def get_response_property_name(self, property_name, response=None, exact_name=False):
        if property_name is None or property_name == '':
            raise Exception('propertyName must not be null/empty.')

        if response is None and self.response is not None:
            response = self.response

        if response is None:
            return None

        if not exact_name and property_name not in response:
            if property_name[0] == property_name[0].upper():
                other_case_property_name = property_name[0].lower()
            else:
                other_case_property_name = property_name[0].upper()
            if len(property_name) > 1:
                other_case_property_name += property_name[1:]

            property_name = other_case_property_name
            if property_name not in response:
                property_name = property_name.lower()
            if property_name not in response:
                property_name = property_name.upper()
        return response.get(property_name)
