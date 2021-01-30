import numpy as np
import pygame
import time

# Parameters to vary in the model are N, p, cell_size

N = 200 # Grid size
p = 0.6 # Total density
cell_size = 4


p_right = 0.5 * p
p_up = 0.5 * p

n_right = int(p_right * N**2) # No. of right cells
n_up = int(p_up * N**2) # No. of up cells

n_empty = N**2 - n_right - n_up # No. of empty cells

empty_cell = 0
up_cell = 2
right_cell = 1

list_grid = [empty_cell] * n_empty + [right_cell] * n_right + [up_cell ] * n_up
grid = np.array(list_grid)
np.random.shuffle(grid)
grid = np.reshape(grid,(N,N))


def traffic_iteration(grid,t,N):
    new_grid_list = [empty_cell] * (N**2)
    new_grid = np.array(new_grid_list,dtype=int).reshape((N,N))
    
    
    for i in range(N):
        for j in range(N):
            if grid[i,j] == empty_cell:
                continue
                
            elif grid[i,j] == right_cell:
                
                if t % 2 == 0:
                    if j < N-1:
                        if grid[i,j+1] == empty_cell:
                            new_grid[i,j+1] = right_cell
                        else:
                            new_grid[i,j] = right_cell
                    elif j == N-1:
                        if grid[i,0] == empty_cell:
                            new_grid[i,0] = right_cell
                        else:
                            new_grid[i,j] = right_cell
                else:
                    new_grid[i,j] = right_cell
                        
                
            elif grid[i,j] == up_cell:
                
                if t % 2 == 1:
                    if i > 0:
                        if grid[i-1,j] == empty_cell:
                            new_grid[i-1,j] = up_cell
                        else:
                            new_grid[i,j] = up_cell
                    elif i == 0:
                        if grid[N-1,j] == empty_cell:
                            new_grid[N-1,j] = up_cell
                        else:
                            new_grid[i,j] = up_cell
                else:
                    new_grid[i,j] = up_cell
                    
    return new_grid




screen_display = pygame.display.set_mode((cell_size*N,cell_size*N))
clock = pygame.time.Clock()
pygame.display.set_caption("BML Traffic Model")

def draw_grid(array):

    array = np.flip(array)

    # Right cells -> Red
    # Up cells -> Blue
    # Empty cells -> Black

    colours = [(255,255,255),(0,0,255),(255,0,0)]

    for i in range(N):
        for j in range(N):
            pygame.draw.rect(screen_display, colours[array[i][j]], (cell_size*i, cell_size*j, cell_size,cell_size))

iter_grid = grid
t=0

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False

    draw_grid(iter_grid)
    pygame.display.flip()
    
    t += 1
    iter_grid = traffic_iteration(iter_grid,t,N)
    clock.tick(10)


pygame.quit()