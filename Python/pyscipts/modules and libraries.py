Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import math
math.pi
3.141592653589793
#above is attribute
math.pow(2, 3)
8.0
#above is method
sin(30)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    sin(30)
NameError: name 'sin' is not defined. Did you mean: 'bin'?
from math import sin
sin(30)
-0.9880316240928618
x = 30
rad_x = math.radians(x)
math.sin(rad_x)
0.49999999999999994
help(math.radians())
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    help(math.radians())
TypeError: math.radians() takes exactly one argument (0 given)
help(math)
Help on built-in module math:

NAME
    math

DESCRIPTION
    This module provides access to the mathematical functions
    defined by the C standard.

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.

        The result is between 0 and pi.

    acosh(x, /)
        Return the inverse hyperbolic cosine of x.

    asin(x, /)
        Return the arc sine (measured in radians) of x.

        The result is between -pi/2 and pi/2.

    asinh(x, /)
        Return the inverse hyperbolic sine of x.

    atan(x, /)
        Return the arc tangent (measured in radians) of x.

        The result is between -pi/2 and pi/2.

    atan2(y, x, /)
        Return the arc tangent (measured in radians) of y/x.

        Unlike atan(y/x), the signs of both x and y are considered.

    atanh(x, /)
        Return the inverse hyperbolic tangent of x.

    cbrt(x, /)
        Return the cube root of x.

    ceil(x, /)
        Return the ceiling of x as an Integral.

        This is the smallest integer >= x.

    comb(n, k, /)
        Number of ways to choose k items from n items without repetition and without order.

        Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
        to zero when k > n.

        Also called the binomial coefficient because it is equivalent
        to the coefficient of k-th term in polynomial expansion of the
        expression (1 + x)**n.

        Raises TypeError if either of the arguments are not integers.
        Raises ValueError if either of the arguments are negative.

    copysign(x, y, /)
        Return a float with the magnitude (absolute value) of x but the sign of y.

        On platforms that support signed zeros, copysign(1.0, -0.0)
        returns -1.0.

    cos(x, /)
        Return the cosine of x (measured in radians).

    cosh(x, /)
        Return the hyperbolic cosine of x.

    degrees(x, /)
        Convert angle x from radians to degrees.

    dist(p, q, /)
        Return the Euclidean distance between two points p and q.

        The points should be specified as sequences (or iterables) of
        coordinates.  Both inputs must have the same dimension.

        Roughly equivalent to:
            sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))

    erf(x, /)
        Error function at x.

    erfc(x, /)
        Complementary error function at x.

    exp(x, /)
        Return e raised to the power of x.

    exp2(x, /)
        Return 2 raised to the power of x.

    expm1(x, /)
        Return exp(x)-1.

        This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.

    fabs(x, /)
        Return the absolute value of the float x.

    factorial(n, /)
        Find n!.

        Raise a ValueError if x is negative or non-integral.

    floor(x, /)
        Return the floor of x as an Integral.

        This is the largest integer <= x.

    fmod(x, y, /)
        Return fmod(x, y), according to platform C.

        x % y may differ.

    frexp(x, /)
        Return the mantissa and exponent of x, as pair (m, e).

        m is a float and e is an int, such that x = m * 2.**e.
        If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.

    fsum(seq, /)
        Return an accurate floating-point sum of values in the iterable seq.

        Assumes IEEE-754 floating-point arithmetic.

    gamma(x, /)
        Gamma function at x.

    gcd(*integers)
        Greatest Common Divisor.

    hypot(...)
        hypot(*coordinates) -> value

        Multidimensional Euclidean distance from the origin to a point.

        Roughly equivalent to:
            sqrt(sum(x**2 for x in coordinates))

        For a two dimensional point (x, y), gives the hypotenuse
        using the Pythagorean theorem:  sqrt(x*x + y*y).

        For example, the hypotenuse of a 3/4/5 right triangle is:

            >>> hypot(3.0, 4.0)
            5.0

    isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
        Determine whether two floating-point numbers are close in value.

          rel_tol
            maximum difference for being considered "close", relative to the
            magnitude of the input values
          abs_tol
            maximum difference for being considered "close", regardless of the
            magnitude of the input values

        Return True if a is close in value to b, and False otherwise.

        For the values to be considered close, the difference between them
        must be smaller than at least one of the tolerances.

        -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
        is, NaN is not close to anything, even itself.  inf and -inf are
        only close to themselves.

    isfinite(x, /)
        Return True if x is neither an infinity nor a NaN, and False otherwise.

    isinf(x, /)
        Return True if x is a positive or negative infinity, and False otherwise.

    isnan(x, /)
        Return True if x is a NaN (not a number), and False otherwise.

    isqrt(n, /)
        Return the integer part of the square root of the input.

    lcm(*integers)
        Least Common Multiple.

    ldexp(x, i, /)
        Return x * (2**i).

        This is essentially the inverse of frexp().

    lgamma(x, /)
        Natural logarithm of absolute value of Gamma function at x.

    log(...)
        log(x, [base=math.e])
        Return the logarithm of x to the given base.

        If the base is not specified, returns the natural logarithm (base e) of x.

    log10(x, /)
        Return the base 10 logarithm of x.

    log1p(x, /)
        Return the natural logarithm of 1+x (base e).

        The result is computed in a way which is accurate for x near zero.

    log2(x, /)
        Return the base 2 logarithm of x.

    modf(x, /)
        Return the fractional and integer parts of x.

        Both results carry the sign of x and are floats.

    nextafter(x, y, /, *, steps=None)
        Return the floating-point value the given number of steps after x towards y.

        If steps is not specified or is None, it defaults to 1.

        Raises a TypeError, if x or y is not a double, or if steps is not an integer.
        Raises ValueError if steps is negative.

    perm(n, k=None, /)
        Number of ways to choose k items from n items without repetition and with order.

        Evaluates to n! / (n - k)! when k <= n and evaluates
        to zero when k > n.

        If k is not specified or is None, then k defaults to n
        and the function returns n!.

        Raises TypeError if either of the arguments are not integers.
        Raises ValueError if either of the arguments are negative.

    pow(x, y, /)
        Return x**y (x to the power of y).

    prod(iterable, /, *, start=1)
        Calculate the product of all the elements in the input iterable.

        The default start value for the product is 1.

        When the iterable is empty, return the start value.  This function is
        intended specifically for use with numeric values and may reject
        non-numeric types.

    radians(x, /)
        Convert angle x from degrees to radians.

    remainder(x, y, /)
        Difference between x and the closest integer multiple of y.

        Return x - n*y where n*y is the closest integer multiple of y.
        In the case where x is exactly halfway between two multiples of
        y, the nearest even value of n is used. The result is always exact.

    sin(x, /)
        Return the sine of x (measured in radians).

    sinh(x, /)
        Return the hyperbolic sine of x.

    sqrt(x, /)
        Return the square root of x.

    sumprod(p, q, /)
        Return the sum of products of values from two iterables p and q.

        Roughly equivalent to:

            sum(itertools.starmap(operator.mul, zip(p, q, strict=True)))

        For float and mixed int/float inputs, the intermediate products
        and sums are computed with extended precision.

    tan(x, /)
        Return the tangent of x (measured in radians).

    tanh(x, /)
        Return the hyperbolic tangent of x.

    trunc(x, /)
        Truncates the Real x to the nearest Integral toward 0.

        Uses the __trunc__ magic method.

    ulp(x, /)
        Return the value of the least significant bit of the float x.

