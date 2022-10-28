import math
class Category:
  def __init__(self,name):
    self.name = name
    self.ledger = []

  def __str__(self):
    output = self.name.center(30,'*') + '\n'
    total = 0
    for i in self.ledger:
      line = i["description"][:23].ljust(23) + "{:.2f}".format(i["amount"]).rjust(7) + '\n'
      total += i["amount"]
      output += line
    output += "Total: " + str(total)
    return output

  def deposit(self , amount , description=""):
    d = {}
    d["amount"] = amount
    d["description"] = description
    #remain
    self.remain = amount
    
    self.ledger.append(d)
  
  def withdraw(self,amount, description=""):
    if self.check_funds(amount) == True: 
      w = {}
      w["amount"] = -amount
      w["description"] = description
      self.ledger.append(w)
      return True
    else:
      return False
    
  def get_balance(self):
    balance = 0
    for i in self.ledger:
      balance += i["amount"]
      
    return balance
    
  def transfer(self, amount , category):
    if self.check_funds(amount) == True:
      #"Transfer to [Destination Budget Category]"
      self.withdraw(amount, "Transfer to " + category.name)
      #"Transfer from [Source Budget Category]"
      category.deposit(amount,"Transfer from " + self.name)
      return True
    else:
      return False
    
  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    return True

def create_spend_chart(categories):
  chart = 'Percentage spent by category\n'
  total = 0
  percentage = []
  expenses = {}
  count = 0
  max_len = 0
  
  for c in categories:
    for i in range(len(c.ledger)):
      if int(c.ledger[i]["amount"]) < 0:
        expenses[c.name] = int(c.ledger[i]["amount"])
        total += int(c.ledger[i]["amount"])
        count += 1
  
  for k, v in expenses.items():
    p = math.floor((v / total * 100) / 10) * 10
    percentage.append(p)
    if len(k) > max_len:
        max_len = len(k)

  for i in range(100, -1, -10):
    chart += str(i).rjust(3) + '|'
    for p in percentage: 
      if i <= p:
          chart += ' o '  
      else:
          chart += ' ' * 3
    chart += " \n"
                  
  chart += '    ' + ('-' * (count * 3 + 1)) + '\n'
  
  for i in range(max_len):
    chart += ' ' * 4
    
    for k in expenses:
      if i < len(k):
          chart += ' ' + k[i] + ' '
      else:
        chart += " " * 3
          
    if i == max_len - 1:
      chart += " "
    else:
      chart += " \n"     
  
  return chart
