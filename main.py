import random

class Facts:
    def __init__(self):
        self.facts_list = ['catfacts', 'numbers']
        random.shuffle(self.facts_list)
        self.list_count = len(self.facts_list)
        self.facts_api = self.facts_list[0]

facts = Facts()
print str(facts.facts_api)