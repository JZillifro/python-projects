"""
Assignment 4: Metaprogramming

The idea of this assignment is to get you used to some of the dynamic
and functional features of Python and how they can be used to perform
useful metaprogramming tasks to make other development tasks easier.
"""

import functools
import sys

def logcalls(prefix):
    """A function decorator that logs the arguments and return value
    of the function whenever it is called.

    The output should be to sys.stderr in the format:
    "{prefix}: {function name}({positional args}..., {keyword=args}...)" 
    and 
    "{prefix}: {function name} -> {return value}"
    respectively for call and return. The call line should
    be printed before the call and the return line after.
    This is important for recursive functions (it will make 
    the call and return lines show the actual nested 
    structure of the recursion).

    Look up functools.wraps and use it to make the function you return
    have the same documentation and name as the function passed in.

    This will be used like:
    @logcalls("test")
    def f(arg):
        return arg

    NOTE: Do not generate and then modify strings. Instead generate
    the string you wanted directly. Look at str.join and keep
    generator comprehensions in mind.
    """

    def deco(func):
        @functools.wraps(func)
        def wrap(*args, **kws):
            arguString = ""
            for i in args:
                if arguString == "":
                    arguString = repr(i)
                else:
                    arguString = ", ".join((arguString, repr(i)))
            keyString = ""
            for i in kws:
                i = "=".join((i, repr(kws.get(i))))
                if keyString == "":
                    keyString = i
                else:
                    keyString = ", ".join((i, keyString))

            if (arguString == "") and (keyString == ""):
                params = ""
            elif (arguString == ""):
                params = keyString
            elif (keyString == ""):
                params = arguString
            else:
                params = ", ".join((arguString, keyString))

            print(prefix, ": ", func.__name__, "(", params, ")", sep="", file=sys.stderr)
            returnVal = func(*args, **kws)
            print(prefix,": ", func.__name__, " -> ",repr(returnVal), sep="", file=sys.stderr)
            return returnVal

        return wrap
    return deco
