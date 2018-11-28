# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.omni.campaign.Campaign import Campaign


class CampaignsResponse(DefaultObject):
    @property
    @serializable(name="campaigns", type=Campaign)
    def campaigns(self):
        """
        Property is a list of: Campaign
        """
        return self.get_field_value("campaigns")

    @campaigns.setter
    def campaigns(self, campaigns):
        """
        Property is a list of: Campaign
        """
        self.set_field_value("campaigns", campaigns)

    def set_campaigns(self, campaigns):
        self.campaigns = campaigns
        return self

    @property
    @serializable(name="campaignCount", type=int)
    def campaign_count(self):
        """
        Property is of type: long
        """
        return self.get_field_value("campaign_count")

    @campaign_count.setter
    def campaign_count(self, campaign_count):
        """
        Property is of type: long
        """
        self.set_field_value("campaign_count", campaign_count)

    def set_campaign_count(self, campaign_count):
        self.campaign_count = campaign_count
        return self