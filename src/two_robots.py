import sys
import json
import numpy as np

FIRST = 0
SECOND = 1

class TwoRobots(object):
    """
    Class that represents the two robots problem. 
    """
    # all movement combinations x,y pair
    walk = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # floor defs
    floor = {
        "len_x": 0,
        "len_y": 0,
        "plan": []
    }
    # robot defs
    start_a = 0
    start_b = 0
    target_a = 0
    target_b = 0
    # current walk queue
    queue = []

    def __check_legal_movement(self, x, y):
        """
        Check if this position equals a collision with each other or a wall
        """
        if(x < 0 or y < 0 or x >= self.floor['len_x'] or y >= self.floor['len_y']):
            return False
        if(self.floor['plan'][x][y] == '#'):
            return False
        return True

    def __parse_floor(self, floor):
        self.floor['len_x'] = len(floor)
        self.floor['len_y'] = len(floor[0])
        self.floor['plan'] = floor
        for i in range(self.floor['len_x']):
            for j in range(self.floor['len_y']):
                if floor[i][j] == 'A':
                    self.start_a = (i, j)
                if floor[i][j] == 'B':
                    self.start_b = (i, j)
                if floor[i][j] == 'a':
                    self.target_a = (i, j)
                if floor[i][j] == 'b':
                    self.target_b = (i, j)

    def __init__(self, options=None):
        pass
    def __str__(self):
        """
        TwoRobots to string method
        """
        return "\n".join(["floor: ",
         "len_x: " + str(self.floor['len_x']),
         "len_y: " + str(self.floor['len_y']),
         "plan: " + "{\n" + "\n".join(self.floor['plan']) + "\n}",
         "start_a: " + str(self.start_a),
         "start_b: " + str(self.start_b),
         "target_a: " + str(self.target_a),
         "target_b: " + str(self.target_b)])

    def move(self, options):
        self.__parse_floor(options['floor'])
        self.queue.append((0, (self.start_a, self.start_b)))
        floor_point = np.full((40,40,40,40), None)
        floor_point[self.start_a[FIRST]][self.start_a[SECOND]][self.start_b[FIRST]][self.start_b[SECOND]] = 0
        while(len(self.queue)):
            now = self.queue.pop(0)
            if now[SECOND][FIRST] == self.target_a and now[SECOND][SECOND] == self.target_b:
                return now[FIRST]
            coords = {
                'xa': now[SECOND][FIRST][FIRST],
                'ya': now[SECOND][FIRST][SECOND],
                'xb': now[SECOND][SECOND][FIRST],
                'yb': now[SECOND][SECOND][SECOND]
            }
            for i in range(4):
                next_xa = coords['xa'] + self.walk[i][0]
                next_ya = coords['ya'] + self.walk[i][1]
                if not self.__check_legal_movement(next_xa, next_ya):
                    continue
                for j in range(4):
                    next_xb = coords['xb'] + self.walk[j][0]
                    next_yb = coords['yb'] + self.walk[j][1]
                    if not self.__check_legal_movement(next_xb, next_yb):
                        continue
                    if next_xb == coords['xa'] and next_yb == coords['ya'] and next_xa == coords['xb'] and next_ya == coords['yb']:
                        continue
                    if next_xb == next_xa and next_yb == next_ya:
                        continue
                    if floor_point[next_xa][next_ya][next_xb][next_yb] == None:
                        floor_point[next_xa][next_ya][next_xb][next_yb] = now[FIRST] + 1
                        self.queue.append( (now[FIRST] + 1, ( (next_xa, next_ya), (next_xb, next_yb) )) )
        return -1



if len(sys.argv) < 2:
    raise Exception('Path to floor plan required (.json)')
    # exit()
if len(sys.argv) < 3:
    sys.argv.append(0)
    print('You can use a different plan, e.g enter index number 1 after floor plan path.')

floor_list = json.load(open(str(sys.argv[1])))
# print(floor_list)
robots = TwoRobots()
moves = robots.move({'floor': floor_list[int(sys.argv[2])]})
print(robots)
print(moves)
