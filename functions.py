"""A collection of function for doing my project."""

import random

### class to create a new player and it has several methods to analyze, compare and get stats from players
class BasketballPlayer():
 


    def __init__(self, name = '', appearance = 0, points = 0, rebounds = 0, assists = 0,
                 steals = 0, blocks = 0, throw = 0, field_goal = 0):

        """create a new player based on real data

        Parameters
        ----------
        Instance Attributes
        name, points, rebounds, assists, steals, blocks, throw, field_goal

        Returns
        -------
        None
        """

        # put input to the instance attributes
        self.name = name
        self.appearance = appearance
        self.points = points
        self.rebounds = rebounds
        self.assists = assists
        self.steals = steals
        self.blocks = blocks
        self.throw = throw
        self.field_goal = field_goal

        
        
    def shoot(self):

        """

        This method is just for fun!  Try to see how efficiently the player can get the shoot

        """

        # calcululate the percentage
        percentage = round(self.field_goal/self.throw,2) * 100
        
        # get the possibility, a number between 0 and 100
        possibility = random.randint(0,100)
        
        # get the ball or miss the ball according to the possibility
        if possibility < percentage:
            print( "Nice shoot for " + str(self.name) +
                   ". His overall field goal percentage is around " + str(percentage) + "%.")
        else:
            print( str(self.name) + " missed it." 
                  " His overall field goal percentage is around " + str(percentage) + "%.")

            
            
    def getTotalStats(self):
        
        """Print the total statistics of the player

        Parameters
        ----------
        None

        Returns
        -------
        String: A String containing the total statistics
        """

        # get the String of total statistics for a whole career of the player
        total_data = "     " + str(self.name) + "'s total statistics\n"
        total_data += "He has totally played " + str(self.appearance) + " games. He got "
        total_data += str(self.points) + " points, " + str(self.rebounds) +" rebounds, " + str(self.assists)
        total_data += " assists, " + str(self.steals) + " steals and " + str(self.blocks) + " blocks."

        # return the output
        return total_data

    
    
    def getAverage(self):

        """Print the average statistics for one game of the player

        Parameters
        ----------
        None

        Returns
        -------
        String: A String containing the average statistics
        """

        # calculate each data by dividing it by the whole appearances for player's
        # whole career and add them to a String
        average_data = "     " + str(self.name)+"'s average data\n"
        average_data += str(self.name) + " can get "
        average_data += str(round(self.points/self.appearance,2)) + " points, "
        average_data += str(round(self.rebounds/self.appearance,2)) + " rebounds, "
        average_data += str(round(self.assists/self.appearance,2)) + " assists, "
        average_data += str(round(self.steals/self.appearance,2)) + " steals and "
        average_data += str(round(self.blocks/self.appearance,2)) + " blocks in every game."
        average_data += " His field goal percentage is " + str(round(self.field_goal/self.throw,4) * 100) + "%."

        # return output
        return average_data

    
   
    def addGame(self,points,rebounds,assists,steals,blocks,throw,field_goal):

        """add a game and change the statistics of the player

        Parameters
        ----------
        Instance attributes
        points,rebounds,assists,steals,blocks,throw,field_goal
        to add

        Returns
        -------
        None
        """

        # add the input to the statistics
        self.appearance += 1
        self.points += points
        self.rebounds += rebounds
        self.assists += assists
        self.steals += steals
        self.blocks += blocks
        self.throw += throw
        self.field_goal += field_goal
        

        
    def compareAverage(self,player):

        """compare average data between two players

        Parameters
        ----------
        player         another player to compare with

        Returns
        -------
        String: a String that tells the result of comparison
        """

        # calculate the average statistics for one game of two players
        points1 = self.points / self.appearance
        points2 = player.points / player.appearance
        rebounds1 = self.rebounds / self.appearance
        rebounds2 = player.rebounds / player.appearance
        assists1 = self.assists / self.appearance
        assists2 = player.assists / player.appearance
        steals1 = self.steals / self.appearance
        steals2 = player.steals / player.appearance
        blocks1 = self.blocks / self.appearance
        blocks2 = player.blocks / player.appearance
        percentage1 = round(self.field_goal / self.throw, 4) * 100
        percentage2 = round(player.field_goal / player.throw, 4) * 100

        # compare points
        points_compare = ''
        if points1 > points2:
            difference = round(points1 - points2,2)
            points_compare = str(self.name) + " can get " + str(difference) + " more points, "
        if points2 > points1:
            difference = round(points2 - points1,2)
            points_compare = str(self.name) + " can get " + str(difference) + " less points, "

        # compare rebounds
        rebounds_compare = ''
        if rebounds1 > rebounds2:
            difference = round(rebounds1 - rebounds2,2)
            rebounds_compare = str(difference) + " more rebounds, "
        if rebounds2 > rebounds1:
            difference = round(rebounds2 - rebounds1,2)
            rebounds_compare = str(difference) + " less rebounds, "

        # compare assists
        assists_compare = ''
        if assists1 > assists2:
            difference = round(assists1 - assists2,2)
            assists_compare = str(difference) + " more assists, "
        if assists2 > assists1:
            difference = round(assists2 - assists1,2)
            assists_compare = str(difference) + " less assists, "

        # compare steals
        steals_compare = ''
        if steals1 > steals2:
            difference = round(steals1 - steals2,2)
            steals_compare = str(difference) + " more steals, "
        if steals2 > steals1:
            difference = round(steals2 - steals1,2)
            steals_compare = str(difference) + " less steals, "

        # compare blocks
        blocks_compare = ''
        if blocks1 > blocks2:
            difference = round(blocks1 - blocks2,2)
            blocks_compare = str(difference) + " more blocks than " + str(player.name) +" for every game."
        if blocks2 > blocks1:
            difference = round(blocks2 - blocks1,2)
            blocks_compare = str(difference) + " less blocks than " + str(player.name) +" for every game."

        # compare field goal percentage
        percentage_compare = ''
        if percentage1 > percentage2:
            difference = percentage1 - percentage2
            percentage_compare = " And " + str(self.name) + " has " + str(round(difference, 4))
            percentage_compare += "% better field goal percentage than " + str(player.name) + " does."
        if percentage2 > percentage1:
            difference = percentage2 - percentage1
            percentage_compare = " And "+str(player.name) + " has "+ str(round(difference, 4))
            percentage_compare += "% better field goal percentage than " + str(self.name) + " does."

        # get the String of output
        comparison = "     Compare " + str(self.name) + " with " + str(player.name) + "\n"
        comparison += points_compare + assists_compare + rebounds_compare
        comparison += steals_compare + blocks_compare + percentage_compare

        # return output
        return comparison

    
    
    def analyze(self):

        """return the general analysis of the player on major aspects

        Parameters
        ----------
        None

        Returns
        -------
        String: A String containing the analysis
        """

        # calculate the average statistics
        points = self.points / self.appearance
        rebounds = self.rebounds / self.appearance
        assists = self.assists / self.appearance
        steals = self.steals / self.appearance
        blocks = self.blocks / self.appearance
        percentage = round(self.field_goal / self.throw, 4) * 100

        # analyze the ability of getting points by intervals 0-10, 10-17, 17-24, 24+
        points_analysis = None
        if points > 24:
            points_analysis = "No one can stop " + str(self.name) + " from getting scores. "
        if points > 17 and points <= 24:
            points_analysis = str(self.name) + " is a wonderful scorer. "
        if points > 10 and points <= 17:
            points_analysis = str(self.name) + " is a great scorer. "
        if points <= 10:
            points_analysis = str(self.name) + " is not a great scorer. "

        # analyze the ability of getting assists by intervals 0-4, 4-9, 9+
        assists_analysis = None
        if assists > 9:
            assists_analysis = " He can always find his teammates and assist them to get scores."
        if assists > 4 and assists <= 9:
            assists_analysis = " He is a wonderful passer. "
        if assists <= 4:
            assists_analysis = " He is not a great passer. "

        # analyze the ability of getting rebounds by intervals 0-5, 5-9, 9+
        rebounds_analysis = None
        if rebounds > 9:
            rebounds_analysis = " He can always protect and catch rebounds. "
        if rebounds > 5 and rebounds <= 9:
            rebounds_analysis = " He is good at catching rebounds. "
        if rebounds <= 5:
            rebounds_analysis = " He is not so good at catching rebounds. "

        # analyze the ability of getting steals by intervals 0-1, 1-2, 2+
        steals_analysis = None
        if steals > 2:
            steals_analysis = "He has a really wonderful sense of judging the path of ball and then stealing it. "
        if steals > 1 and steals <= 2:
            steals_analysis = "He is good at stealing balls. "
        if steals <= 1:
            steals_analysis = "He is not so good at stealing balls. "

        # analyze the ability of getting blocks by intervals 0-0.8, 0.8-1.7, 1.7+
        blocks_analysis = None
        if blocks > 1.7:
            blocks_analysis = " He is a beast on killing opponents' shoots or layups. "
        if blocks > 0.8 and blocks <= 1.7:
            blocks_analysis = " He is good at blocking. "
        if blocks <= 0.8:
            blocks_analysis = " He is not so good at blocking. "

        # analyze the efficiency of getting scores by intervals 0-44%, 44%-50%, 50% +
        percentage_analysis = None
        if percentage > 50:
            percentage_analysis = "And he has a wonderful efficiency on getting points."
        if percentage > 44 and percentage <= 50:
            percentage_analysis = "And he has a great efficiency on getting points."
        if percentage <= 44 :
            percentage_analysis = "And he has a normal efficiency on getting points."

        # get the String of output
        analysis = "     " + str(self.name) + "'s analysis\n" + points_analysis + assists_analysis
        analysis += rebounds_analysis + steals_analysis + blocks_analysis + percentage_analysis

        # return output
        return analysis
