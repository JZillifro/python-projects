"""Implement a class called TreeDict that supports operators the same
way as a dict. 

TreeDict should be implemented using the binarysearchtree module I
have provided (you can download it from canvas in the same folder as
this file).

You need to make sure you support the following operations with the
same semantics as a normal Python dict:
* td[key]
* td[key] = value
* key in td
* td.get(key)
* td.get(key, default)
* td.update(iterable_of_pairs_or_dict_or_TreeDict)
* len(td)
* for key in td: pass
* for key, value in td.items(): pass
* A constructor: TreeDict(iterable_of_pairs_or_dict_or_TreeDict)

Iteration should be in key order, this should be pretty easy to do
just by traversing the tree using an in-order traversal. None of the
iterator methods should make a copy of any of the data in the
TreeDict. You should only implement in-order traversal once and use
that implementation for both kinds of traversal.

You should support a constructor which takes the same arguments as
update and creates a TreeDict with just those values. There is an easy
way to do this in just a couple of lines using your existing update
method.

For each operation, make sure it does the same thing as a dict and you
handle errors by throwing the same type of exception as would be thrown
by a dict. However unlike dict your implementation will not support
None as a key and you should throw an appropriate exception if None is
used as a key. Look at the available built in exceptions and pick the
most appropriate one you find.

Most of these methods will be very short (just a couple of lines of
code), a couple will be a bit more complicated. However all the hard
work should already be handled by the binarysearchtree module. It
looks like a lot of operations, but it shouldn't actually take that
long. Many of the operations are quite similar as well.

Do not reimplement anything in the binarysearchtree module or copy
code from it. You should not need to.

For this assignment I expect you will have to use at least the
following things you have learned:
* Raising exceptions
* Catching exceptions
* Implementing magic methods
* Generators using yield (and you will need to look up "yield from" in the Python documentation)
* Type checks
* Default values/optional arguments

You will also need to read code which I think will help you learn to
think in and use Python.

To reiterate some of the things you should be aware of to avoid losing
points:
* None of the iterator methods should make a copy of any of the data
  in the TreeDict.
* You should only implement in-order traversal once and it should be
  recursive (it's so much easier that way).
* Do not reimplement anything in the binarysearchtree module or copy
  code from it.
* There are easy ways to implement all the required operations. If
  your implementation of a method is long you may want to think if
  there is a simpler way.

Links:
* https://docs.python.org/3.5/library/stdtypes.html#dict
* http://en.wikipedia.org/wiki/Binary_search_tree#Traversal
* https://docs.python.org/3.5/reference/expressions.html#yieldexpr

"""
from binarysearchtree import Node


class TreeDict:

    def __init__(self, args = dict()):
        self.root = Node()
        self.size = 0
        self.update(args)

    def update(self, args):
        # self.root = Node()
        # self.size = 0
        for e in args:
            if e is not None:
                if type(e) is tuple:
                    a = e[0]
                    b = e[1]
                else:
                    a = e
                    b = args[e]
                self.root.insert(a, b)
                self.size += 1
            else:
                raise KeyError("None is not a valid key")


        # if type(args) is dict:
        #     print("HEY")
        #     for e in args:
        #         self.root.insert(e, args[e])
        #         self.size += 1
        # elif type(args) is TreeDict:
        #     print("HO")
        #     for e in args:
        #         if e != None:
        #             self.root.insert(e, args[e])
        # elif iter(args):
        #     temp = iter(args)
        #     if (sum(1 for e in temp)%2) == 0:
        #         temp = iter(args)
        #         for a,b in temp:
        #             self.root.insert(a, b)
        #     else:
        #         raise ValueError("Iter, but not of pairs")


        # else:
        #     raise ValueError("bad type")

    def __getitem__(self, key):
        if type(self.root.key) != type(key):
            raise KeyError(".*"+key+".*")
        try:
            temp = self.root.lookup(key)
            return temp.value
        except ValueError:
            return None
    def __setitem__(self, key, value):

        try:
            temp = self.root.lookup(key)
            temp.value = value
        except ValueError:
            if self.__contains__(key):
                self.size -= 1
            self.root.insert(key, value)
            self.size += 1


    def __contains__(self, item):
        try:
            self.root.lookup(item)
        except ValueError:
            return False
        return True

    def get(self, key, default=None):
        if key in self:
            return self[key]
        return default

    def __len__(self):
        return self.size



    def __iter__(self):
        yield from in_order(self.root)

    def items(self):
        # result = ()
        # for e in self:
        #     result.__add__(tuple((e, self[e])))
        # return result
        return [(e, self[e]) for e in self]

def in_order(cur_node):
    if cur_node is not None:
        yield from in_order(cur_node.left)
        yield cur_node.key
        yield from in_order(cur_node.right)





