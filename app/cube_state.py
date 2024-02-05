class CubeState:
    def __init__(self, state) -> None:
        self.state = state
    
    def solved(self):
        self.state = [[0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5]]

    def is_solvable(self, state):
        temp_state = state.copy()
        temp_state2 = state.copy()
        temp_state.sort()
        temp_arg = 0
        corner_swaps = 0
        for i, v in enumerate(temp_state2[0]):
            if not i == v:
                temp_arg = temp_state2[0][v]
                temp_state2[0][v] = v
                temp_state2[0][i] = temp_arg
                corner_swaps += 1
            if temp_state2 == temp_state:
                break
        return corner_swaps

cube = CubeState([[1, 0, 3, 2, 5, 4, 6, 7], [0, 1, 2, 3, 4, 5]])
print(cube.is_solvable(cube.state))