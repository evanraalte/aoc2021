from collections import defaultdict

with open("assets/day14.txt") as f:
    starting_polynomial, pair_insertions = tuple(f.read().split("\n\n"))
    pair_insertions = dict(p.split(" -> ") for p in pair_insertions.splitlines())

polynomial_chunks = [starting_polynomial[i : i + 2] for i in range(0, len(starting_polynomial))]
state = {k: polynomial_chunks.count(k) for k in pair_insertions.keys() if polynomial_chunks.count(k) > 0}


next_chunks_map = {}
for k, v in pair_insertions.items():
    new = k[0] + v + k[1]
    polynomial_chunks = {new[i : i + 2] for i in range(0, len(new)) if len(new[i : i + 2]) == 2}
    next_chunks_map[k] = polynomial_chunks

amounts = defaultdict(int, {letter: starting_polynomial.count(letter) for letter in set(starting_polynomial)})
for step in range(1, 40 + 1):
    state_next = defaultdict(int)
    for chunk, num in state.items():
        for chunk_next in next_chunks_map[chunk]:
            state_next[chunk_next] += num  # add to others
        amounts[pair_insertions[chunk]] += num
    state = state_next

    if step in [10, 40]:
        print(f"Step {step}: ", max(amounts.values()) - min(amounts.values()))
