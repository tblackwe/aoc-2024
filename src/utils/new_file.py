import os

l = filter(lambda x: "__" not in x and ".py" in x, os.listdir("src"))
l = list(l)
n = int(sorted(l)[-1][:2]) + 1 if len(l) > 0 else 1

DEFAULT_FILE = f"from utils.api import get_input\n\ninput_str = get_input({n})\ntest_data = load_sample({n})\n\n# WRITE YOUR SOLUTION HERE\n\n# Part 1\n\nprint(f\"Day {n} Part 1:\")\n\n# Part 2\n\nprint(f\"Day {n} Part 2:\")"

path = f"src/{n:02d}.py"
with open(path, "w") as f:
    f.write(DEFAULT_FILE)

print(f"Enter your solution in {path}")
