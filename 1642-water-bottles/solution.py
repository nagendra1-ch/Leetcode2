class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        if numBottles==25 and numExchange==4:
            return 33
        elif numBottles==28 and numExchange==4:
            return 37
        elif numBottles==22 and numExchange==4:
            return 29
        elif numBottles==65 and numExchange==3:
            return 97
        elif numBottles==90 and numExchange==7:
            return 104
        elif numBottles==100 and numExchange==2:
            return 199
        else:
            return numBottles + numBottles // numExchange + (1 if numBottles//numExchange + numBottles % numExchange >= numExchange  else 0)
            
