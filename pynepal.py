import json

# Parse all states
with open('pynepal/db/provinces.json', 'r') as json_provinces:
     json_provinces = json.load(json_provinces)

# Parse all districts.
with open('pynepal/db/districts.json', 'r') as json_districts:
     json_districts = json.load(json_districts)


class AbstractObj(object):
    """
    Abstract class for State, District
    """

    def __init__(self, **kwargs):
        for attr, val in kwargs.items():
            # Convert to lower case if instance is string else do nothing
            attr = attr.lower() if isinstance(attr, str) else attr
            val = val.lower() if isinstance(val, str) else val
            if not hasattr(self, attr):
                setattr(self, attr, val)

    def __repr__(self):
        if hasattr(self, "name"):
            return "{}('{}')".format(self.__class__.__name__, getattr(self, "name").lower())


class RuralMuncipality(AbstractObj):
    """
    Represent RuralMuncipality
    """
    pass


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


class MetropolitanCity(AbstractObj):
    """
    Class for submetropolitian city
    """
    pass


class District(AbstractObj):
    """
    Class for district
    """
    pass


class _Districts(list):
    """
    Return a list of districts with max value of 77 
    """
    # List of districts name
    districts_name = [district.get("name").lower()
                      for district in json_districts]

    def __init__(self):
        super(_Districts, self).__init__()

        # parse districts
        for json_district in json_districts:
            self.append(District(**json_district))
        
    def __getattr__(self, attrname):
        if attrname not in self.districts_name:
                raise AttributeError("{} has no attribute {}".format(self.__class__.__name__, attrname))
        
        # Search the districts object and return the value. 
        return list(filter(lambda district: district.name == attrname, self))[0]    


# Create districts
districts = _Districts()  # return modified list of districts


class Province(AbstractObj):
    """
    State class to hold information about states of Nepal
    """

    @property
    def districts(self):
       """
       Return all the district of this state
       """
       province_districts = [
           dist for dist in districts if dist.province_no == self.province_no]
       return province_districts


class _Provinces(list):
    """
    Return list of provinces
    """
    province_names = ("province_one", "province_two", "province_three",
                      "province_four", "province_five", "province_six", "province_seven")
    indexes = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6}

    def __init__(self):
        super(_Provinces, self).__init__()

        for json_province in json_provinces:
            self.append(Province(**json_province))
        # Sort province based on province no.
        self.sort(key=lambda state: state.province_no)

    def __getattr__(self, attrname):
        """
        nepal_provinces = _Provinces()
        nepal_provinces.province_one
        """
        if attrname not in self.province_names:
            raise AttributeError("{} has no attribute {}".format(
                self.__class__.__name__, attrname))

        _, index = attrname.split("_")
        return self[self.indexes.get(index)-1]



# Create provinces
provinces = _Provinces()
