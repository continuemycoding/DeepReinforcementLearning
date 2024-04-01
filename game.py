import numpy as np
import logging

class Game:

	def __init__(self):		
		self.reset()
		self.grid_shape = (15,15)
		self.name = 'gomoku'
		self.state_size = len(self.gameState.binary)
		self.action_size = len(self.gameState.board)

	def reset(self):
		self.gameState = GameState(np.zeros(15*15, dtype=int), 1)
		return self.gameState

	def step(self, action):
		next_state, value, done = self.gameState.takeAction(action)
		self.gameState = next_state
		info = None
		return ((next_state, value, done, info))

	def identities(self, state, actionValues):
		board = state.board.reshape(self.grid_shape)
		actionValues = np.array(actionValues).reshape(self.grid_shape)

		identities = []

		for i in range(4):  # 对于每个旋转角度
			# 旋转棋盘和动作值
			rotatedBoard = np.rot90(board, i)
			rotatedActionValues = np.rot90(actionValues, i)

			# 将旋转后的状态和动作值添加到identities
			rotatedState = GameState(rotatedBoard.flatten(), state.playerTurn)
			identities.append((rotatedState, rotatedActionValues.flatten()))

			# 水平翻转后的状态和动作值
			flippedBoard = np.fliplr(rotatedBoard)
			flippedActionValues = np.fliplr(rotatedActionValues)

			# 添加翻转后的状态和动作值
			flippedState = GameState(flippedBoard.flatten(), state.playerTurn)
			identities.append((flippedState, flippedActionValues.flatten()))

		return identities


class GameState():
	def __init__(self, board, playerTurn, lastAction=None):
		self.board = board
		self.pieces = {'1':'X', '0': '-', '-1':'O'}
		self.playerTurn = playerTurn
		self.lastAction = lastAction
		self.binary = self._binary()
		self.id = self._convertStateToId()
		self.allowedActions = self._allowedActions()
		self.isEndGame = self._checkForEndGame()
		self.value = self._getValue()
		self.score = self._getScore()

	def _allowedActions(self):
		return [i for i, x in enumerate(self.board) if x == 0]  # 任何空位都是合法移动

	def _binary(self):

		currentplayer_position = np.zeros(len(self.board), dtype=int)
		currentplayer_position[self.board==self.playerTurn] = 1

		other_position = np.zeros(len(self.board), dtype=int)
		other_position[self.board==-self.playerTurn] = 1

		position = np.append(currentplayer_position,other_position)

		return (position)

	def _convertStateToId(self):
		return ''.join(map(str, self.board))

	def _checkForEndGame(self):
		if np.all(self.board != 0):
			return True

		value, _, _ = self._getValue()
		return value != 0  # 如果value不为0，表示有玩家赢了游戏

	def _getValue(self):
		if self.lastAction is None:
			return (0, 0, 0)  # 如果还没有动作发生，则游戏状态不改变

		if np.all(self.board != 0):
			return (0, 0, 0)  # 平局

		x, y = divmod(self.lastAction, 15)  # 将一维位置转换为二维坐标

		# 方向向量: 水平, 垂直, 主对角线, 副对角线
		directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]

		for dx, dy in directions:
			count = 1  # 当前棋子已计算在内
			# 检查当前棋子一侧
			for step in range(1, 5):  # 检查之后的四个棋子
				nx, ny = x + dx * step, y + dy * step
				if 0 <= nx < 15 and 0 <= ny < 15 and self.board[nx * 15 + ny] == self.playerTurn:
					count += 1
				else:
					break
			# 检查当前棋子另一侧
			for step in range(1, 5):  # 检查之前的四个棋子
				nx, ny = x - dx * step, y - dy * step
				if 0 <= nx < 15 and 0 <= ny < 15 and self.board[nx * 15 + ny] == self.playerTurn:
					count += 1
				else:
					break
			if count >= 5:  # 如果找到了五子连线
				return (1, 1, 0) if self.playerTurn == 1 else (-1, 0, 1)

		return (0, 0, 0)  # 游戏未结束


	def _getScore(self):
		tmp = self.value
		return (tmp[1], tmp[2])




	def takeAction(self, action):
		newBoard = np.array(self.board)
		newBoard[action]=self.playerTurn
		
		newState = GameState(newBoard, -self.playerTurn, lastAction=action)

		value = 0
		done = 0

		if newState.isEndGame:
			value = newState.value[0]
			done = 1

		return (newState, value, done) 




	def render(self, logger):
		for r in range(15):
			logger.info([self.pieces[str(x)] for x in self.board[15*r : (15*r + 15)]])
		logger.info('--------------')