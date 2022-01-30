from functools import total_ordering

@total_ordering
class CountSalaries:
  
  def __init__(self, code):
    self._code = code
    self._value = 0
    
  def __eq__(self, other):
    if type(other) != CountSalaries:
      return False
    
    return self._code == other._code and self._value == other._value
  
  def __lt__(self, other):
    if self._value != other._value:
      return self._value < other._value
    
    return self._value < other._value
  
  def withdraw(self, value):
    self._value += value
    
  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self._code, self._value)
    