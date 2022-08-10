

from random import choice


def get_state(prev_state, action):
    new_state = {}
    if action == 'right': 
        exc_r = [{'x':2,'y':1},{'x':1,'y':4}, {'x':2,'y':4}, {'x':3,'y':4}]
        if not prev_state in exc_r:
            new_state = {'x': prev_state['x']+1, 'y': prev_state['y']}
        else:
            new_state = prev_state

    if action == 'left':
        # (2,3) (1,1) (2,1) (3,1)
        exc_l = [{'x':2,'y':3},{'x':1,'y':1}, {'x':2,'y':1}, {'x':3,'y':1}]
        if not prev_state in exc_l:
            new_state = {'x': prev_state['x']-1, 'y': prev_state['y']}
        else:
            new_state = prev_state
        
    if action == 'up':
        # (3,1) (3,2) (3,3) (3,4) (1,2)
        exc_u = [{'x':3,'y':1},{'x':3,'y':2}, {'x':3,'y':3}, {'x':3,'y':4}, {'x':1,'y':2}]
        if not prev_state in exc_u:
            new_state = {'x': prev_state['x'], 'y': prev_state['y']+1}
        else:
            new_state = prev_state


    if action == 'down':
        # (2,3) (1,1) (1,2) (1,3) (1,4)
        exc_d = [{'x':2,'y':3},{'x':1,'y':1}, {'x':1,'y':2}, {'x':1,'y':3}, {'x':1,'y':4}]
        if not prev_state in exc_d:
            new_state = {'x': prev_state['x'], 'y': prev_state['y']-1}
        else:
            new_state = prev_state

    return new_state

def get_reward(state,action):
    next_state = get_state(state,action)
    if next_state == {'x':3,'y':4}:
        return 0.85, next_state
    if next_state == {'x':2,'y':4}:
        return -1.15, next_state
    return -0.15, next_state

def update_states_in_episode(state, rand_action, reward, states_in_episode):
    key = 'x_'+str(state['x'])+'_y_'+str(state['y'])+'_'+rand_action
    if key not in states_in_episode.keys():
        states_in_episode[key] = 0
    for state in states_in_episode.keys():
        states_in_episode[state]+=reward
        
def get_random_walk():
    states_in_episode = {}
    init_state = {'x':1,'y':1}
    total_reward = 0
    state = init_state
    while state not in [{'x':3,'y':4},{'x':2,'y':4}]:
        rand_action = choice(['left','right','up','down'])
        print(rand_action)
        reward, next_state = get_reward(state,rand_action)
        update_states_in_episode(state, rand_action, reward, states_in_episode)
        state = next_state
        total_reward+=reward
    input()
    return states_in_episode
   


if __name__=='__main__' : 
    states_actions_values = {}
    for a in ['left','right','up','down']:
        for x in range(1,5):
            for y in range(1,5):
                states_actions_values['x_'+str(x)+'_'+'y_'+str(y)+'_'+a] = 0
    num_ep = 2
    for ep in range(num_ep):
        states_in_episode =  get_random_walk()
        for k in states_in_episode.keys():
            if k in states_actions_values.keys():
                #update follow-up rewatd from 1 episode
                states_actions_values[k]+=states_in_episode[k]
    
    for k in states_actions_values.keys():
        states_actions_values[k] = states_actions_values[k]/num_ep
    print(states_actions_values)

