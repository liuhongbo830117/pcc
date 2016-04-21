﻿import uuid
from threading import currentThread
from recursive_dictionary import RecursiveDictionary

def get_type(obj):
  # both iteratable/dictionary + object type is messed up. Won't work.
  try:
    if hasattr(obj, "__dependent_type__"):
      return "dependent"
    if dict in type(obj).mro():
      return "dictionary"
    if hasattr(obj, "__iter__"):
      print obj
      return "collection"
    if len(set([float, int, str, unicode, type(None)]).intersection(set(type(obj).mro()))) > 0:
      return "primitive"
    if hasattr(obj, "__dict__"):
      return "object"
  except TypeError, e:
    return "unknown"
  return "unknown"

class spacetime_property(property):
  change_tracker = RecursiveDictionary()
  def __init__(self, tp, fget, fset = None, fdel = None, doc = None):
    setattr(self, "_type", tp)
    setattr(self, "_dimension", True)
    setattr(self, "_name", fget.func_name)
    setattr(self, "change", {})
    setattr(self, "_primarykey", None)

    property.__init__(self, fget, fset, fdel, doc)

  def setter(self, fset):
    prop = spacetime_property(self._type, self.fget, fset)
    for a in self.__dict__:
      setattr(prop, a, self.__dict__[a])
    return prop

  def __copy__(self):
    prop = Property(self.fget, self.fset)
    prop.__dict__.update(self.__dict__)
    return prop

  def __set__(self, obj, value, bypass = False):
    property.__set__(self, obj, value)
    if not hasattr(obj, "__start_tracking__"):
      return
    if not obj.__start_tracking__ or bypass:
      if self._primarykey and value == None:
        value = str(uuid.uuid4())
        obj._primarykey = self
      property.__set__(self, obj, value)
      return
    if not self._primarykey and "_primarykey" != self._name:
      type_name = get_type(value)
      store_value = value
      if type_name == "dependent":
        return
      elif type_name == "object":
        store_value = value.__dict__

      spacetime_property.change_tracker.setdefault(
        currentThread().getName(), RecursiveDictionary()).setdefault(
          obj.__class__, RecursiveDictionary()).setdefault(
            obj.__primarykey__, {})[self._name] = store_value
    else:
      setattr(obj, self._name, value, bypass = True)

class primarykey(object):
  def __init__(self, tp = None, default = True):
    self.type = tp if tp else "primitive"
    self.default = default

  def __call__(self, func):
    x = spacetime_property(self.type, func)
    x._primarykey = True
    return x

class dimension(object):
  def __init__(self, tp = None):
    self.type = tp if tp else "primitive"

  def __call__(self, func):
    x = spacetime_property(self.type, func)
    return x
   