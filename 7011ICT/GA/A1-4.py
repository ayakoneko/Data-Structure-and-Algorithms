## Searching System - lookup, insertion, deletion
#identified items solely by their weight for customer orders Balanced Binary Search Tree 
#item relocated or removed from the inventory over time
#if exact match is not found, return the closest available item (i.e. sorted order)
#Balanced Binary Search Tree to identify the insertion point 


class warehouse:
    def __init__(self):
        self.inventory=[]
    
    #find index of target_weight where it should be located (sorted order in binary tree), the combination of weight and item name will be saved under tuples

        def binary(self, target_weight):
            left, right=0, len(self.inventory)-1
            while left <= right:
                mid=(left+right)//2
                if self.inventory[mid][0] == target_weight:
                    return mid
                elif self.inventory[mid][0] < target_weight:
                    left= mid+1
                else:
                    right= mid-1
            return left #insertion point (balanced binary)
        
    def add_item(self, weight, name):
        index=self.binary(weight)
        #check if there is any existing item with same weight in inventory, if so add 1 on index until it reaches the last position of same weight
        while index < len(self.inventory) and self.inventory[index][0] == weight:
            index += 1
        self.inventory.insert(index, (weight, name))
        print (f"Item added - {name} with weight of {weight}")
        return (weight, name)
        
    def remove_item(self, weight):
        index=self.binary(weight)
        #find the first occurance when there is multiple item with same weight
        while index>0 and self.inventory[index-1][0]== weight:
            index -= 1
            
        if index < len(self.inventory) and self.inventory[index][0]== weight:
            removed_item= self.inventory.pop(index)
            print(f"Removed item - {removed_item[1]} with weight of {removed_item[0]}")
            return removed_item
        else:
            print(f"No items found with weight of {weight}")
            return None

    def search_item(self, weight):
        index=self.binary(weight)
        #find the first occurance when there is multiple item with same weight
        while index>0 and self.inventory[index-1][0]== weight:
            index -= 1
    
        #exact match
        if index < len(self.inventory) and self.inventory[index][0]== weight:   
            exact=self.inventory[index]  
            print(f"Search Result: Item with weight of {weight} - {exact}") 
            return exact
        
        #closest match
        else:
            #before and after of target
            before=self.inventory[index-1] if index > 0 else None
            after=self.inventory[index] if index < len(self.inventory) else None
                
            #neighbor check 
            if before is None:
                closest= after
            elif after is None:
                closest= before
            else:#compare closer wright between before and after
                closest= before if abs(before[0]-weight) <= abs(after[0]-weight) else after
            print(f"Search Result: Item with closest weight of {weight} - {closest[1]} with weight of {closest[0]}")
            return closest
    
    def display_all(self):
        print(self.inventory)
        return self.inventory

def inquiry():
    warehouse1=warehouse()

    while True:
        inquiry=input("Choose your request (add/remove/search/display/quit): ").strip().lower()
        
        if inquiry == "add":
            try:
                weight, item=input("Enter inventory (Weight, Item): ").split(",")
                warehouse1.add_item(float(weight.strip()), item.strip().lower())
            except: #input error
                print("Invalid input. Please use the format: weight,item (e.g., 4.5, item B)")

        elif inquiry == "remove":
            weight=input("Enter weight of item: ")
            warehouse1.remove_item(float(weight))

        elif inquiry == "search":
            weight=input("Enter weight of item: ")
            warehouse1.search_item(float(weight))

        elif inquiry == "display":
            warehouse1.display_all()

        elif inquiry == "quit":
            print("Exiting order system")
            break

        else:
            print("Invalid input, please try again")  

inquiry()










# ## Searching System - lookup, insertion, deletion
# #identified items solely by their weight for customer orders (dictionary with weight as key)
# #item relocated or removed from the inventory over time
# #if exact match is not found, return the closest available item (i.e. sorted order)

# class warehouse:
#     def __init__(self):
#         self.inventory={} #create dictionary
    
#     def add_item(self, weight, item):
#         if weight not in self.inventory:
#             self.inventory[weight]=[]
#         self.inventory[weight].append(item)
#         print(f"Added item - {item} with weight of {weight}")
    
#     def remove_item(self, weight):
#         if weight in self.inventory:
#             removed_item = self.inventory[weight].pop(0)
#             print(f"Removed item - {removed_item} with weight of {weight}")
#         else:
#             print(f"No items found with weight of {weight}")

#     def search_item(self, weight):
#         if weight in self.inventory:
#             # return self.inventory[weight][0]
#             print(f"Search Result: Item with weight of {weight} - {self.inventory[weight]}")        
#         else:
#             def difference(closeitem):
#                 return abs(closeitem-weight)
#             closest_weight=min(self.inventory.keys(), key=difference)
#             # return self.inventory[closest_weight][0]
#             print(f"Search Result: Item with closest weight of {weight} - {self.inventory[closest_weight]} with weight of {closest_weight}")
    
#     def display_inventory(self):
#         print(self.inventory)

# def inquiry():
#     warehouse1=warehouse()

#     while True:
#         inquiry=input("Choose your request (add/remove/search/display/quit): ").strip().lower()
        
#         if inquiry == "add":
#             weight, item=input("Enter inventory (Weight, Item): ").split(",")
#             warehouse1.add_item(float(weight), item.lower())

#         elif inquiry == "remove":
#             weight=input("Enter weight of item: ")
#             warehouse1.remove_item(float(weight))

#         elif inquiry == "search":
#             weight=input("Enter weight of item: ")
#             warehouse1.search_item(float(weight))

#         elif inquiry == "display":
#             warehouse1.display_inventory()
            
#         elif inquiry == "quit":
#             print("Exiting order system")
#             break

#         else:
#             print("Invalid input, please try again")  

# inquiry()


# warehouse1=warehouse()
# warehouse1.add_item(5.5, "ItemA")
# warehouse1.add_item(6.2, "ItemB")
# warehouse1.add_item(7, "ItemC")
# warehouse1.add_item(5.5, "ItemD")
# warehouse1.add_item(7.0, "ItemE")
# warehouse1.add_item(5.43, "ItemF")
# warehouse1.display_inventory()
# warehouse1.search_item(5.5)
# warehouse1.search_item(6.5)
# warehouse1.remove_item(5.5)
# warehouse1.search_item(5.5)
# warehouse1.display_inventory()


