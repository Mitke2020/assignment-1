from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.

<<<<<<< HEAD
#print(products)

# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.

customer_preferences=[]
=======


# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.


>>>>>>> f60253f8995b3490d3d2ee3728a47f83ee07a2d0
response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    # Add the customer preference to the list
<<<<<<< HEAD
    customer_preferences.append(preference)
=======

>>>>>>> f60253f8995b3490d3d2ee3728a47f83ee07a2d0
    response = input("Do you want to add another preference? (Y/N): ").upper()
  

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.

<<<<<<< HEAD
customer_preferences=set(customer_preferences)
=======

>>>>>>> f60253f8995b3490d3d2ee3728a47f83ee07a2d0

# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []

<<<<<<< HEAD
for product in products:
    converted_product={"name":product["name"],"tags":set(product["tags"])}
    converted_products.append(converted_product)
=======

>>>>>>> f60253f8995b3490d3d2ee3728a47f83ee07a2d0


# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
<<<<<<< HEAD
    return len(product_tags & customer_tags)
    
=======
    pass
>>>>>>> f60253f8995b3490d3d2ee3728a47f83ee07a2d0




# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
<<<<<<< HEAD
    products_match=[]
=======
>>>>>>> f60253f8995b3490d3d2ee3728a47f83ee07a2d0
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
<<<<<<< HEAD
    for product in products:
        products_match.append((product["name"],count_matches(set(product["tags"]),customer_tags)))
    products_match.sort(key=lambda item:item[1],reverse=True)
    return  products_match
    
=======
    pass
>>>>>>> f60253f8995b3490d3d2ee3728a47f83ee07a2d0



# TODO: Step 7 - Call your function and print the results

<<<<<<< HEAD
x=recommend_products(products,customer_preferences)
print(x)
=======


>>>>>>> f60253f8995b3490d3d2ee3728a47f83ee07a2d0

# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
# 2. How might this code change if you had 1000+ products?
<<<<<<< HEAD


# 1. I have used the for loops mainly as we are working with the list of dictionaries, so in order to access and conveert tags for an example we have to get inside of each dictionary within that list, and also I have used 
# for loops to be able to check every product and its tags in the list.
# I have used the "&" to find the intersection for the tags matches, as it is the simplest command that I could use to find the intersection of the two sets
=======
>>>>>>> f60253f8995b3490d3d2ee3728a47f83ee07a2d0
