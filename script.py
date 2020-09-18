import flexmock

class Foobar(object):
  attr=1

  def __init__(self):
    self.attr=2

_realFoobar = type('_realFoobar', Foobar.__bases__, dict(Foobar.__dict__))
def mock_foobar(*args):
  obj = _realFoobar()
  flexmock(obj).should_receive("attr").and_return(3)
  return obj

flexmock(Foobar).should_receive("__new__").replace_with(mock_foobar)

a = Foobar()
print('instance', a.attr)
print('class', Foobar.attr)
print('type', type(a))