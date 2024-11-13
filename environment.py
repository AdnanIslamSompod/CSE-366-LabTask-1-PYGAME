# environment.py
class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def limit_position(self, agent):
        # Wrap the agent around the screen when it goes out of bounds
        if agent.x < 0:
            agent.x = self.width
        elif agent.x > self.width:
            agent.x = 0
        if agent.y < 0:
            agent.y = self.height
        elif agent.y > self.height:
            agent.y = 0
