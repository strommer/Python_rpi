
UNITS_LENGTH = {'m': 1, 'cm' : 0.01, 'mm' : 0.001, 'km' : 1000, 'in' : 0.0254, 'ft' : 0.3048, 'yd' : 0.9144 ,'mi' : 1609.34}
UNITS_AREA = {'sq_m' : 1, 'sq_cm': 0.0001, 'sq_mm': 0.000001, 'sq_km': 1000000, 'sq_in' : 0.00064516, 'sq_ft' : 0.092903, 'sq_yd' : 0.836127, 'sq_mi' : 2589988, 'acres' : 4046.86}

def unit_check(self, other, operator):
		if self.unit == other.unit:
			return self, other
		if (self.unit in UNITS_LENGTH and
			other.unit in UNITS_AREA):
			raise Exception("Unit conversion error in expression: "+ str(self) + " " + operator + " " + str(other))
		if (other.unit in UNITS_LENGTH and
			self.unit in UNITS_AREA):
			raise Exception("Unit conversion error in expression: "+ str(self) + " " + operator + " " + str(other))
		u = convert_unit(self.unit, other.unit)
		other.value = other.value * u
		other.unit = self.unit
		return self, other

def convert_unit(unit1, unit2):
		if unit1 in UNITS_LENGTH or unit2 in UNITS_LENGTH:
			convert_rate1 = UNITS_LENGTH[unit1]
			convert_rate2 = UNITS_LENGTH[unit2]
		elif unit1 in UNITS_AREA or unit2 in UNITS_AREA:
			convert_rate1 = UNITS_AREA[unit1]
			convert_rate2 = UNITS_AREA[unit2]
		else: 
			raise Exception(" Invalid Units")
		return convert_rate2/convert_rate1

class length (object):
	def __init__(self,value=None, unit=None):
		if value == None:
			self.value = 1
		else:
			self.value = value
		if unit not in UNITS_LENGTH:
			raise AssertionError("Invalid unit")
		self.unit = unit
 
	def __str__(self):
		return "%g%s" %(self.value, self.unit)

	def __repr__(self):
		return "%g%s" %(self.value, self.unit)

	def __add__(self, other):
		if type(other) is int or type(other) is float:
			other = length(value=other, unit=self.unit)
		(self, other) = unit_check(self, other, '+')
		result = self.value + other.value
		return length(value=result, unit=self.unit)

	def __radd__(self, other):
		return self + other

	def __mul__(self, other):
		if type(other) is int or type(other) is float:
			return length(value=self.value * other, unit=self.unit)
		self.convert_to('m')
		(self, other) = unit_check(self, other, '*')
		result = self.value * other.value
		return area(value=result, unit='sq_m')

	def __rmul__(self, other):
		if type(other) is int or type(other) is float:
			return length(value=self.value * other, unit=self.unit)


	def __sub__(self, other):
		if type(other) is int or type(other) is float:
			other = length(value=other, unit=self.unit)
		(self, other) = unit_check(self, other, '-')
		result = self.value - other.value
		return length(value=result, unit=self.unit)

	def __rsub__(self, other):
		return self - other

	def __lt__(self, other):
		if type(other) is int or type(other) is float:
			other = length(value=other, unit=self.unit)
		(self, other) = unit_check(self, other, '<')
		if self.value < other.value:
			 return True
		else:
			return False

	def __gt__(self, other):
		if type(other) is int or type(other) is float:
			other = length(value=other, unit=self.unit)
		(self, other) = unit_check(self, other, '>')
		if self.value < other.value:
			 return True
		else:
			return False

	def __eq__(self, other):
		if type(other) is int or type(other) is float:
			return False
		(self, other) = unit_check(self, other, '==')
		if self.value == other.value:
			return True
		else:
			return False

	def __truediv__(self, other):
		if type(other) is int or type(other) is float:
			return length(value=self.value / other, unit=self.unit)
		else:
			raise Exception('Unit conversion error in expression: ' + str(self) + ' / ' + str(other) )

	def __rtruediv__(self, other):
		raise Exception('Unit conversion error in expression: ' + str(other) + ' / ' + str(self) )

	def convert_to(self, to_unit):
		temp = length(unit= to_unit)
		(temp, self)= unit_check(temp, self, 'to')
		return self


