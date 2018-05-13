import json
from .utils import clean_string

# Parse all states
with open('pynepal/db/provinces.json', 'r') as json_provinces:
     json_provinces = json.load(json_provinces)

# Parse all districts.
with open('pynepal/db/districts.json', 'r') as json_districts:
     json_districts = json.load(json_districts)

# Parse all municipalities.
with open('pynepal/db/municipalities.json', 'r') as json_municipalities:
     json_municipalities = json.load(json_municipalities)


class AbstractObj(object):
    """
    Abstract class for state, district and municipalities,
    """

    def __init__(self, **kwargs):
        for attr, val in kwargs.items():
            # Convert to lower case if instance is string else do nothing
            attr = clean_string(attr) if isinstance(attr, str) else attr
            val = clean_string(val) if isinstance(val, str) else val
            if not hasattr(self, attr):
                setattr(self, attr, val)

    def __repr__(self):
        if hasattr(self, "name"):
            return "{}('{}')".format(self.__class__.__name__, getattr(self, "name").lower())


class lists(list):
    """
    Return the list object with  with overloaded . operator
    attributes are check against the attr_list
    """

    def __init__(self, *args, attr_list=[]):
        super(lists, self).__init__()
        self._attr_list = attr_list

        # append the items
        for item in args:
            self.append(item)

    def __getattr__(self, attrname):
        # If attribute is two word, split it and check in attr_list
        # attribute is given in the form of self.eastern_rukum
        attrname = " ".join(attrname.split("_"))

        if attrname not in self._attr_list:
            raise AttributeError("{} has no attribute {}".format(
                self.__class__.__name__, attrname))

        # Search the districts object and return the value.
        for item in self:
            if item.name == attrname:
                return item
        return list(filter(lambda item: item.name == attrname, self))[0]


class RuralMunicipality(AbstractObj):
    """
    Represent RuralMunicipality
    """
    pass


class Municipality(AbstractObj):
    """
    Class for municipality object
    """
    pass


class SubMetropolitan(AbstractObj):
    """
    Class for submetropolitian city
    """
    pass


class Metropolitan(AbstractObj):
    """
    Class for submetropolitian city
    """
    pass


# Create the list of metropolitian, submetropolitian, and municipalites and remote municipalities
metropolitans, sub_metropolitans, municipalities, rural_municipalities = list(
), list(), list(), list()

types = ("metropolitan", "submetropolitan",
         "municipality", "ruralmunicipality")

for item in json_municipalities:
    if item.get('type') in types:
        if item.get('type') == "metropolitan":
           metropolitans.append(Metropolitan(**item))

        elif item.get('type') == "submetropolitan":
            sub_metropolitans.append(SubMetropolitan(**item))

        elif item.get('type') == "municipality":
            municipalities.append(Municipality(**item))

        elif item.get('type') == "ruralmunicipality":
            rural_municipalities.append(RuralMunicipality(**item))


# name list of all metropolitans
metropolitan_names = list()
for metropolitan in metropolitans:
    # clean up metropolitan name
    name = getattr(metropolitan, "name", None)
    if name:
        metropolitan_names.append(clean_string(name))
    pass


# List of metropolitans, having attribute as metropolitan name
# metropolitans.kathmandu returns Metropolitan("Kathmandu")
metropolitans = lists(*metropolitans, attr_list=metropolitan_names)


# name list of all sub_metropolitans
sub_metropolitan_names = list()
for sub_metropolitan in sub_metropolitans:
    # clean up sub metropolitan name
    name = getattr(sub_metropolitan, "name", None)
    if name:
        sub_metropolitan_names.append(clean_string(name))

#  sub_metropolitians, municipalities, rural_municipalities
sub_metropolitans = lists(
    *sub_metropolitans, attr_list=sub_metropolitan_names)


# name list of all municipality
municipality_names = list()
for municipality in municipalities:
    # clean up sub municipality name
    name = getattr(municipality, "name", None)

    if name:
        municipality_names.append(clean_string(name))


# Municipalities list
municipalities = lists(*municipalities, attr_list=municipality_names)


# Name list of all rural municipality
rural_municipalities_names = list()
for rural_municipality in rural_municipalities:
    # clean up rural municipality name
    name = getattr(municipality, "name", None)
    if name:
        rural_municipalities_names.append(clean_string(name))


# rural municipalities list
rural_municipalities = lists(
    *rural_municipalities, attr_list=rural_municipalities_names)


class District(AbstractObj):
    """
    Class for district
    """
    pass


# Create List of districts using list type
districts = [District(**json_district) for json_district in json_districts]

# Create a list of districts that support (.) operator, example: districts.gulmi.name
# List of district name
district_names = []
for district in districts:
    name = getattr(district, "name")
    # Clean name example eastern rukum to eastern_rukum
    name = clean_string(name)
    district_names.append(name)

# List of districts
districts = lists(*districts, attr_list=district_names)


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

       # Create and return of list of districts
       return lists(*province_districts, attr_list=province_districts)

    @property
    def metropolitans(self):
        """
        Return the list of all metropolitans from this province
        """
        metropolitans_list = [
            metropolitan for metropolitan in metropolitans if metropolitan.province_no == self.province_no]
        return metropolitans_list

    @property
    def sub_metropolitans(self):
        """
        Return the list of all metropolitans from this province
        """
        sub_metropolitan_lists = [
            sub_metropolitan for sub_metropolitan in sub_metropolitans if sub_metropolitan.province_no == self.province_no]
        return sub_metropolitan_lists

    @property
    def municipalities(self):
        """
        Return the list of municipalities of this province
        """
        municipalities_list = [
            municipality for municipality in municipalities if municipality.province_no == self.province_no]

        return municipalities_list

    @property
    def rural_municipalities(self):
        """
        Return the list of municipalities of this province
        """
        rural_municipality_lists = [
            rural_municipality for rural_municipality in rural_municipalities if rural_municipality.province_no == self.province_no]

        return rural_municipality_lists


class _Provinces(list):
    """
    Return list of provinces
    """
    province_names = ("province_one", "province_two", "province_three",
                      "province_four", "province_five", "province_six", "province_seven")
    indexes = {"one": 1, "two": 2, "three": 3,
               "four": 4, "five": 5, "six": 6, "seven": 7}

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


# List of provinces
provinces = _Provinces()
