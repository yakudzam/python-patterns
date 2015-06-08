#!/usr/bin/env python
 
class Hello(object):
    singleton = None
 
    def __new__(clz):
        if not clz.singleton:
            clz.singleton = object.__new__(clz)
        return clz.singleton
 
    def __init__(self):
        self.world = "world"
        return None
 
h = Hello()
h.hello = "hello"
 
print h.hello
print h
print h.world
 
x = Hello()
 
print x.hello
print x
print x.world