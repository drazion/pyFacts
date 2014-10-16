import random

class CatfactsAPI:
    def __init__(self):
        self.base_url = self.api_address()
        self.method_list = self.available_methods()
        self.chosen_method = self.choose_method()
        self.variables = self.build_variables()

    def api_address(self):
        return 'http://catfacts-api.appspot.com/api/facts'

    def available_methods(self):
        return ['?number=1']

    def choose_method(self):
        random.shuffle(self.method_list)
        return self.method_list[0]

    def build_variables(self):
        variables_string = self.chosen_method
        return variables_string

    def build_url(self):
        return self.base_url + str(self.chosen_method)