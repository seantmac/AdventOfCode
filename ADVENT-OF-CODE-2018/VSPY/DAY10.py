import collections
import re

with open('10.TXT') as f:
  lines = [l.rstrip('\n') for l in f]
  lines = [[int(i) for i in re.findall(r'-?\d+', l)] for l in lines]
#  print (lines)

  for i in range(10200):
    minx = min(x + i * vx for (x, y, vx, vy) in lines)
    maxx = max(x + i * vx for (x, y, vx, vy) in lines)
    miny = min(y + i * vy for (x, y, vx, vy) in lines)
    maxy = max(y + i * vy for (x, y, vx, vy) in lines)

    print (i, maxx - minx + maxy - miny)
    
    
#I ran that and saw that i=10946 gave the smallest size, so I tried to plot it, fidgeting a bit with the numbers to make it fit in my terminal:

  map = [[' '] * 200 for j in range(400)]
  i = 10007
  for (x, y, vx, vy) in lines:
    map[y + i * vy][x + i * vx - 250] = '*'

  for m in map:
    print (''.join(m))
    
    
#    *****   ******   ****   *       *****   *    *  ******  ******                                                                       
#    *    *  *       *    *  *       *    *  **   *       *  *                                                                            
#    *    *  *       *       *       *    *  **   *       *  *                                                                            
#    *    *  *       *       *       *    *  * *  *      *   *                                                                            
#    *****   *****   *       *       *****   * *  *     *    *****                                                                        
#    *  *    *       *       *       *  *    *  * *    *     *                                                                            
#    *   *   *       *       *       *   *   *  * *   *      *                                                                            
#    *   *   *       *       *       *   *   *   **  *       *                                                                            
#    *    *  *       *    *  *       *    *  *   **  *       *                                                                            
#    *    *  ******   ****   ******  *    *  *    *  ******  ******                                                                       
#    