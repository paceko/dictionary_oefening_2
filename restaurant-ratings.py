

def restaurant_ratings(file_name):
    """Read a file and print out restaurant ratings in alphabetical order"""


    the_file = open(file_name)

    # dictionary to hold restaurant names and rating.
    rest_ratings = {}

    for line in the_file:
        line = line.rstrip()
        restaurant = line.split(":")

        rest_ratings[restaurant[0]] = restaurant[1]
    
    #sort the restaurant in alphabetical order
    ordered_restaurants = sorted(rest_ratings)



    for restaurant_name in ordered_restaurants:
        print "%s is rated at %s." %(restaurant_name, rest_ratings[restaurant_name])        


restaurant_ratings('scores.txt')