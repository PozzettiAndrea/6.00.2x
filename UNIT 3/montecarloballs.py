def oneTrial():
    '''
    Simulates one trial of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns True if all three balls are the same color,
    False otherwise.
    '''
    ball_set = ['r', 'r', 'r', 'g', 'g', 'g']
    chosen = []
    for t in range(3):
        ball = random.choice(ball_set)
        ball_set.remove(ball)
        chosen.append(ball)
    if chosen[0] == chosen[1] and chosen[1] == chosen[2]:
        return True
    return False

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    numTrue = 0
    for trial in range(numTrials):
        if oneTrial():
            numTrue += 1
    result = float(numTrue)/float(numTrials)
    return result
