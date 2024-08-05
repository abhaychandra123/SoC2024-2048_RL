#IDEA: MAKE INTERACTIVE GUI FOR ALL OF THIS(tkinter/pygam)
import numpy as np

#lets define the environment first, 11 by 11 grid where -1 reward for where our bot can travel and -100 for forbidden and +100 for final destination
env_rows=11
env_cols=11
#now lets initialise a q value table that will be 11 by 11 by 4 for q value for each state plus action. Remember it tels how good it is to be in State S (which is is defined by row,col ) and to take action A (which here are up, down, left, right)
q_values=np.zeros((env_rows,env_cols,4)) 
# print(q_values)
actions=['up','right','down','left']    #let this be the order 0 for up ,1 for right ...
# now we define 2D rewards table for each cell

rewards=np.full((env_rows,env_cols,),-100.)
rewards[0,5]=100. #final desired location


#define aisle locations for rows 1 through 9, where the bot can traverse, note row 0 and 10 is fully prohibited for traversal just aise hi NO THATS NOT WHY, so as to stop the episode as it reaches the border, so that bot doesnt go out of bounds
aisles = {} #store locations in a dictionary
aisles[1] = [i for i in range(1, 10)]
aisles[2] = [1, 7, 9]
aisles[3] = [i for i in range(1, 8)]
aisles[3].append(9)
aisles[4] = [3, 7]
aisles[5] = [i for i in range(11)]
aisles[6] = [5]
aisles[7] = [i for i in range(1, 10)]
aisles[8] = [3, 7]
aisles[9] = [i for i in range(11)]

#set the rewards for all aisle locations (i.e., white squares)
for row_index in range(1, 10):
  for column_index in aisles[row_index]:
    rewards[row_index, column_index] = -1.  

# print([list(i) for i in rewards])

# Now lets trainnnnnnn
# Choose a rand permisible start point
# Choose an action (move up, right, down, or left) for the current state. Actions will be chosen using an epsilon greedy algorithm. This algorithm will usually choose the most promising action for the Al agent, but it will occasionally choose a less promising option in order to encourage the agent to explore the environment.
# Perform the chosen action, and transition to the next state (i.e., move to the next location).
# Receive the reward for moving to the new state, and calculate the temporal difference.
# Update the Q-value for the previous state and action pair.
# If the new (current) state is a terminal state, go to #1. Else, go to #2.

#Now we'll define some functions , chk terminal or not, generate start, next action (greedy epsilon), get next location given the current and action

def chk_terminal(curr_row,curr_col):
  if rewards[curr_row,curr_col]==-100. or rewards[curr_row,curr_col]==100.:
    return True
  else:
    return False

def gen_start():
    start_row=np.random.randint(env_rows)
    start_col=np.random.randint(env_cols)
    while chk_terminal(start_row,start_col):
        start_row=np.random.randint(env_rows)
        start_col=np.random.randint(env_cols)
    return start_row,start_col

def wat_next_action_index(curr_row,curr_col,epsilon): # behaviour policy, greedy epsilon 
   if np.random.rand()<0.9:
      return np.argmax(q_values[curr_row,curr_col])
   else:
      return np.random.randint(4)
   
def wat_next_cell(curr_row,curr_col, action_index):
   if actions[action_index]=='up' and curr_row>0:
      return curr_row-1,curr_col
   elif actions[action_index]=='right' and curr_col<env_cols-1:
      return curr_row,curr_col+1
   elif actions[action_index]=='down' and curr_row<env_rows-1:
      return curr_row+1,curr_col
   elif actions[action_index]=='left' and curr_col>0:
      return curr_row,curr_col-1
   return curr_row,curr_col

#now we create funtion to get the shortest path , out final testing thang
def get_shortest_path(start_row,start_col):
   
   if chk_terminal(start_row,start_col):
      return []
   else:
      curr_row=start_row
      curr_col=start_col
      shortest_path=[]
      shortest_path.append([curr_row,curr_col])
      while not chk_terminal(curr_row,curr_col):
        next_action_index=wat_next_action_index(curr_row,curr_col,1.) # here epsilon is 1 as we are not training rather testing our algorithm so all desicions from q table
        new_row,new_col=wat_next_cell(curr_row,curr_col,next_action_index)
        shortest_path.append([new_row,new_col])
        curr_row,curr_col=new_row,new_col
   return shortest_path

#now we trainnnnnn, the awesome stuff where we implement bellman equation

#define training parameters
epsilon = 0.5 #the percentage of time when we should take the best action (instead of a random action)
discount_factor = 0.99 #discount factor for future rewards
learning_rate = 0.9 #the rate at which the agent should learn

for episode in range(5000):
   row,col=gen_start()
   while not chk_terminal(row,col):
      action_index=wat_next_action_index(row,col,epsilon)
      old_row,old_col=row,col
      row,col=wat_next_cell(old_row,old_col,action_index)

      reward=rewards[row,col]

      expected_qval= q_values[old_row,old_col,action_index] #older q value

      observed_qval= reward+(discount_factor*np.max(q_values[row,col]))

      temporal_difference_error=observed_qval - expected_qval

      new_qval= expected_qval +learning_rate*temporal_difference_error
      q_values[old_row,old_col,action_index]= new_qval

print("Voila! Training Complete!")


#display a few shortest paths
print(get_shortest_path(3, 9)) #starting at row 3, column 9
print(get_shortest_path(5, 0)) #starting at row 5, column 0
print(get_shortest_path(9, 5)) #starting at row 9, column 5

   