DATA
    e = 2.718281828459045
    inf = inf
    nan = nan
    pi = 3.141592653589793
    tau = 6.283185307179586

FILE
    (built-in)


import random
random.random()
0.4606650794815249
random.random()*100
13.886150146191667
random.randint(1, 10)
4
random.randint(1, 10)
6
l = ['h', 't']
random.choice(l)
'h'
random.choice(l)
'h'
random.choice(l)
'h'
random.choice(l)
'h'
random.choice(l)
'h'
random.choice(l)
't'
#os module
import os
os.getcwd()
'C:\\Users\\Pratyush Shrestha\\AppData\\Local\\Programs\\Python\\Python312'
#prints the current working directory
gamma(1/2)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    gamma(1/2)
NameError: name 'gamma' is not defined
math.gamma(1/2)
1.7724538509055159
math.gamma(5)
24.0
os.listdir
<built-in function listdir>
os.listdir()
['DLLs', 'Doc', 'etc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'python.exe', 'python3.dll', 'python312.dll', 'pythonw.exe', 'Scripts', 'share', 'tcl', 'vcruntime140.dll', 'vcruntime140_1.dll']
math.gamma(-1)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    math.gamma(-1)
ValueError: math domain error
math.gamma(0)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    math.gamma(0)
ValueError: math domain error
math.gamma(100)
9.332621544394415e+155
math.gamma(11)
3628800.0
math.gamma(50)
6.082818640342675e+62
math.gamma(10000)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    math.gamma(10000)
OverflowError: math range error
math.gamma(150)
3.8089226376305703e+260
math.gamma(200)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    math.gamma(200)
OverflowError: math range error
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2025, 6, 19, 12, 46, 57, 309050)
>>> datetime.now()
datetime.datetime(2025, 6, 19, 12, 47, 21, 447534)
>>> datetime.now()
datetime.datetime(2025, 6, 19, 12, 47, 24, 53581)
>>> datetime.today()
datetime.datetime(2025, 6, 19, 12, 48, 17, 248966)
>>> datetime.datetime.now().year
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    datetime.datetime.now().year
AttributeError: type object 'datetime.datetime' has no attribute 'datetime'
>>> datetime.now().year
2025
>>> datetime.now().microsecond
94579
>>> datetime.now().microsecond
99674
>>> datetime.now().microsecond
386887
>>> datetime.now().microsecond
239548
datetime.now().microsecond
>>> 
>>> datetime.now().microsecond
796748
>>> datetime.now().microsecond
164114
>>> datetime.now().microsecond
187796
datetime.now().microsecond
>>> 
>>> datetime.now().microsecond
900447
datetime.now().microsecond
>>> 
>>> datetime.now().microsecond
555415
datetime.now().microsecond
>>> 
>>> datetime.now().microsecond
188721
