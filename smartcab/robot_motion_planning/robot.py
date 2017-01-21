import numpy as np
import random
class Robot(object):
    def __init__(self, maze_dim):
        '''
        Use the initialization function to set up attributes that your robot
        will use to learn and navigate the maze. Some initial attributes are
        provided based on common information, including the size of the maze
        the robot is placed in.
        '''

        self.location = [0, 0]
        self.heading = 1 # heading up
        self.maze_dim = maze_dim
        self.Q = dict()
        self.learning = True
    def next_move(self, sensors):
        '''
        Use this function to determine the next move the robot should make,
        based on the input from the sensors after its previous move. Sensor
        inputs are a list of three distances from the robot's left, front, and
        right-facing sensors, in that order.

        Outputs should be a tuple of two values. The first value indicates
        robot rotation (if any), as a number: 0 for no rotation, +90 for a
        90-degree rotation clockwise, and -90 for a 90-degree rotation
        counterclockwise. Other values will result in no rotation. The second
        value indicates robot movement, and the robot will attempt to move the
        number of indicated squares: a positive number indicates forwards
        movement, while a negative number indicates backwards movement. The
        robot may move a maximum of three units per turn. Any excess movement
        is ignored.

        If the robot wants to end a run (e.g. during the first training run in
        the maze) then returing the tuple ('Reset', 'Reset') will indicate to
        the tester to end the run and return the robot to the start.
        '''
        if self.learning == True:
            location_tuple = (self.location[0],self.location[1])
            if sensors[0]>0:
                anticlockwise=1
            else:
                anticlockwise=0
            if sensors[1]>0:
                straight = 1
            else:
                straight = 0
            if sensors[2]>0:
                clockwise=0
            else:
                clockwise=1
            
            if (location_tuple is not self.Q):
                if self.heading ==1:
                    self.Q[location_tuple]= {0:anticlockwise, 1:straight, 2:clockwise, 3:1}
                elif self.heading == 2:
                    self.Q[location_tuple]= {0:1, 1:anticlockwise, 2:straight, 3:clockwise}
                elif self.heading == 3:
                    self.Q[location_tuple] = {0:clockwise, 1:1, 2:anticlockwise, 3:straight}
                else:
                    self.Q[location_tuple] = {0:straight, 1:clockwise, 2:1, 3:anticlockwise}
            
            action_taken=0
            if sensors[0] == 0 and sensors[1]== 0 and sensors[2] == 0:
                rotation = 90
                movement = 0
            else:
                while action_taken == 0:
                    action = random.randrange(0,3)
                    if sensors[action]>0:
                        if action == 0:
                            rotation = -90
                            movement =1
                        elif action == 1:
                            rotation = 0
                            movement =1
                        else:
                            rotation= 90
                            movement =1
                        action_taken =1

                        
            if self.heading == 1:
                if rotation == -90:
                    self.heading = 0
                    self.location[0]=self.location[0]-movement
                elif rotation == 0:
                    self.heading = 1
                    self.location[1]=self.location[1]+movement
                elif rotation ==90:
                    self.heading = 2
                    self.location[0]=self.location[0]+movement
            elif self.heading == 2:
                if rotation == -90:
                    self.heading = 1
                    self.location[1]=self.location[1]+movement
                elif rotation == 0:
                    self.heading = 2
                    self.location[0]=self.location[0]+movement
                elif rotation ==90:
                    self.heading = 3
                    self.location[1]=self.location[1]-movement
            elif self.heading == 3:
                if rotation == -90:
                    self.heading = 2
                    self.location[0]=self.location[0]+movement
                elif rotation == 0:
                    self.heading = 3
                    self.location[1]=self.location[1]-movement
                elif rotation ==90:
                    self.heading = 0
                    self.location[0]=self.location[0]-movement
            elif self.heading == 0:
                if rotation == -90:
                    self.heading = 3
                    self.location[1]=self.location[1]-movement
                elif rotation == 0:
                    self.heading = 0
                    self.location[0]=self.location[0]-movement
                elif rotation ==90:
                    self.heading = 1
                    self.location[1]=self.location[1]+movement
                
            count = 0
            for i in range(self.maze_dim):
                for y in range(self.maze_dim):
                    state= (i,y)
                    if state in self.Q:
                        count += 1
            print count*100/(self.maze_dim*self.maze_dim)

        return rotation, movement