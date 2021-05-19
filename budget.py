class Category:
    def __init__(self,name):
      self.name=name
      self.ledger=[]
    def __str__(self):
       title= f"{self.name:*^30}\n"
       items=""
       total=0
       for item in self.ledger:
         items+=f"{item['description'][0:23]:23}" +f"{item['amount']:>7.2f}"+"\n"
         total+=item["amount"]
         
       output=title+items+"Total"+": "+str(total)
       return output

    def deposit(self,amount,description=""):
      self.ledger.append({"amount": amount, "description": description}) 
    def withdraw(self,amount,description="")   :
      if self.get_balance()>=amount:

        self.ledger.append({"amount": (-1*amount), "description": description})
        return True
      else:
        return False  
    def get_balance(self):
       m=0
       for i in self.ledger:
         m=m+i["amount"]
       return m
    def transfer(self,amount,budget):
       if self.get_balance()>=amount:
         self.ledger.append({"amount": (-1*amount), "description": "Transfer to {}".format(budget.name)})  
         budget.ledger.append({"amount": amount, "description": "Transfer from {}".format(self.name)}) 
         return True
       else:
         return False
    def check_funds(self,amount):
      if self.get_balance()>=amount:
        return True
      else:
        return False
    def get_withdrawls(self):
      total=0
      for item in self.ledger:
        if item["amount"]<0:
          total+=item["amount"]
      return total    


def truncate(n):
  multiplier=10
  return int(n*multiplier)/multiplier
def getTotals(Categories):
  total=0
  breakdown=[]
  for category in Categories:
    total+=category.get_withdrawls()
    breakdown.append(category.get_withdrawls())
  rounded=list(map(lambda x: truncate(x/total),breakdown))
  return rounded  
def create_spend_chart(categories):
    # percent=["100| "," 90| "," 80| "," 70| "," 60| "," 50| "," 40| "," 30| "," 20| "," 10| ","  0| "]
    # Categories_percent=Categories_percent(categories)
    res="Percentage spent by category\n"
    i=100
    totals=getTotals(categories)
    while i>=0:
      cat_spaces=" "
      for total in totals:
        if total*100>=i:
           cat_spaces+="o  "
        else :
          cat_spaces+= "   "
      res+=str(i).rjust(3)+"|"+cat_spaces+("\n")
      i-=10
    dashes="-"+"---"*len(categories)
    names=[]
    x_axis=""
    for category in categories:
      names.append(category.name)
    maxi=max(names,key=len)
    for x in range(len(maxi)):
      nameStr='     '
      for name in names:
        if x>=len(name):
           nameStr +="   "
        else:
          nameStr+=name[x]+"  "
      if x!=(len(maxi)-1):  
        nameStr+="\n"
      x_axis+=nameStr
    res+=dashes.rjust(len(dashes)+4)+"\n"+x_axis
    return res  

