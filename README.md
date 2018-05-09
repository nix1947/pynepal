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
>>> province_five
Province('lumbini pradesh')

# Get name
>>> province_five.name
'lumbini pradesh'

# Get the province five districts gulmi info 
>>> province_five.districts.gulmi.headquarter
'resunga'

# Know who is the CM
>>> from pynepal import provinces
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