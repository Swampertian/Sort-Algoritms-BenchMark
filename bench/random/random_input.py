import random
from typing import List


def generate_input(size: int, seed: int = 42) -> List[int]:
    """Generates a list of random integers in arbitrary order."""
    rng = random.Random(seed)
    return [rng.randint(0, size * 10) for _ in range(size)]
