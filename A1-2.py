##Conditions##
## restaurant online food delivery order (FIFO), 
## while allowing customers to cancel before they're processed
## no priority levels, no need for reordering, no fixed number of order slots

#queue using array
# - 1. Add order: enqueue a new order
# - 2. Process order : dequeue and remove order from queue
# - 3. View next order: peek at next order w/o removing
# - 4. Cancel order: remove specific order from queue
# - 5. Check if empty: determine if there're pending orders


class RestaurantOrder:
    #create empty order queue list
    def __init__(self):
        self.queue=[]

    #1 add a new order
    def new_order (self, order):
        self.queue.append(order)
        print(f"Order added: {order}")

    #2 process next order (FIFO) and remove from the queue
    def process_order(self):        
        if self.empty_check():
            print("No orders to process")
        else:
            order_processed=self.queue.pop(0) #remove from top (index=0)
            print(f"Order processed: {order_processed}")
    
    #3 view next order without removing 
    def view_next_order(self):
        if self.empty_check():
            print("No pending order")
        else:
            print(f"Next order: {self.queue[0]}, Full order list: {self.queue}")
    
    #4 remove specific order from queue to cancel
    def cancel_order(self, order):        
        if order in self.queue:
            self.queue.remove(order) #remove first occurance of order
            print(f"Order cancelled: {order}")
        else:
            print(f"Order not found: {order}")
    
    #5 determine if there is any pending orders (result in boolean (True/False))
    def empty_check(self):
        return len(self.queue)==0

def inquiry():
    restaurant1=RestaurantOrder()

    while True:
        inquiry=input("Choose your request (add/process/view/cancel/check/quit): ").strip().lower()
        
        if inquiry == "add":
            order=input("Enter order (Your Name, Item, Quantity): ").lower()
            restaurant1.new_order(order)
        
        elif inquiry == "process":
            restaurant1.process_order()

        elif inquiry == "view":
            restaurant1.view_next_order()

        elif inquiry == "cancel":
            while True:
                order=input("Enter order (Your Name, Item, Quantity): ").lower()
                if order in restaurant1.queue:
                    restaurant1.cancel_order(order)
                    break
                else:
                    print("Order not found, please try again")

        elif inquiry == "check":
            print(f"Empty Check: {restaurant1.empty_check()}")
        
        elif inquiry == "quit":
            print("Exiting order system")
            break

        else:
            print("Invalid input, please try again")  

inquiry()




# restaurant1=RestaurantOrder()
# restaurant1.new_order("Mike potato 2")
# restaurant1.view_next_order()
# restaurant1.process_order()
# restaurant1.view_next_order()
# restaurant1.process_order()
# restaurant1.new_order("Katy fish 1")
# restaurant1.new_order("Mike chicken 3")
# restaurant1.new_order("Justin cheese 4")
# restaurant1.view_next_order()
# restaurant1.view_all()
# restaurant1.cancel_order("Katy fish 1")
# restaurant1.cancel_order("Mike fish 2")
# restaurant1.view_all()
# restaurant1.empty_check()