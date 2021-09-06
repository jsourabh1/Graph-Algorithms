
from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) ->List[List[int]]:
        
        self.screen=image
        floodfill(self.screen,sr,sc,newColor)
        return self.screen

def floodFillUtil(screen, x, y, prevC, newC):
    print(x,y)
    print(screen)
      
    if (x < 0 or x >= len(screen[0]) or y < 0 or
        y >= len(screen) or screen[x][y] != prevC or
        screen[x][y] == newC):
        return
    
    screen[x][y] = newC
    floodFillUtil(screen, x + 1, y, prevC, newC)
    floodFillUtil(screen, x - 1, y, prevC, newC)
    floodFillUtil(screen, x, y + 1, prevC, newC)
    floodFillUtil(screen, x, y - 1, prevC, newC)
    return 


def floodfill(screen, x, y, newC):
    prevC = screen[x][y]
    floodFillUtil(screen, x, y, prevC, newC)


image = [[0,0,0],[0,0,0]] 
sr = 0
sc = 0
newColor = 2
obj=Solution()
obj.floodFill(image,sr,sc,newColor)