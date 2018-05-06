# pynepal
python package to get info related to Nepal administrative and geographical information

## Installation 
pip install pynepal 

### Usages:

#### General info
```
import pynepal

>>> pynepal.president
'Bidhya Devi Bhandari'

>>> pynepal.capital
'Kathmandu'

>>> pynepal.total_states
7
>>> pynepal.density
'180'

>>> pynepal.population
'26,494,504'

>>> pynepal.area
147181
```

#### Get provinces information
```
>>> from pynepal import provinces
>>> provinces
[Province('Province no 1'), Province('Province no 2'), Province('Province no 3'), Province('Province no 4'), Province('Province no 5'), Province('Province no 6'), Province('Province no 7')]
``` 

#### Get province six info
```
>>> from pynepal import province_six

>>> province_six
Province('karnali pradesh')

# Get name
>>> province_six.name
'karnali pradesh'

# Get area info
>>> province_six.area
'30213'

# Get governer name 
>>> province_six.governer
'Durga Keshar Khanal'

# Get density info
>>> province_six.density
'175'

# Get human development index
>>> province_six.hdi
'0.478'

# Get CM name.
>>> province_six.chief_minister
'Mahendra Bahadur Shahi'

>>> province_six.capital
'Dhangadhi
```

#### Get all the district info of a province one
```
from pynepal import province_one

# province one district
>>> province_one.districts
[District('Pachthar'),...]

# province one patchar distrct information
>>> province_one.districts[0].name
'Pachthar'

# Get province no of this district
>>> province_one.districts[0].province
1

# Get total population of this district
>>> province_one.districts[0].population
1234
```