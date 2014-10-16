import random
import requests
import json
from apilist import numbers
from apilist import catfacts

class Facts:
    def __init__(self):
        self.facts_list = ['catfacts', 'numbers']
        random.shuffle(self.facts_list)
        self.list_count = len(self.facts_list)
        self.facts_api = self.facts_list[0]

    def get_url(self):
        #Numbers API - http://numbersapi.com/
        if self.facts_api == 'numbers':
            fact = numbers.NumbersAPI()
            return fact.build_url()
        #Placeholder for catfacts
        elif self.facts_api == 'catfacts':
            fact = catfacts.CatfactsAPI()
            return fact.build_url()

    def send_request(self, url):
        print url
        result = requests.get(url)
        return self.parse_results(result)

    def parse_results(self, result):
        parsed_result = ''
        #Parse Numbers API Result
        if self.facts_api == 'numbers':
            if self.too_long(result.text) == 1:
                new_url = self.get_url()
                self.send_request(new_url)
            else:
                parsed_result = result.text
        #Parse CatFacts results
        elif self.facts_api == 'catfacts':
            tmp_result = json.loads(result.text)
            tmp_result = str(tmp_result["facts"])
            if self.too_long(tmp_result) == 1:
                new_url = self.get_url()
                self.send_request(new_url)
            else:
                parsed_result = tmp_result

        return parsed_result

    def too_long(self, text):
        if len(text) > 110:
            return 1
        else:
            return 0

facts = Facts()

url = facts.get_url()
api_response = facts.send_request(url)
print api_response

#api_response = facts.parse_results(api_response)

#print api_response