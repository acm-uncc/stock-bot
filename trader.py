class Trader:
  def __init__(self, name):
    self.name = name
    self.id = f"trader_{name}"
    self.wallet = 