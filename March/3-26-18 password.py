class lock:
  def __init__(self, toppings):
    self.open = open
    self._opened = False

  @property
  def opened(self):
    return self._opened

  @opened.setter
  def opened(self, value):
    if value:
      password = input("Enter the password: ")
      if password == "Sw0rdf1sh!":
        self._opened = value
      else:
        raise ValueError("Alert! Intruder!")

lock = lock(["strong", "secure"])
print(lock.opened)
lock.opened = True
print(lock.opened)