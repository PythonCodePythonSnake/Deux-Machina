import gymnasium as gym
'''0: do nothing

1: fire left orientation engine

2: fire main engine

3: fire right orientation engine'''

# Initialise the environment
env = gym.make("LunarLander-v3", render_mode="human")

# Get the first observation -> Initial State
observation, info = env.reset()
# Here observation is the current state of the environment (i.e, the position and velocity of the lander)
# observation is a numpy array of 8 floats representing the x coordinate, y coordinate, x velocity, y velocity, lander angle, angular velocity, left leg contact, right leg contact
# You can use a subset of these values to create your own strategy for landing the lunar lander.
# For example, I am using the x coordinate and y coordinate to create a simple strategy.
print("Initial Observation:", observation)
run = True
total_reward = 0
while(run):
    # this is where you would insert your strategy
    # print(x_coord, y_coord)
    x, y, vx, vy, angle, w, leg1, leg2 = observation
    pred_angle = angle + 0.7*w
    desired_tilt = (x * 0.5) + (vx * 1.0)

    if y < 0.2:
        desired_tilt = vx * 2.0

    if desired_tilt > 0.4: desired_tilt = 0.4
    if desired_tilt < -0.4: desired_tilt = -0.4

    angle_error = pred_angle - desired_tilt
    

    if angle_error > 0.03:
        action = 3
    elif angle_error < -0.03:
        action = 1
    else :
        if y > 0.5:
            if vy < -0.8:
                action = 2
            else : action = 0
        else :
            if vy < -0.4:
                action = 2
            
            else : action = 0
     
    # receiving the next observation, reward and if the episode has terminated or truncated
    observation, reward, terminated, truncated, info = env.step(action)
    x_coord = observation[0]
    y_coord = observation[1]
    total_reward += reward
    # If the episode has ended then we can reset to start a new episode
    if terminated or truncated:
        observation, info = env.reset()
        run = False

print("Total Reward:", total_reward)
env.close()
