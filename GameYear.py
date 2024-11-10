import math
import random


class GameYear:
    def __init__(self,num_of_yrs=1,wallet=2800,acresOwned=1000,acresPlanted=1000,population=100,immigrants=5,bushelRats=200,howManyPeopleStarved=0,harvest=3000,fertility=3,landValue=19,bushelsFed=0):
        self.num_of_yrs = num_of_yrs
        self.wallet=wallet
        self.acresOwned=acresOwned
        self.population=population
        #####
        self.immigrants = immigrants
        self.harvest = harvest
        self.bushelRats = bushelRats
        self.fertility = fertility
        self.landValue = landValue
        self.bushelsFed = bushelsFed
        self.acresPlanted = acresPlanted
        self.howManyPeopleStarved = howManyPeopleStarved
        self.bought = False

    def game_over_check (self):
        if (self.population <= 0):
            return True
        if (self.uprising == True):
            return True
        return False
    def inventory(self):
        inv = "Population: {population}  Money: {wallet}  Acres: {acresOwned}".format(**self.__dict__)
        y=f"YEAR: {self.num_of_yrs}"
        gaps = "  //                                                                                    //"
        edge = "  ////////////////////////////////////////////////////////////////////////////////////////"
        print(edge)
        print(gaps)
        print(f"  //",y.center(82),"//")
        print(f"  //",inv.center(82),"//")
        print (gaps)
        print(edge)
        print()
        print()

    def endOfYear(self):
        self.num_of_yrs = self.num_of_yrs + 1
        if (self.num_of_yrs == 11):
            GameYear.youWin()

    def youWin(self):
        print("YOU WIN!!")

    def upLoss(self):
        print("Too many people starved and your people rose up, you lose")
    def noPop(self):
        print("All the citizens are dead. You lose")

        ######### Gabi ########
    def askHowManyAcresToSell(self):
        ## Could you please add a if that checks if self.bought == false, else pass? That way no one
        #can buy and sell on the same turn.
        print(f"You have {self.acresOwned} acres.")
        print(f"Land is valued at {self.landValue} bushels an acre.")
        land_to_sell = int(input("How many acres do you want to sell? "))
        while(land_to_sell > self.acresOwned):
            # print(str(land_to_sell) + " is more than you own")
            print(f"{land_to_sell} is more than you own")
            land_to_sell = int(input(f"How many acres do you want to sell? You have {self.acresOwned} acres."))
        # bushels = bushels + land_to_sell * 19 needs to be in the playGame method because we do not have wallet in this method
        self.acresOwned = self.acresOwned - land_to_sell
        self.wallet = self.wallet + land_to_sell * self.landValue

    def plagueDeaths(self):
        chanceOfPlagues = random.randint(1,100)
        if chanceOfPlagues < 16:
            # print("Plague got you this year. Half your population is dead.")
            ### I commented out the prints because this outcome is announced in the royal report
            return self.population  // 2
        else:
            # print("Good news! No plagues this year")
            return self.population    
        
    def starvationDeaths(self):
        minToSurvive = self.population * 20  #the min. to survive is the number of people * 20 bushels
        #Number of deaths due starvation
        if self.bushelsFed < minToSurvive:
            howManyPeopleStarved = math.ceil((minToSurvive - self.bushelsFed) / 20) #math.ceil round up the number of dead people.
            # print("This many people starved " + str(howManyPeopleStarved)) 
            self.population = self.population-howManyPeopleStarved
            self.howManyPeopleStarved = howManyPeopleStarved
        else: 
            pass
        
    def uprising(self):
        if self.howManyPeopleStarved > ((self.population+self.howManyPeopleStarved) * 0.45):
            GameYear.upLoss()
        else: 
            pass    



        ####### Sharmin #######
    def askHowMuchGrainToFeedPeople(self):
        while (self.population >0):
            try:
                ask_to_feed_population = int(input("How many bushels you want to use for feeding the population? "))
                if ask_to_feed_population <= self.wallet:
                    return ask_to_feed_population
                else:
                    print(f"Please enter a number between 0 and available{self.wallet}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        ### This takes in the variable and makes the right checks, but doesn't actually do anything.
        ### you need to take the input, times it by twenty and then delete it from self.wallet and return that
        ### that to self.wallet


    def getHarvest(self):
        self.fertility = random.randint(1, 7)
        self.harvest = self.acresPlanted * self.fertility
        # print(harvest(acers, bushelsBeingUsedAsSeed))




######## ULAS ##########

    def askHowManyAcresToPlant(self):
        x = int(input("How many acres you want to plant?"))
        if(x > self.acresOwned):
            print("You don't have enough acres!")
            GameYear.askHowManyAcresToPlant()
        elif(x > 10 * self.population):
            print("You don't have enough population!")
            GameYear.askHowManyAcresToPlant()
        elif(2*x >self.wallet):
            print("You don't have enough grain!")
            GameYear.askHowManyAcresToPlant()
        else: 
            self.wallet = self.wallet - 2*x
            self.acresPlanted = self.acresPlanted

    def grainEatenByRats(self):
        x = random.randint(0, 1) * 10
        if(x>40):
            self.bushelRats = 0
        else:
            x = random.randint(1, 3) * 10
            self.bushelRats = x * self.wallet
            ##### This still needs a line that subtracts self.bushelRats 
            # from self.wallet and return or set it to equal self.wallet
            
    def newCostOfLand(self):
        self.landValue = random.randint(17, 23)

###### Maisha #######
    def askHowManyAcresToBuy(self):
        # while True:   I commented this out because it looped forever.
        acres = int(input("How many acres of land would you like to buy?\n")) 
        if acres > 0 and acres * self.landValue <= self.wallet:
            self.acresOwned += acres
            self.wallet -= acres * self.landValue
                ##### I think there's a missing varriable like total(landvaule*acres), or something. 
                #The next line looks at the value which is 17-23 and the wallet will almost always be bigger
                #Also, could you please add self.bought == True? I will have Gabi add a check for it at the top
                #There will be a check at the top of sell to stop it from being asked if they bought.
        elif self.landValue > self.wallet:
            print("Land value is", self.landValue, "bushels per acre. You don't have enough bushels to purchase. Try again! ")
        elif acres == 0 or acres < 0:
            print("Must enter a positive number to buy land.")
                ### I think taking in 0 is fine. If they don't buy, they get to sell.
                #If 0, just pass I think.

    def immigrants(self):
        if self.peopleStarved == 0:
            self.immigrants = (( 20*self.acresOwned + self.grainInStorage) // (100 * self.population) + 1)
        ### This needs a line that adds the immigrants to the pop 
