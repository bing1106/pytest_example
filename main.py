import lib.trump_util as tutil
import lib.donald_trump as trump

def some_application():
    president = trump.Donald_Trump()
    president.publish_message("China! China! China!")
    print("Now he has: " + str(president.enemies))
    president.publish_message(tutil.concat_two_strings("Make America ", "Great Again!"))
    print("Now he has: " + str(president.enemies))
    del president
    
some_application()