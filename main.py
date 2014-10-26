import random
import requests

from apilist import numbers
from apilist import catfacts
from postTwitter import TwitterAPI

class Facts:
    def __init__(self):
        self.facts_list = ['catfacts', 'numbers']
        random.shuffle(self.facts_list)
        self.list_count = len(self.facts_list)
        self.facts_api_name = self.facts_list[0]
        self.facts_api = ''
        self.api_public_url = ''

    def get_url(self):
        #Numbers API - http://numbersapi.com/
        if self.facts_api_name == 'numbers':
            self.facts_api = numbers.NumbersAPI()
            self.api_public_url = self.facts_api.public_url
            return self.facts_api.build_url()
        #Catfacts API
        elif self.facts_api_name == 'catfacts':
            self.facts_api = catfacts.CatfactsAPI()
            self.api_public_url = self.facts_api.public_url
            return self.facts_api.build_url()

    #Send the request to the API
    def send_request(self, url):
        result = requests.get(url)
        #Pass the text of the result
        return self.parse_results(result.text)

    #Parse the result and then post the status
    def parse_results(self, result):
        #init parsed result
        parsed_result = ''

        #If the response length is too long for twitter - resend and call send_request again
        if self.too_long(result) == 1:
            new_url = self.get_url()
            self.send_request(new_url)
        #Else parse the response and pass it to post_status()
        else:
            self.post_status(self.facts_api.parse_response(result))

    #Post the status to twitter
    def post_status(self, text):
        text = '#PyFacts ' + text + ' ' + self.api_public_url
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