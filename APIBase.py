#Future planned abc
import abc

class APIBase(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def api_location(self):
        """
        Define the location of the API
        :return: string
        """
        return