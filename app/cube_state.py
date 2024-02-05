class CubeState:
    def __init__(self, state) -> None:
        self.state = state
    
    def solved(self):
        self.state = [[0, 1, 2, 3], [0, 1, 2, 3], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 2, 3, 4, 5]]

    def is_solvable(self):
        # Parity check
        temp_state = self.state.copy()
        temp_arg = 0
        corner_swaps = 0
        alt_corner_swaps = 0
        center_swaps = 0
        for i, v in enumerate(temp_state[0]):
            if not i == v:
                temp_arg = temp_state[0][v]
                temp_state[0][v] = v
                temp_state[0][i] = temp_arg
                corner_swaps += 1
        
        for i, v in enumerate(temp_state[1]):
            if not i == v:
                temp_arg = temp_state[1][v]
                temp_state[1][v] = v
                temp_state[1][i] = temp_arg
                alt_corner_swaps += 1

        for i, v in enumerate(temp_state[4]):
            if not i == v:
                temp_arg = temp_state[4][v]
                temp_state[4][v] = v
                temp_state[4][i] = temp_arg
                center_swaps += 1
        
        if corner_swaps%2 == 1 or alt_corner_swaps%2 == 1 or center_swaps%2 == 1:
            return False
        
        #Corner orientation check
        sum = 0
        for i in temp_state[2]:
            sum += i
        if sum%3 != 0:
            return False
        
        sum = 0
        for i in temp_state[3]:
            sum += i
        if sum%3 != 0:
            return False
        
        return True

cube = CubeState([[0, 1, 2, 3], [0, 1, 2, 3], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 2, 3, 4, 5]])
print(cube.is_solvable())
