import random
from typing import List


def generate_input(size: int, seed: int = 42) -> List[int]:
    rng = random.Random(seed)
    return sorted((rng.randint(0, size * 10) for _ in range(size)), reverse=True)
