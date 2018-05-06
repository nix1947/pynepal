import json 

# Parse all states
with open('pynepal/db/state.json', 'r') as json_states:
     json_states = json.load(json_states)

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
    pass 

class SubMetropolitanCity(AbstractObj):
    pass 

class District(AbstractObj):
    pass 


# List of districts
districts = [] 
for json_district in json_districts:
    districts.append(District(**json_district))


class State(AbstractObj):
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

# List of states.
states = [] 
for json_state in json_states:
     states.append(State(**json_state))
  
