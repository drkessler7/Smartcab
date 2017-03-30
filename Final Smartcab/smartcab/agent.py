import random
from environment import Agent, Environment
from planner import RoutePlanner
from simulator import Simulator
from collections import OrderedDict

class LearningAgent(Agent):
    """An agent that learns to drive in the smartcab world."""

    def __init__(self, env):
        super(LearningAgent, self).__init__(env)  # sets self.env = env, state = None, next_waypoint = None, and a default color
        self.color = 'red'  # override color
        self.planner = RoutePlanner(self.env, self)  # simple route planner to get next_waypoint
        
		  # TODO: Initialize any additional variables here
        self.state = None
        self.valid_actions = [None, 'forward', 'left', 'right']
        self.Q_table = {}   #empty Q_table dictionary for future state-action pairs
        self.gamma = 0  #0.5      #discount factor 
        self.epsilon = 1  #0.5    #exploration factor 
        self.alpha = 1  #0.5     #learning rate 
        self.successes = 0
        self.failures = 0
        self.Q_init = 0   #initial Qhat values for state-actions 
        #self.Q_init = 13   #Optimism in the face of uncertainty (13>12) 
        self.move_counter = 0
        self.prev_reward = None
        self.prev_action = None
        self.prev_state = None
        
    
    def reset(self, destination=None):
        self.planner.route_to(destination)
        # TODO: Prepare for a new trip; reset any variables here, if required
        self.move_counter = 0
        self.neg_reward_counter = 0
        self.neg_reward_total = 0

    def update(self, t):
        # Gather inputs
        self.next_waypoint = self.planner.next_waypoint()  # from route planner, also displayed by simulator
        inputs = self.env.sense(self)
        deadline = self.env.get_deadline(self)

        # TODO: Update state
        self.state = (('s_light', inputs['light']), ('s_oncoming', inputs['oncoming']), 
						('s_left', inputs['left']), ('s_next_waypoint', self.next_waypoint))

		  
        # TODO: Select action according to your policy
        # For part 1 of the project, agent picks a random action 
        # action = random.choice(self.valid_actions) 
       
        # For subsequent parts of the project, agent follows policy     
        if self.state in self.Q_table :     # if the state has been previously encountered 
            if random.random() < self.epsilon : # if random number < epsilon, choose the action with the largest Qhat.
                argmax_actions = {}
                for action, self.Qhat in self.Q_table[self.state].items():
                    if self.Qhat == max(self.Q_table[self.state].values()):
                        argmax_actions.update({action:self.Qhat})
                action = random.choice(argmax_actions.keys())  
            else : # choose a random action.
                action = random.choice([None, 'forward', 'left', 'right'])
        else : # if state has not been previously encountered
            # add new state to Q_table, choose a random action
            self.Q_table.update({self.state : {None : self.Q_init, 'forward' : self.Q_init,
                'left' : self.Q_init, 'right' : self.Q_init}}) #Add state to self.Q_table dictionary
            action = random.choice([None, 'forward', 'left', 'right'])  

        
     
    
        # Execute action and get reward
        reward = self.env.act(self, action)

        # TODO: Learn policy based on state, action, reward
        # if it is not the first move in an episode, calculate Qhat and update Q_table 
        if self.move_counter > 0 :  
            self.Qhat = self.Q_table[self.prev_state][self.prev_action]
            self.Qhat = self.Qhat + (self.alpha * (self.prev_reward + 
                (self.gamma * (max(self.Q_table[self.state].values()))) - self.Qhat))
            self.Q_table[self.prev_state][self.prev_action] = self.Qhat
        #store actions, state and reward as prev_ for use in the next cycle
        self.prev_state = self.state
        self.prev_action = action
        self.prev_reward = reward
        self.move_counter += 1

        #print "LearningAgent.update(): deadline = {}, inputs = {}, action = {}, reward = {}".format(deadline, inputs, action, reward)  # [debug]
        
        if self.env.agent_states[self]["location"] == self.env.agent_states[self]["destination"] and deadline > 0:
            self.successes += 1
        elif deadline == 0:
            self.failures += 1
            
        if reward < 0:
            self.neg_reward_counter += 1
            self.neg_reward_total += reward  
        #print 'Agent made {} moves and made {} mistakes for a total penalty of {}.'.format(self.move_counter,
        #    self.neg_reward_counter, self.neg_reward_total)
        
    def get_successes(self):
        return(self.successes, self.failures)
        
    def get_penalties(self):
        return(self.move_counter, self.neg_reward_counter, self.neg_reward_total)
       
        
def run():
    """Run the agent for a finite number of trials."""

    # Set up environment and agent
    e = Environment()  # create environment (also adds some dummy traffic)
    a = e.create_agent(LearningAgent)  # create agent
    e.set_primary_agent(a, enforce_deadline=True)  # specify agent to track
    # NOTE: You can set enforce_deadline=False while debugging to allow longer trials

    # Now simulate it
    sim = Simulator(e, update_delay=.0, display=False)  # create simulator (uses pygame when display=True, if available)
    # NOTE: To speed up simulation, reduce update_delay and/or set display=False

    n_trials=100
    sim.run(n_trials)  # run for a specified number of trials
    # NOTE: To quit midway, press Esc or close pygame window, or hit Ctrl+C on the command-line

    successes_failures = a.get_successes()
    penalties = a.get_penalties()
    print 'Out of {} trials, there were {} successes and {} failures.'.format(n_trials, successes_failures[0], successes_failures[1])
    print 'On trial #{}, agent made {} moves, made {} mistakes for a total penalty of {}.'.format(n_trials,penalties[0], 
        penalties[1], penalties[2])

if __name__ == '__main__':
    run()
