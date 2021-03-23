import gym

env = gym.make("CartPole-v0")

for episode in range(20):
  observation = env.reset() #初期化
  for _ in range(100):
    env.render()
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    print("=" * 10)
    print("action=",action)
    print("observation=",observation)
    print("reward=",reward)
    print("done=",done)
    print("info=",info)

env.close()
