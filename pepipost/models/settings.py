# -*- coding: utf-8 -*-

"""
    pepipost

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import pepipost.models.email_struct

class Settings(object):

    """Implementation of the 'Settings' model.

    TODO: type model description here.

    Attributes:
        footer (bool): enable or disable footer
        click_track (bool): enable or disable click tracking
        open_track (bool): enable or disable open tracking
        unsubscribe_track (bool): enable or disable unsubscribe tracking
        bcc (list of EmailStruct): email address for bcc

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "footer":'footer',
        "click_track":'click_track',
        "open_track":'open_track',
        "unsubscribe_track":'unsubscribe_track',
        "bcc":'bcc'
    }

    def __init__(self,
                 footer=None,
                 click_track=None,
                 open_track=None,
                 unsubscribe_track=None,
                 bcc=None):
        """Constructor for the Settings class"""

        # Initialize members of the class
        self.footer = footer
        self.click_track = click_track
        self.open_track = open_track
        self.unsubscribe_track = unsubscribe_track
        self.bcc = bcc


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        footer = dictionary.get('footer')
        click_track = dictionary.get('click_track')
        open_track = dictionary.get('open_track')
        unsubscribe_track = dictionary.get('unsubscribe_track')
        bcc = None
        if dictionary.get('bcc') != None:
            bcc = list()
            for structure in dictionary.get('bcc'):
                bcc.append(pepipost.models.email_struct.EmailStruct.from_dictionary(structure))

        # Return an object of this model
        return cls(footer,
                   click_track,
                   open_track,
                   unsubscribe_track,
                   bcc)


