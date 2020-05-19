# -*- coding: utf-8 -*-

"""
    pepipost

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import pepipost.models.mfrom
import pepipost.models.content
import pepipost.models.attachments
import pepipost.models.personalizations
import pepipost.models.settings
import pepipost.models.email_struct

class Send(object):

    """Implementation of the 'Send' model.

    Master modal

    Attributes:
        reply_to (string): email address which recipients can reply to.
        mfrom (From): email address representing the sender of the mail
        subject (string): Subject line of the email
        template_id (long|int): ID of the template to be used for sending the
            mail
        content (list of Content): content in text/plain format
        attachments (list of Attachments): attachment information
        personalizations (list of Personalizations): to recipient with some
            personalized data like to address, attachments and attributes
        settings (Settings): Enable/Disable settings like click, open and
            unsubscribe track
        tags (list of string): define custom tags to organize your emails
        lint_payload (bool): TODO: type description here.
        schedule (long|int): schedule the time of email delivery
        bcc (list of EmailStruct): Global bcc can be defined here

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mfrom":'from',
        "subject":'subject',
        "content":'content',
        "personalizations":'personalizations',
        "reply_to":'reply_to',
        "template_id":'template_id',
        "attachments":'attachments',
        "settings":'settings',
        "tags":'tags',
        "lint_payload":'lint_payload',
        "schedule":'schedule',
        "bcc":'bcc'
    }

    def __init__(self,
                 mfrom=None,
                 subject=None,
                 content=None,
                 personalizations=None,
                 reply_to=None,
                 template_id=None,
                 attachments=None,
                 settings=None,
                 tags=None,
                 lint_payload=None,
                 schedule=None,
                 bcc=None):
        """Constructor for the Send class"""

        # Initialize members of the class
        self.reply_to = reply_to
        self.mfrom = mfrom
        self.subject = subject
        self.template_id = template_id
        self.content = content
        self.attachments = attachments
        self.personalizations = personalizations
        self.settings = settings
        self.tags = tags
        self.lint_payload = lint_payload
        self.schedule = schedule
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
        mfrom = pepipost.models.mfrom.From.from_dictionary(dictionary.get('from')) if dictionary.get('from') else None
        subject = dictionary.get('subject')
        content = None
        if dictionary.get('content') != None:
            content = list()
            for structure in dictionary.get('content'):
                content.append(pepipost.models.content.Content.from_dictionary(structure))
        personalizations = None
        if dictionary.get('personalizations') != None:
            personalizations = list()
            for structure in dictionary.get('personalizations'):
                personalizations.append(pepipost.models.personalizations.Personalizations.from_dictionary(structure))
        reply_to = dictionary.get('reply_to')
        template_id = dictionary.get('template_id')
        attachments = None
        if dictionary.get('attachments') != None:
            attachments = list()
            for structure in dictionary.get('attachments'):
                attachments.append(pepipost.models.attachments.Attachments.from_dictionary(structure))
        settings = pepipost.models.settings.Settings.from_dictionary(dictionary.get('settings')) if dictionary.get('settings') else None
        tags = dictionary.get('tags')
        lint_payload = dictionary.get('lint_payload')
        schedule = dictionary.get('schedule')
        bcc = None
        if dictionary.get('bcc') != None:
            bcc = list()
            for structure in dictionary.get('bcc'):
                bcc.append(pepipost.models.email_struct.EmailStruct.from_dictionary(structure))

        # Return an object of this model
        return cls(mfrom,
                   subject,
                   content,
                   personalizations,
                   reply_to,
                   template_id,
                   attachments,
                   settings,
                   tags,
                   lint_payload,
                   schedule,
                   bcc)


