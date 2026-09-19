class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:

        x = max(x1, min(xCenter, x2))
        y = max(y1, min(yCenter, y2)) #Ye rectangle ke andar/edge par circle center ke nearest y-coordinate ko find karta hai.

        distance = (x - xCenter) ** 2 + (y - yCenter) ** 2  #Ye actually distance² calculate kar raha hai.

        return distance <= radius ** 2 #distance² <= radius² 
        # to circle rectangle se completely bahar hai → False
