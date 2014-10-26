import random

class NumbersAPI:
    def __init__(self):
        self.public_url = 'http://goo.gl/i18CPK'
        self.base_url = self.api_address()
        self.method_list = self.available_methods()
        self.chosen_method = self.choose_method()
        self.variables = self.build_variables()

    def api_address(self):
        return 'http://numbersapi.com/'

    def available_methods(self):
        return ['math', 'trivia', 'date']

    def choose_method(self):
        random.shuffle(self.method_list)
        return self.method_list[0]

    def build_variables(self):
        variables_string = ''
        if(self.chosen_method == 'math'):
            variables_string = random.randint(0, 600)
        elif(self.chosen_method == 'trivia'):
            variables_string = random.randint(0, 790)
        elif(self.chosen_method == 'date'):
            month = str(random.randint(1,12))
            date = 1
            thirty_days = [4, 6, 9, 11]
            if(month == 2):
                date = random.randint(1, 29)
            elif(month in  thirty_days):
                date = random.randint(1, 30)
            else:
                date = random.randint(1, 31)

            variables_string =  str(month) + '/' + str(date)

        return variables_string

    def parse_response(self, result):
       return result

    def build_url(self):
        return self.base_url + str(self.variables) + '/' + str(self.chosen_method)


