class Service(object):
    """
    Base class for service implementations in 'services' directory.
    """
    def __init__(self, data, api_key, destination_config):
        """
        Initialize service.

        :param data:                data to be transformed
        :param api_key:             api key for 3rd party
        :param destination_config:  destination config of search
        """
        self.data = data
        self.api_key = api_key
        self.destination_config = destination_config

    def process(self):
        """
        Abstract process method.Entry point for transform and push logic. This method should
        invoke transform and then push methods.
        """
        raise NotImplementedError

    def transform(self):
        """
        Abstract transform method. Converts data to 3rd push api data model. To be fully
        implemented in sub class.
        """
        raise NotImplementedError

    def push(self, payload):
        """
        Method that takes care of pushing business.

        :param payload: Payload to be pushed to 3rd party.
        :return:
        """
        return payload is not None
