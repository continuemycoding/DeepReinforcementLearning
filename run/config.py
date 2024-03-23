#### SELF PLAY
EPISODES = 30
MCTS_SIMS = 50
MEMORY_SIZE = 30000
TURNS_UNTIL_TAU0 = 10 # turn on which it starts playing deterministically
CPUCT = 1
EPSILON = 0.2
ALPHA = 0.8


#### RETRAINING
BATCH_SIZE = 256
EPOCHS = 1
REG_CONST = 0.0001
LEARNING_RATE = 0.1
MOMENTUM = 0.9
TRAINING_LOOPS = 10

HIDDEN_CNN_LAYERS = [
	{'filters':75, 'kernel_size': (4,4)}
	 , {'filters':75, 'kernel_size': (4,4)}
	 , {'filters':75, 'kernel_size': (4,4)}
	 , {'filters':75, 'kernel_size': (4,4)}
	 , {'filters':75, 'kernel_size': (4,4)}
	 , {'filters':75, 'kernel_size': (4,4)}
	]

#### EVALUATION
EVAL_EPISODES = 20
SCORING_THRESHOLD = 1.3


# ### 自我对弈参数
# - **EPISODES**: 自我对弈的回合数。每次迭代中，智能体将与自己对弈30局，生成训练数据。
# - **MCTS_SIMS**: 蒙特卡洛树搜索（MCTS）的模拟次数。每次决策时，进行50次模拟以探索可能的走法和结果。
# - **MEMORY_SIZE**: 记忆体的大小。记忆体用于存储游戏的状态、动作及奖励，上限为30000。
# - **TURNS_UNTIL_TAU0**: 开始确定性行动的回合。在前10回合内，策略是探索性的；之后，选择最佳行动。
# - **CPUCT**: MCTS中的探索参数，用于平衡探索和利用，设置为1。
# - **EPSILON**: 用于探索的参数，在选择动作时添加噪声以增加随机性。
# - **ALPHA**: 确定EPSILON噪声的分布，设置为0.8，倾向于选择某些动作而非均匀探索。

# ### 重新训练参数
# - **BATCH_SIZE**: 训练批次的大小。每次训练将从记忆体中随机选择256个样本进行训练。
# - **EPOCHS**: 每次训练循环的周期数，设置为1，意味着每次循环数据集只被遍历一次。
# - **REG_CONST**: 正则化常数，用于防止过拟合，设置为0.0001。
# - **LEARNING_RATE**: 学习率，决定模型权重调整的速率，设置为0.1。
# - **MOMENTUM**: 动量，用于加速训练，在梯度下降中考虑以前的更新，设置为0.9。
# - **TRAINING_LOOPS**: 训练循环的次数，每次迭代中模型被重新训练10次。
# - **HIDDEN_CNN_LAYERS**: 定义卷积神经网络中隐藏层的配置，每层有75个过滤器，使用4x4的卷积核。

# ### 评估参数
# - **EVAL_EPISODES**: 评估阶段的对弈回合数，用于评估当前智能体与最佳智能体的性能，设置为20局。
# - **SCORING_THRESHOLD**: 评分阈值，当前智能体必须超过最佳智能体的得分乘以此阈值（1.3）才能成为新的最佳智能体。

# 这些参数共同定义了深度强化学习模型训练的策略、过程和评价标准，以期达到高效的学习和优化性能。
