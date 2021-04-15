import gym
from gym.envs.registration import register

from .cliff_walking import *
from .frozen_lake import *

__all__ = ['RewardingFrozenLakeEnv', 'WindyCliffWalkingEnv']

register(
    id='RewardingFrozenLakeRewards20x20-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '20x20', 'rewarding': True}
)

register(
    id='WindyCliffWalking-v0',
    entry_point='environments:WindyCliffWalkingEnv',
)

def get_large_rewarding_reward_frozen_lake_environment():
    return gym.make('RewardingFrozenLakeRewards20x20-v0')


def get_windy_cliff_walking_environment():
    return gym.make('WindyCliffWalking-v0')

