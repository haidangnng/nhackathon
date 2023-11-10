with open("./input.txt", "r") as f:
    input = f.read()


directions = {
    "L": (-1, 0),
    "R": (1, 0),
    "D": (0, 1),
    "U": (0, -1),
}


def get_mazes(block):
    block = block.split("\n")
    name = block[0]
    maze = []
    start = ()

    for line in range(1, len(block)):
        maze.append(block[line].split())
        for index, char in enumerate(block[line].split()):
            if char == "S":
                start = (line - 1, index)

    return (name, maze, start)


def bfs(maze, start):
    visited = set()
    queue = [(start, ["S"])]
    while queue:
        (cur_x, cur_y), path = queue.pop(0)

        visited.add((cur_x, cur_y))

        for dir in directions:
            (dir_x, dir_y) = directions[dir]
            next_x = cur_x + dir_x
            next_y = cur_y + dir_y

            next_cell = maze[next_y][next_x]
            if next_cell == "G":
                path = path + [dir, "G"]
                return " ".join(path)
            if next_cell == "." and (next_x, next_y) not in visited:
                visited.add((next_x, next_y))
                queue.append(((next_x, next_y), path + [dir]))


for block in input.split("\n\n"):
    (name, maze, start) = get_mazes(block)
    res = bfs(maze, start)
    print(name)
    print(res, end="\n\n")
