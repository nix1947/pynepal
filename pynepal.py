import json 

# Parse all states
with open('pynepal/db/provinces.json', 'r') as json_provinces:
     json_provinces = json.load(json_provinces)

# Parse all districts.
with open('pynepal/db/districts.json', 'r') as json_districts:
     json_districts = json.load(json_districts)


class AbstractObj(object):
    """
    Abstract class for State, District class
    """
    def __init__(self, **kwargs):
        for attr, val in kwargs.items():
            if not hasattr(self, attr):
                setattr(self, attr, val)
    
     
    def __repr__(self):
        if hasattr(self, "name"):
            return "{}('{}')".format(self.__class__.__name__,getattr(self, "name"))
        
       
class Municipality(AbstractObj):
    """
    Class for municipality object
    """ 
    pass 

class SubMetropolitanCity(AbstractObj):
    """
    Class for submetropolitian city
    """
    pass 

class District(AbstractObj):
    """
    Class for district
    """
    pass 


# List of districts
districts = [] 
for json_district in json_districts:
    districts.append(District(**json_district))


class Province(AbstractObj):
    """
    State class to hold information about states of Nepal
    """

    @property
    def districts(self):
       """
       Return all the district of this state
       """
       province_districts = [dist for dist in districts if dist.province_no == self.province_no]
       return province_districts

# List of provinces.
provinces = [] 
for json_state in json_provinces:
     provinces.append(Province(**json_state))

# Sort province based on province no.
provinces.sort(key=lambda state: state.province_no)
