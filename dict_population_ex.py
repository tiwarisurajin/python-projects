def main() :
      op_inpt = input("Choose the opeation(add,remove,query): ").lower()
      if op_inpt == "add" :
        add()
      elif op_inpt == "remove" :
            remove()        
      elif op_inpt == "query" :             
            query()
    
    
    
    
    
    
def add():
        p= {"india":150,"china": 140 , "america": 32,"pakistan": 21}
        add_inpt = input("Enter the country to add : ").lower()

        if add_inpt in p :
              print("Country already exists")
              return
        else :
            p_inpt = input("Enter the population of country: ")
            p[add_inpt] = p_inpt
        for i,v in p.items() :
             print(i,"==>",v)

def remove() :
        p= {"india":150,"china": 140 , "america": 32,"pakistan": 21}
        remove_inpt = input("Enter the country to rmeove").lower
        if remove_inpt not in p :
              print("Coutnry do not exist")
              return
        else:
              p.pop(remove_inpt)
              for i,v in p.items() :
                print(i,"==>",v)

def query() :
        p= {"india":150,"china": 140 , "america": 32,"pakistan": 21}
        query_input = input("Enter the country name: ")
        if query_input not in p :
              print("Country does not exist")
              return
        else :
              print(p.items(query_input))
            