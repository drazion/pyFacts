pyFacts
=======

A pyFacts API that currently reaches out to numbersapi and catfacts to pull random facts and post them to twitter.
I have a bit of work to do on cleanup and documentation, there are currently some wonky ways the code is being
run, but it works.

You can see it in action at https://twitter.com/drazion

If you want to play around with it, you will need to create a keys.py in your parent folder and structure it as follows:

```python
class privateKeys():
    def __init__(self):
        self.consumer_key='your_key_here'
        self.consumer_secret='your_key_here',
        self.access_token_key='your_key_here',
        self.access_token_secret='your_key_here'
```
