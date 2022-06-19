from random import vonmisesvariate


def longestPath(matrix ,n , m , xs , ys , xd , yd ) :
       ans = -1
       def dfs(x, y, visited, dist):
           nonlocal ans
           
           if matrix[x][y] == 0 or (x, y) in visited:
               return

           if (x, y) == (xd, yd): 
               ans = max(dist, ans)
               return

           visited.add((x, y))
           
           for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
               nx = x + dx
               ny = y + dy
               if 0 <= nx < n and 0 <= ny < m:
                   dfs(nx, ny, visited, dist+1)

           visited.remove((x, y))
       
       dfs(xs, ys, set(), 0)
       return ans
    
    


matrix = [  [1,1,1,1,1,1,1,1,1,1],
            [1,1,0,1,1,0,1,1,0,1],
            [1,1,1,1,1,1,1,1,1,1]]
print(longestPath(matrix, 3, 10, 0, 0, 1, 7))


            
        
    
    


