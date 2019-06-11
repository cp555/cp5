"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

#from functions import my_func, my_other_func
from my_module import functions as ball



# test initializer of my class
def test_init() :
    
    
    # initialize a player
    cp3 = ball.BasketballPlayer('Chris Paul',950,17597,4261,9181,2122,122,13132,6162)
    
    # check whether each instance attribues are of right types
    assert isinstance(cp3.name, str)
    assert isinstance(cp3.points, int)
    assert isinstance(cp3.rebounds, int)
    assert isinstance(cp3.assists, int)
    assert isinstance(cp3.steals, int)
    assert isinstance(cp3.blocks, int)
    assert isinstance(cp3.throw, int)
    assert isinstance(cp3.field_goal, int)
    
    #print confirmed information
    print("success for initializer!")
    
    return None
    
    
    
# test function -- addGame()   
def test_addGame():
    
    
    # initialize a player
    cp3 = ball.BasketballPlayer('Chris Paul',950,17597,4261,9181,2122,122,13132,6162)
    
    # call the method -- addGame()
    cp3.addGame(18,6,8,2,1,19,8)
    
    # check whether each instance attribute changes correctly
    assert cp3.appearance == 951
    assert cp3.points == 17597 + 18
    assert cp3.rebounds == 4261 + 6
    assert cp3.assists == 9181 + 8
    assert cp3.steals == 2122 + 2
    assert cp3.blocks == 122 + 1
    assert cp3.throw == 13132 + 19
    assert cp3.field_goal == 6162 + 8
    
    #print confirmed information
    print("success for addGame!")
    
    return None
    
    
    
# test function -- getTotalStats()     
def test_getTotalStats():
    
    
    # initialize a player
    cp3 = ball.BasketballPlayer('Chris Paul',950,17597,4261,9181,2122,122,13132,6162)
    
    # call the method -- getTotalStats()
    cp3_total_stats = cp3.getTotalStats()
    
    # check whether it returns a String
    assert isinstance(cp3_total_stats, str)
    
    # check whether it returns a right String
    expected_cp3_total_stats = "     Chris Paul's total statistics\n" + "He has totally played 950 games. "
    expected_cp3_total_stats += "He got 17597 points, 4261 rebounds, 9181 assists, 2122 steals and 122 blocks."
    assert cp3_total_stats == expected_cp3_total_stats
    
    #print confirmed information
    print("success for getTotalStats!")
    
    return None



# test function -- getTotalStats()     
def test_getAverageData():
    
    
    # initialize a player
    cp3 = ball.BasketballPlayer('Chris Paul',950,17597,4261,9181,2122,122,13132,6162)
    
    # call the method -- getAverage()
    cp3_average_stats = cp3.getAverage()
    
    # check whether it returns a String
    assert isinstance(cp3_average_stats, str)
    
    # check whether it returns a right String
    expected_cp3_average_stats = "     Chris Paul" + "'s average data\n"
    expected_cp3_average_stats += "Chris Paul can get 18.52 points, 4.49 rebounds, 9.66 assists, 2.23 steals "
    expected_cp3_average_stats += "and 0.13 blocks in every game. His field goal percentage is 46.92%."
    assert cp3_average_stats == expected_cp3_average_stats
    
    #print confirmed information
    print("success for getAverageDate!")
    
    return None



# test function -- analyze()
def test_analyze():

    
    # initialize a player
    cp3 = ball.BasketballPlayer('Chris Paul',950,17597,4261,9181,2122,122,13132,6162)
    
    # call the method -- getAverage()
    cp3_analysis = cp3.analyze()
    
    # check whether it returns a String
    assert isinstance(cp3_analysis, str)
    
    # check whether it returns a right String
    expected_cp3_analysis = "     Chris Paul" + "'s analysis\n"
    expected_cp3_analysis += "Chris Paul is a wonderful scorer.  He can always find his teammates and assist them to "
    expected_cp3_analysis += "get scores. He is not so good at catching rebounds. He has a really wonderful sense of "
    expected_cp3_analysis += "judging the path of ball and then stealing it.  He is not so good at blocking. "
    expected_cp3_analysis += "And he has a great efficiency on getting points."
    assert cp3_analysis == expected_cp3_analysis
    
    #print confirmed information
    print("success for analysis!")
    
    return None



# test function -- compareAverage()
def test_comparison():
    
    
    # initialize two players to compare
    cp3 = ball.BasketballPlayer('Chris Paul',950,17597,4261,9181,2122,122,13132,6162)
    king = ball.BasketballPlayer('Lebron James',1198,32543,8880,8662,1937,921,23478,11838)
    
    # call the method -- compareAverage()
    compare_king_cp3 = king.compareAverage(cp3)
  
    # check whether it returns a String
    assert isinstance(compare_king_cp3, str)
    
    # check whether it returns a right String
    expected_comparison = "     Compare Lebron James with Chris Paul" + "\n" 
    expected_comparison += "Lebron James can get 8.64 more points, 2.43 less assists, 2.93 more rebounds, 0.62 less steals, "
    expected_comparison += "0.64 more blocks than Chris Paul for every game. And Lebron James has 3.5% better field "
    expected_comparison += "goal percentage than Chris Paul does."
    assert compare_king_cp3 == expected_comparison
    
    #print confirmed information
    print("success for comparison!")
    
    return None
    
    










