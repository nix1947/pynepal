# pynepal
python package to get info related to Nepal administrative and geographical information

## Installation 
pip install pynepal 

### Usages:

#### Get general info
```
import pynepal
>>> pynepal.population
'26,494,504'

>>> pynepal.provinces.province_five.districts.gulmi.area
>>> pynepal.provinces.province_one.districts
```

#### Get provinces information
```
>>> from pynepal import provinces
>>> provinces
[Province('sagarmatha pradesh'), Province('janakpur pradesh'), Province('kathmandu pradesh'), Province('annapurna pradesh'), Province('lumbini pradesh'), Province('karnali pradesh'), Province('mahakali pradesh')]
``` 

#### Get province five info
```
>>> from pynepal import province_five
>>> from pynepal import provinces

>>> province_five
Province('lumbini pradesh')


# Get name
>>> province_five.name
'lumbini pradesh'

# Get all metropolitan list of province five. 
>>> province_five.metropolitans

# Get submetropolitan list 
>>> provinces.province_five.sub_metropolitans

# Get all the municipalities list of province five
>>> provinces.province_five.municipalities

# Get all the gaupalika(rural muncipilites) of province five
>>> provinces.province_five.rural_municipalities

# Get the province five districts gulmi info 
>>> province_five.districts.gulmi.headquarter
'resunga'

# Know who is the CM
>>> provinces.province_five.chief_minister
'shankar pokhrel'

# Get human development index
>>> provinces.province_five.hdi
'0.519'
```

#### Get all the district info of a province one
```
from pynepal import province_five

# province one district
>>> province_five.districts
[District('kapilvastu'), District('parasi'),....]

# Get  district information
>>> provinces.province_five.districts.gulmi.province_no
5
```

## Links
- Website: [http://manojgautam.com.np/pynepal](http://manojgautam.com.np/pynepal)
- Documentation: [Documentation]()
- License: [License]()
- Releases: [Releases]()
- Code: [code]()
- Issue tracker: [Issue tracker]()
