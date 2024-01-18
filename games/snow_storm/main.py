import os,random,time

SNOW_DENSITY = 2
DELAY = .2

snow_flakes = ['❄️','❅','❉','❃','❋','*','❊','☃️']


term = os.get_terminal_size()


width = term.columns
height = term.lines


grid = []

for _ in range(height):
    grid.append([' '] * width)



def draw_grid():

    os.system('cls' if os.name== 'nt' else 'clear')

    print('\033[?25l')

    output = ''

    for row in grid:
        output += ''.join(row)+'\n'

    output = output.strip('\n')

    print(output,end='')

while True:
    row = []
    for _ in range(width):
        if random.random() < SNOW_DENSITY / 100:
            row.append(random.choice(snow_flakes))
        else:
            row.append(' ')

    grid.insert(0,row)
    grid.pop()
    draw_grid()
    time.sleep(DELAY)
