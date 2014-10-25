import random
import requests
import json

from apilist import numbers
from apilist import catfacts
from postTwitter import TwitterAPI

class Facts:
    def __init__(self):
        self.facts_list = ['catfacts', 'numbers']
        random.shuffle(self.facts_list)
        self.list_count = len(self.facts_list)
        self.facts_api = self.facts_list[0]
        self.api_public_url = ''

    def get_url(self):
        #Numbers API - http://numbersapi.com/
        if self.facts_api == 'numbers':
            fact = numbers.NumbersAPI()
            self.api_public_url = fact.public_url
            return fact.build_url()
        #Placeholder for catfacts
        elif self.facts_api == 'catfacts':
            fact = catfacts.CatfactsAPI()
            self.api_public_url = fact.public_url
            return fact.build_url()

    def send_request(self, url):
        result = requests.get(url)
        #Pass the text of the result
        return self.parse_results(result.text)

    def parse_results(self, result):
        parsed_result = ''
        if self.too_long(result) == 1:
            new_url = self.get_url()
            self.send_request(new_url)
        #Parse Numbers API Result
        if self.facts_api == 'numbers':
            parsed_result = result
            self.postStatus(parsed_result)
        #Parse CatFacts results
        elif self.facts_api == 'catfacts':
            tmp_result = json.loads(result)
            tmp_result = str(tmp_result["facts"])
            tmp_result = tmp_result.replace('[u\'', '')
            tmp_result = tmp_result.replace('\']', '')
            parsed_result = tmp_result
            self.postStatus(parsed_result)

        #return str(parsed_result)

    def postStatus(self, text):
        text = '#PyFacts ' + text + ' ' + self.api_public_url
        #text = 'Testing pyFacts API'
        api = TwitterAPI(text)
        api.postStatus()


    def too_long(self, text):
        if len(text) > 110:
            return 1
        else:
            return 0

facts = Facts()

url = facts.get_url()
api_response = facts.send_request(url)

#api_response = facts.parse_results(api_response)

#print api_response