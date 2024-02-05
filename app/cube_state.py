class CubeState:
    def __init__(self, state) -> None:
        self.state = state

    def solved(self):
        self.state = [
            [0, 1, 2, 3],
            [0, 1, 2, 3],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 1, 2, 3, 4, 5],
        ]

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

        if corner_swaps % 2 == 1 or alt_corner_swaps % 2 == 1 or center_swaps % 2 == 1:
            return False

        # Corner orientation check
        sum = 0
        for i in temp_state[2]:
            sum += i
        if sum % 3 != 0:
            return False

        sum = 0
        for i in temp_state[3]:
            sum += i
        if sum % 3 != 0:
            return False

        return True

    def move_R(self, reps):
        temp_state = self.state.copy()
        if reps == 1:
            self.state = [
                [
                    temp_state[0][0],
                    temp_state[0][2],
                    temp_state[0][3],
                    temp_state[0][1],
                ],
                [
                    temp_state[1][0],
                    temp_state[1][1],
                    temp_state[1][2],
                    temp_state[1][3],
                ],
                [
                    (temp_state[2][0]) % 3,
                    (temp_state[2][1] + 2) % 3,
                    (temp_state[2][2] + 2) % 3,
                    (temp_state[2][3] + 2) % 3,
                ],
                [
                    (temp_state[3][0]) % 3,
                    (temp_state[3][1]) % 3,
                    (temp_state[3][2]) % 3,
                    (temp_state[3][3] + 1) % 3,
                ],
                [
                    temp_state[4][0],
                    temp_state[4][1],
                    temp_state[4][5],
                    temp_state[4][2],
                    temp_state[4][4],
                    temp_state[4][3],
                ],
            ]

        if reps == 2:
            self.state = [
                [
                    temp_state[0][0],
                    temp_state[0][3],
                    temp_state[0][1],
                    temp_state[0][2],
                ],
                [
                    temp_state[1][0],
                    temp_state[1][1],
                    temp_state[1][2],
                    temp_state[1][3],
                ],
                [
                    (temp_state[2][0]) % 3,
                    (temp_state[2][1] + 1) % 3,
                    (temp_state[2][2] + 1) % 3,
                    (temp_state[2][3] + 1) % 3,
                ],
                [
                    (temp_state[3][0]) % 3,
                    (temp_state[3][1]) % 3,
                    (temp_state[3][2]) % 3,
                    (temp_state[3][3] + 2) % 3,
                ],
                [
                    temp_state[4][0],
                    temp_state[4][1],
                    temp_state[4][3],
                    temp_state[4][5],
                    temp_state[4][4],
                    temp_state[4][2],
                ],
            ]

    def move_L(self, reps):
        temp_state = self.state.copy()
        if reps == 1:
            self.state = [
                [
                    temp_state[0][0],
                    temp_state[0][1],
                    temp_state[0][3],
                    temp_state[0][2],
                ],
                [
                    temp_state[1][0],
                    temp_state[1][1],
                    temp_state[1][0],
                    temp_state[1][3],
                ],
                [
                    (temp_state[2][0]) % 3,
                    (temp_state[2][1] + 1) % 3,
                    (temp_state[2][2] + 1) % 3,
                    (temp_state[2][3] + 1) % 3,
                ],
                [
                    (temp_state[3][0]) % 3,
                    (temp_state[3][1]) % 3,
                    (temp_state[3][2]) % 3,
                    (temp_state[3][3] + 2) % 3,
                ],
                [
                    temp_state[4][0],
                    temp_state[4][1],
                    temp_state[4][3],
                    temp_state[4][5],
                    temp_state[4][4],
                    temp_state[4][2],
                ],
            ]

        if reps == 2:
            self.state = [
                [
                    temp_state[0][2],
                    temp_state[0][1],
                    temp_state[0][3],
                    temp_state[0][0],
                ],
                [
                    temp_state[1][0],
                    temp_state[1][1],
                    temp_state[1][2],
                    temp_state[1][3],
                ],
                [
                    (temp_state[2][0] + 1) % 3,
                    (temp_state[2][1]) % 3,
                    (temp_state[2][2] + 1) % 3,
                    (temp_state[2][3] + 1) % 3,
                ],
                [
                    (temp_state[3][0]) % 3,
                    (temp_state[3][1]) % 3,
                    (temp_state[3][2] + 2) % 3,
                    (temp_state[3][3]) % 3,
                ],
                [
                    temp_state[4][0],
                    temp_state[4][5],
                    temp_state[4][2],
                    temp_state[4][3],
                    temp_state[4][1],
                    temp_state[4][4],
                ],
            ]

    def move_U(self, reps):
        temp_state = self.state.copy()
        if reps == 1:
            self.state = [
                [
                    temp_state[0][1],
                    temp_state[0][3],
                    temp_state[0][2],
                    temp_state[0][0],
                ],
                [
                    temp_state[1][0],
                    temp_state[1][1],
                    temp_state[1][2],
                    temp_state[1][3],
                ],
                [
                    (temp_state[2][0] + 2) % 3,
                    (temp_state[2][1] + 2) % 3,
                    (temp_state[2][2]) % 3,
                    (temp_state[2][3] + 2) % 3,
                ],
                [
                    (temp_state[3][0] + 1) % 3,
                    (temp_state[3][1]) % 3,
                    (temp_state[3][2]) % 3,
                    (temp_state[3][3]) % 3,
                ],
                [
                    temp_state[4][3],
                    temp_state[4][1],
                    temp_state[4][2],
                    temp_state[4][4],
                    temp_state[4][1],
                    temp_state[4][5],
                ],
            ]

        if reps == 2:
            self.state = [
                [
                    temp_state[0][0],
                    temp_state[0][3],
                    temp_state[0][1],
                    temp_state[0][2],
                ],
                [
                    temp_state[1][0],
                    temp_state[1][1],
                    temp_state[1][2],
                    temp_state[1][3],
                ],
                [
                    (temp_state[2][0]) % 3,
                    (temp_state[2][1] + 1) % 3,
                    (temp_state[2][2] + 1) % 3,
                    (temp_state[2][3] + 1) % 3,
                ],
                [
                    (temp_state[3][0]) % 3,
                    (temp_state[3][1]) % 3,
                    (temp_state[3][2]) % 3,
                    (temp_state[3][3] + 2) % 3,
                ],
                [
                    temp_state[4][4],
                    temp_state[4][1],
                    temp_state[4][2],
                    temp_state[4][1],
                    temp_state[4][3],
                    temp_state[4][5],
                ],
            ]

    def move_B(self, reps):
        temp_state = self.state.copy()
        if reps == 1:
            self.state = [
                [
                    temp_state[0][0],
                    temp_state[0][1],
                    temp_state[0][2],
                    temp_state[0][3],
                ],
                [
                    temp_state[1][3],
                    temp_state[1][1],
                    temp_state[1][0],
                    temp_state[1][2],
                ],
                [
                    (temp_state[2][0]) % 3,
                    (temp_state[2][1]) % 3,
                    (temp_state[2][2]) % 3,
                    (temp_state[2][3] + 1) % 3,
                ],
                [
                    (temp_state[3][0] + 2) % 3,
                    (temp_state[3][1]) % 3,
                    (temp_state[3][2] + 2) % 3,
                    (temp_state[3][3] + 2) % 3,
                ],
                [
                    temp_state[4][0],
                    temp_state[4][1],
                    temp_state[4][2],
                    temp_state[4][5],
                    temp_state[4][3],
                    temp_state[4][4],
                ],
            ]

        if reps == 2:
            self.state = [
                [
                    temp_state[0][0],
                    temp_state[0][1],
                    temp_state[0][2],
                    temp_state[0][3],
                ],
                [
                    temp_state[1][2],
                    temp_state[1][1],
                    temp_state[1][3],
                    temp_state[1][0],
                ],
                [
                    (temp_state[2][0]) % 3,
                    (temp_state[2][1]) % 3,
                    (temp_state[2][2]) % 3,
                    (temp_state[2][3] + 2) % 3,
                ],
                [
                    (temp_state[3][0] + 1) % 3,
                    (temp_state[3][1]) % 3,
                    (temp_state[3][2] + 1) % 3,
                    (temp_state[3][3] + 1) % 3,
                ],
                [
                    temp_state[4][0],
                    temp_state[4][1],
                    temp_state[4][2],
                    temp_state[4][4],
                    temp_state[4][5],
                    temp_state[4][3],
                ],
            ]
