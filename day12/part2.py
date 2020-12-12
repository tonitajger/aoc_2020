import numpy as np


class Ship:
    pos = np.array([0, 0])
    wp = np.array([10, 1])
    dir = 'E'
    unit_vecs = {'E': np.array([1, 0]),
                 'S': np.array([0, -1]),
                 'W': np.array([-1, 0]),
                 'N': np.array([0, 1])}
    r_matrix = np.array([[0, 1], [-1, 0]])

    def apply_instr(self, instr: str, val: int) -> None:
        if instr == 'R' or instr == 'L':
            self._rotate(instr, val)
        else:
            self._move(instr, val)

    def calc_distance(self):
        print(self.pos)
        print(np.abs(self.pos))
        return np.abs(self.pos).sum()

    def _move(self, instr_dir: str, instr_dist: int) -> None:
        if instr_dir == 'F':
            self.pos += self.wp * instr_dist
        else:
            self.wp += self.unit_vecs[instr_dir] * instr_dist

    def _rotate(self, instr_dir: str , instr_deg: int) -> None:
        inv = 1
        if instr_dir == 'L':
            inv = -1
        self.wp = np.dot(np.linalg.matrix_power(self.r_matrix * inv, (instr_deg // 90)), self.wp)



def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    ship = Ship()

    for line in lines:
        instr = line[0]
        val = int(line[1:])
        ship.apply_instr(instr, val)

    print(ship.calc_distance())


if __name__ == '__main__':
    main()




