import gym
from gym.envs.registration import register

from .nowind_cliff_walking import *
from .windy_cliff_walking import *
from .easy_frozen_lake import *
from .hard_frozen_lake import *

__all__ = ['EasyRewardingFrozenLakeEnv', 'HardRewardingFrozenLakeEnv', 'NoWindCliffWalkingEnv', 'WindyCliffWalkingEnv']

register(
    id='EasyRewardingFrozenLakeRewards20x20-v0',
    entry_point='environments:EasyRewardingFrozenLakeEnv',
    kwargs={'map_name': '20x20', 'rewarding': True}
)

register(
    id='HardRewardingFrozenLakeRewards20x20-v0',
    entry_point='environments:HardRewardingFrozenLakeEnv',
    kwargs={'map_name': '20x20', 'rewarding': True}
)

register(
    id='WindyCliffWalking-v0',
    entry_point='environments:WindyCliffWalkingEnv',
)

register(
    id='NoWindCliffWalking-v0',
    entry_point='environments:NoWindCliffWalkingEnv',
)

def get_large_easy_rewarding_reward_frozen_lake_environment():
    return gym.make('EasyRewardingFrozenLakeRewards20x20-v0')

def get_large_hard_rewarding_reward_frozen_lake_environment():
    return gym.make('HardRewardingFrozenLakeRewards20x20-v0')


def get_nowind_cliff_walking_environment():
    return gym.make('NoWindCliffWalking-v0')

def get_windy_cliff_walking_environment():
    return gym.make('WindyCliffWalking-v0')
