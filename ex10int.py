import operator

# Unicode
# plus_minus_sign = "\u00B1"
# Ascii
plus_minus_sign = "+/-"

class Interval:
    """Represents a range of numeric values.

    The Interval class represents an approach to putting bounds on
    rounding errors.  For example, instead of stating someone's
    height as "2.0" meters, it might be more appropriate to say that a
    person's height is somewhere between 1.97 meters and 2.03
    meters, because of the measurement uncertainty.

    This uncertainty can be represented with this class as:
    Interval(min=1.97, max=2.03)

    Alternatively, this can be represented as:
    Interval(value=2.0, error=.03)   # 2.0 +/- .03 = [1.97, 2.03]

    Intervals have implications on arithmetic operations.
    See en.wikipedia.org/wiki/Interval_arithmetic for details.
    """

    """
    Exercise:
    
    For this assignment, a constructor is provided for you,
    and a method for converting the Interval to a String is provided.
    Do not change these methods!
    
    Your task is to complete the rest of the implementation,
    as needed to make the test cases succeed.

    Once you've successfully implemented logic to implement
    a few doctests, try to refactor your code so that you
    are not duplicating functionality/logic.  If you find
    yourself wanting to copy/paste function bodies, take a
    step back and see if there is a better way to do it.

    For example, you should hopefully see patterns
    that allow you to abstract much of your logic into a
    write a helper function, which can be invoked by each
    of your operators.  If you do this, then the body
    of each of your operators can be a single line of code
    (just to invoke your helper function).

    Hint: Look at the documentation of the operator module,
    which is already imported for you at the top of this file.
    """    
    
    def __init__(self, *, value=None, error=None, min=None, max=None):
        if (min is not None and max is not None and
            value is None and error is None):
            # Specified as a min/max range
            assert (max >= min)
            self.value = (min + max) / 2.0
            self.error = self.value - min
        elif (min is None and max is None):
            # Specified as a value/error
            self.value = value or 0
            self.error = error or 0
        else:
            # Other combinations are not supported
            raise AssertionError("Invalid parameter combination: ("
                "value=", value, ", error=", error,
                ", min=", min,   ", max=", max, ")")

    def __str__(self):
        if self.error:
            # Value Plus or Minus Error
            return "(%g %s %g)" % (self.value, plus_minus_sign, self.error)
        else:
            # If no error, just return the value by itself
            return "%g" % (self.value,)
        

def testInterval():
    """
    >>> ################# TEST CREATION #################
    >>> pi = Interval(value=3.14, error=.005)
    >>> radius = Interval(value=2)
    >>> pi2 = Interval(min=3.14158, max=3.14160)

    >>> ################# SHOW INFORMATION #################
    >>> # Raw components
    >>> print(pi.value, pi.error)
    3.14 0.005
    >>> print(radius.value, radius.error)
    2 0

    >>> print(pi)
    (3.14 +/- 0.005)
    >>> print(radius)
    2

    >>> # Following uses __repr__; to get this doctest
    >>> # to work, you must define the function Interval.__repr__
    >>> # so that it returns the expected string.
    >>> [pi, radius]
    [Interval(value=3.14, error=0.005), Interval(value=2)]

    ************************************************************"""
    MOVE_THIS_AS_NECESSARY_TO_STOP_DOCTEST_TESTING_HERE =       """
    Try to get one doctest working at a time, then move this block
    down, to work on the next doctest.
    ***************************************************************

    >>> # Print as interval using properties min/max
    >>> print("[%g, %g]" % (pi.min, pi.max))
    [3.135, 3.145]
    >>> print("[%g, %g]" % (radius.min, radius.max))
    [2, 2]

    >>> pi.__dict__.keys() == {'value','error'}
    True

    >>> "min" in pi.__dict__
    False
    
    >>> ################# ARITHMETIC #################
    >>> print ("Area1=", pi * radius * radius)
    Area1= (12.56 +/- 0.02)

    >>> print ("Area2=", pi2 * radius * radius)
    Area2= (12.5664 +/- 4e-05)
    >>> print("Area3=", pi * 2 * 2)
    Area3= (12.56 +/- 0.02)
    >>> print("Area4=", 2 * pi * 2)
    Area4= (12.56 +/- 0.02)

    >>> ################# Rectangle example #############
    >>> length = Interval(value=2.0, error=.05)
    >>> width = Interval(value=4.0, error=.05)
    >>> print("Rectangle(length=%s, width=%s)" % (length, width))
    Rectangle(length=(2 +/- 0.05), width=(4 +/- 0.05))
    >>> area = length * width
    >>> print("Area=", area)
    Area= (8.0025 +/- 0.3)
    >>> print("Perimeter=", 2 * length + 2 * width)
    Perimeter= (12 +/- 0.2)
    >>> print((area / width) - length)
    (0.00187529 +/- 0.150023)
    >>> print(0 in (area / width) - length)
    True
    >>> print(99 in (area / width) - length)
    False
    >>> print (99 > (area / width) - length)
    True
    >>> print (99 <= (area / width) - length)
    False
    """
    import doctest
    doctest.testmod()

if __name__ == "__main__":  testInterval()
