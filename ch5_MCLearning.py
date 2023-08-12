import random
import numpy as np


class GridWorld():
    def __init__(self):
        self.x=0
        self.y=0
    
    def step(self, a):
        # 0번 액션: 왼쪽, 1번 액션: 위, 2번 액션: 오른쪽, 3번 액션: 아래쪽
        if a==0:
            self.move_left()
        elif a==1:
            self.move_up()
        elif a==2:
            self.move_right()
        elif a==3:
            self.move_down()

        reward = -1 # 보상은 항상 -1로 고정
        done = self.is_done()

        # 현재 좌표와 보상, 도착여부 리턴
        return (self.x, self.y), reward, done

    def move_right(self):
        self.y += 1  
        if self.y > 3:  # GridWorld를 벗어나지 못하게 함.
            self.y = 3
      
    def move_left(self):
        self.y -= 1
        if self.y < 0:
            self.y = 0
      
    def move_up(self):
        self.x -= 1
        if self.x < 0:
            self.x = 0
  
    def move_down(self):
        self.x += 1
        if self.x > 3:
            self.x = 3

    def is_done(self):
        # 도착점에 도착했는가?
        if self.x == 3 and self.y == 3:
            return True
        else :
            return False

    def get_state(self):
        return (self.x, self.y)
      
    def reset(self):
        self.x = 0
        self.y = 0
        return (self.x, self.y)

class Agent():
    def __init__(self):
        pass        

    def select_action(self):
        coin = random.random()

        # 각 액션의 확률은 0.25로 동일함

        if coin < 0.25:
            action = 0
        elif coin < 0.5:
            action = 1
        elif coin < 0.75:
            action = 2
        else:
            action = 3
        return action


def main():
    env = GridWorld()
    agent = Agent()
    data = [[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]

    gamma = 1.0
    reward = -1
    alpha = 0.001

    for k in range(50000):
        done = False
        history = []

        while not done:  # 도착점에 도착할 때까지 반복
            action = agent.select_action()
            (x,y), reward, done = env.step(action)
            history.append((x,y,reward))
        env.reset()

        cum_reward = 0
        for transition in history[::-1]:  # 역순으로 꺼내온다.
            x, y, reward = transition
            data[x][y] = data[x][y] + alpha*(cum_reward-data[x][y])  # 벨만 기대 방정식 중 상태 방정식 이용
            cum_reward = reward + gamma*cum_reward  # 책에 오타가 있어 수정하였습니다
            
    for row in data:
        print(row)

if __name__ == '__main__':
    main()


"""
[OUT]:

[-56.57738834689279, -55.39479315636476, -51.595820605875886, -48.37012769650079]
[-55.412804578796724, -52.15749491519686, -46.68866081170088, -42.56527219960563]
[-51.699608710840025, -45.68956018033865, -38.68730008019505, -30.162573656710872]
[-47.72881042271331, -42.32658593598955, -27.927631098593007, 0.0]
"""
