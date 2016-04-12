

def restaurant_ratings(file_name):
    """Read a file and returns dictionary of restaurant ratings."""

    the_file = open(file_name)

    # dictionary to hold restaurant names and rating.
    rest_ratings = {}

    for line in the_file:
        line = line.rstrip()
        restaurant = line.split(":")

        rest_ratings[restaurant[0]] = restaurant[1]
   
    the_file.close() 

    return rest_ratings

def print_sorted(my_dict):
    """Sort and print dictionary"""

    #sort the restaurant in alphabetical order
    ordered_restaurants = sorted(my_dict)

    for restaurant_name in ordered_restaurants:
        print "%s is rated at %s." %(restaurant_name, my_dict[restaurant_name])        


restaurants = restaurant_ratings('scores.txt')
#prompt the user for a new restraunt
# add it to your dictionary

#call dictionary print function

your_name = raw_input('What is your name? ')
name = raw_input('what is your restaurant name? ')
name_rating = raw_input('What is the restaurant rating? ')

restaurants[name] = int(name_rating)

print_sorted(restaurants)

