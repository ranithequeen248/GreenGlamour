def display_options():
    options = "(1) View Cart (2) Add to Cart (3) Unadd from Cart"
    selected_option = int(input(options))
    return selected_option
    
items = ["hi"]

def view_cart():
    num_items = len(items)
    print(f"{num_items} These are the items in your cart")
    print(items)
     
def add_item():
    thing = input("What do you want to add?")
    if thing in items:
        print(f"you already have {thing}!")
    else:
        items.append(thing)
        print(f"{thing} added to your cart!")

def unadd():
    view_cart()
    people = int(input("enter index of who you want to unfollow "))
    dropped_item = items.pop(people)
    print(f"Removed {dropped_item} from your cart!")
while True:
    selected_option = display_options()
    if selected_option == 1:
        view_cart()
    elif selected_option == 2:
        add_item()
    elif selected_option == 3:
        unadd()
    elif selected_option == 4:
        
        
        print("Goodbye!")
        break