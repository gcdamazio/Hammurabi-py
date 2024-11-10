from Display import Display
from GameYear import GameYear


    ####  Game Start ####
    #### Title Card ##
Display.title_card()
def Play():
    game_year = GameYear()
    game_over = False      
        ### SUMMARY ###       
    Display.royal_report(game_year)
        #game_over = game_year.game_over_check() 

        # game_over = True #for testing
###### FIRST QUESTION BUY LAND

    while (game_over == False):
    
        Display.clear_terminal()
        game_year.inventory()
        game_year.askHowManyAcresToBuy()


####### SECOND QUESTION SELL LAND
        Display.clear_terminal()
        game_year.inventory()
        game_year.askHowManyAcresToSell()


####### THIRD QUESTION FEED PEOPLE
        Display.clear_terminal()
        game_year.inventory()    
        game_year.askHowMuchGrainToFeedPeople()


###### FOURTH QUESTION PLANT HARVEST
        Display.clear_terminal()
        game_year.inventory()
        game_year.askHowManyAcresToPlant()

######        

##### End of Year #####
        game_year.endOfYear()
        Display.royal_report(game_year)  


#    if __name__ == "__main__":
 #       hammurabi = Hammurabi()
  #      hammurabi.main()
if __name__ == "__main__":
    Play()