class area (object):
	def __init__(self,value=None, unit=None):
		self.value = value
		if unit not in UNITS_AREA:
			raise AssertionError("Invalid unit")
		self.unit = unit

	def __str__(self):
		return "%g%s" %(self.value, self.unit)

	def __repr__(self):
		return "%g%s" %(self.value, self.unit)

	def __add__(self, other):
		if type(other) is int or type(other) is float:
			other = area(value=other, unit=self.unit)
		(self, other) = unit_check(self, other, '+')
		result = self.value + other.value
		return area(value=result, unit=self.unit)

	def __radd__(self, other):
		return self + other

	def __sub__(self, other):
		if type(other) is int or type(other) is float:
			other = area(value=other, unit=self.unit)
		(self, other) = unit_check(self, other, '+')
		result = self.value - other.value
		return area(value=result, unit=self.unit)

	def __rsub__(self, other):
		return self - other

	def __lt__(self, other):
		if type(other) is int or type(other) is float:
			other = length(value=other, unit=self.unit)
		(self, other) = unit_check(self, other, '<')
		if self.value < other.value:
			 return True
		else:
			return False

	def __gt__(self, other):
		if type(other) is int or type(other) is float:
			other = length(value=other, unit=self.unit)
		(self, other) = unit_check(self, other, '>')
		if self.value > other.value:
			 return True
		else:
			return False

	def __eq__(self, other):
		if type(other) is int or type(other) is float:
			return False
		(self, other) = unit_check(self, other, '==')
		if self.value == other.value:
			return True
		else:
			return False

	def __mul__(self, other):
		if type(other) is int or type(other) is float:
			return area(value=self.value * other, unit=self.unit)
		else:
			raise Exception('Unit conversion error in expression: ' + str(self) + ' * ' + str(other) )

	def __rmul__(self, other):
		if type(other) is int or type(other) is float:
			return area(value=self.value * other, unit=self.unit)

	def __truediv__(self, other):
		if type(other) is int or type(other) is float:
			return area(value=self.value / other, unit=self.unit)
		if type(other) is length:
			self.convert_to('sq_m')
			other.convert_to('m')
			return length(value=self.value / other.value, unit = 'm')
		(self, other) = unit_check(self, other, '/')
		result = self.value / other.value
		return result

	def __rtruediv__(self, other):
		raise Exception('Unit conversion error in expression: ' + str(other) + ' / ' + str(self) )			

	def convert_to(self, to_unit):
		temp = area(unit= to_unit)
		(temp, self)= unit_check(temp, self, 'to')
		return self

def test_units():
    """
    >>> meter = length(value=1,unit='m')
    >>> print(meter)
    1m
    >>> millimeter = length(value=1,unit='mm')
    >>> print(millimeter)
    1mm
    >>> length1 = 1 * meter; print(length1)
    1m
    >>> length2 = 2 * meter; print(length2) 
    2m
    >>> length_1_2 = length1 + length2; print(length_1_2) 
    3m
    >>> length3 = 200 * millimeter; print(length3) 
    200mm
    >>> length1_3 = length1 + length3; print(length1_3) 
    1.2m
    >>> length1_4 = length2 - length1; print(length1_4) 
    1m
    >>> length1_3.convert_to('cm')
    120cm
    >>> area = length1_3 * length2; print(area)
    2.4sq_m
    >>> area / length1
    2.4m
    >>> area2 = area/2; print(area2)
    1.2sq_m
    >>> print(area2/area)
    0.5
    >>> length1 < length2
    True
    >>> area2 > area 
    False
    >>> area.convert_to('acres')
    0.000593052acres
    >>> length1 == length1
    True
    >>> length1 != length2
    True
    """
    import doctest
    doctest.testmod()


if __name__ == '__main__':
	test_units()