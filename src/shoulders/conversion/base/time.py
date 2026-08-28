from shoulders.dimension.base import TIME
from shoulders.unit.unit import Unit

MINUTE = Unit('min', TIME, {'min': 1})
min = MINUTE

HOUR = Unit('h', TIME, {'h': 1})
h = HOUR
hr = HOUR

DAY = Unit('d', TIME, {'d': 1})
d = DAY

WEEK = Unit('wk', TIME, {'wk': 1})
wk = WEEK