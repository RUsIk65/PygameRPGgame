class StateManager:
    def __init__(self):
        self.states = {}          
        self.current_state = None  

    def add_state(self, name, state):
        """Регистрируем сцену: sm.add_state("menu", MenuState(sm))"""
        self.states[name] = state

    def change_state(self, name):
        """Переключаемся на другую сцену."""
        if self.current_state:
            self.states[self.current_state].exit()  
        self.current_state = name
        self.states[self.current_state].enter()     

    def handle_events(self, events):
        if self.current_state:
            self.states[self.current_state].handle_events(events)

    def update(self):
        if self.current_state:
            self.states[self.current_state].update()

    def draw(self, screen):
        if self.current_state:
            self.states[self.current_state].draw(screen)