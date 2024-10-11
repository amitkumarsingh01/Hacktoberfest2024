from collections import deque
import numpy as np

faces = ['U', 'D', 'L', 'R', 'F', 'B']
face_colors = ['W', 'Y', 'G', 'B', 'O', 'R']

def rotate_face(cube, face):
    face_map = {
        'U': (0, (3, 0, 1, 2, 3)),
        'D': (1, (3, 0, 1, 2, 3)),
        'L': (2, (3, 0, 1, 2, 3)),
        'R': (3, (3, 0, 1, 2, 3)),
        'F': (4, (3, 0, 1, 2, 3)),
        'B': (5, (3, 0, 1, 2, 3))
    }
    face_idx, rot = face_map[face]
    cube[face_idx] = np.rot90(cube[face_idx], k=-1)

def scramble_cube(cube, moves):
    for move in moves:
        rotate_face(cube, move)

def is_solved(cube):
    for face in cube:
        if not np.all(face == face[0, 0]):
            return False
    return True

def generate_moves():
    return ['U', 'D', 'L', 'R', 'F', 'B']

def solve_cube(cube):
    queue = deque([(cube.copy(), [])])
    seen = set()
    while queue:
        current_cube, path = queue.popleft()
        if is_solved(current_cube):
            return path
        cube_hash = tuple(map(tuple, current_cube.flatten()))
        if cube_hash in seen:
            continue
        seen.add(cube_hash)
        for move in generate_moves():
            new_cube = current_cube.copy()
            rotate_face(new_cube, move)
            queue.append((new_cube, path + [move]))

def create_cube():
    cube = []
    for color in face_colors:
        face = np.full((3, 3), color)
        cube.append(face)
    return np.array(cube)

if __name__ == '__main__':
    cube = create_cube()
    scramble_moves = ['U', 'R', 'F', 'L', 'D']
    scramble_cube(cube, scramble_moves)
    solution = solve_cube(cube)
    print(f"Scramble Moves: {scramble_moves}")
    print(f"Solution: {solution}")
