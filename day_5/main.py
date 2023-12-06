# source, destination, length
Conversion = tuple[int, int, int]
ConversionSet = list[Conversion]
SeedPair = tuple[int, int]


def get_input() -> list[str]:
    """
    Read the input file and return the contents as a list of strings.
    """

    with open("day_5/input/input.txt", "r") as f:
        return f.read().splitlines()


def process_seed_line(seeds_line: str, for_seed_pairs: bool) -> list[int] | list[SeedPair]:
    """
    Process the seed line and return a list of seeds (if for_seed_pairs is False) or seed pairs (if
    for_seed_pairs is True).
    """

    seeds = [int(seed) for seed in seeds_line.split(" ")]
    if for_seed_pairs:
        start_seeds = seeds[::2]
        lengths = seeds[1::2]
        seeds = [
            (start_seed, start_seed + length - 1)
            for (start_seed, length) in zip(start_seeds, lengths)
        ]

    return seeds


def process_input(
    puzzle_input: list[str], for_seed_pairs=False
) -> tuple[list[int], list[Conversion]] | tuple[list[SeedPair], list[Conversion]]:
    """
    Process the input into a list of ints (if for_seed_pairs is False) or a list of tuples (if
    for_seed_pairs is True), and a list of Conversions.
    """

    seeds_line = puzzle_input[0][7:]
    conversion_lines = puzzle_input[2:]

    seeds = process_seed_line(seeds_line, for_seed_pairs)
    conversion_sets = process_conversions(conversion_lines)

    return seeds, conversion_sets


def process_conversions(conversion_lines: list[str]) -> list[ConversionSet]:
    """
    Process the conversion lines and return a list of conversions.
    """

    conversion_sets = []

    conversions = []
    for line in conversion_lines:
        if line == "":
            conversion_sets.append(conversions)
            conversions = []
            continue

        elif not line[0].isdigit():
            continue

        destination, source, length = line.split(" ")
        conversion = (int(destination), int(source), int(length))
        conversions.append(conversion)
    else:
        conversion_sets.append(conversions)

    return conversion_sets


def execute_conversion_for_seed(
    line: str, pre_conversion: list[int], post_conversion: list[int]
) -> None:
    """
    Execute the conversion for a single seed.
    """

    destination, source, length = line

    for seed in pre_conversion[:]:
        if seed in range(source, source + length + 1):
            post_conversion.append(destination + seed - source)

            pre_conversion.remove(seed)


def execute_conversions_for_seeds(
    seeds: list[int], conversion_sets: list[ConversionSet]
) -> list[int]:
    """
    Execute the conversions on the seeds and return the resulting list of seeds.
    """

    pre_conversion = []
    post_conversion = seeds[:]

    for conversion_set in conversion_sets:
        pre_conversion = post_conversion[:]
        post_conversion = []

        for conversion in conversion_set:
            execute_conversion_for_seed(conversion, pre_conversion, post_conversion)

        post_conversion.extend(pre_conversion)

    return post_conversion


def execute_conversion_for_seed_pair(
    conversion: Conversion,
    seed_pair: SeedPair,
    new_pre_conversion: list[SeedPair],
    post_conversion: list[SeedPair],
) -> None:
    """
    Execute the conversion for a single seed pair.
    """

    start_seed, end_seed = seed_pair

    destination, source_start, length = conversion

    source_end = source_start + length - 1

    # If there's no overlap, don't convert the seed pair
    if start_seed > source_end or end_seed < source_start:
        new_pre_conversion.append(seed_pair)
        return

    # If there is overlap, three options are possible:
    # 1. The seed pair is fully converted
    # 2. The start of the seed pair is not converted
    # 3. The end of the seed pair is not converted

    if start_seed < source_start:
        preceding_seed = (start_seed, source_start - 1)
        new_pre_conversion.append(preceding_seed)
        new_seed_start = destination
    else:
        new_seed_start = destination + start_seed - source_start

    if end_seed > source_end:
        succeeding_seed = (source_end + 1, end_seed)
        new_pre_conversion.append(succeeding_seed)
        new_seed_end = destination + source_end - source_start
    else:
        new_seed_end = destination + end_seed - source_start

    post_conversion.append((new_seed_start, new_seed_end))


def execute_conversions_for_seed_pairs(
    seed_pairs: list[SeedPair], conversion_sets: list[ConversionSet]
) -> list[SeedPair]:
    """
    Execute the conversions on the seed pairs and return the resulting list of seed pairs.
    """

    pre_conversion = seed_pairs

    for conversion_set in conversion_sets:
        post_conversion = []

        # Execute all conversions in a conversion set on all seed pairs
        for conversion in conversion_set:
            # Execute the conversion on all seed pairs

            new_pre_conversion = []

            for seed_pair in pre_conversion:
                # Execute the conversion on the seed pair.
                # If converted, add it to 'post_conversion'.
                # If not (or not fully) converted, add it to new_pre_conversion

                execute_conversion_for_seed_pair(
                    conversion, seed_pair, new_pre_conversion, post_conversion
                )

            # Set pre_conversion to new_pre_conversion, so all non-converted values are used in the
            # next conversion
            pre_conversion = new_pre_conversion

        # Add all remaining seed pairs to post_conversion (they didn't get converted)
        post_conversion.extend(pre_conversion)

        # Set pre_conversion to post_conversion, so the new loop starts with all converted values
        pre_conversion = post_conversion

    return post_conversion


def solve_puzzle_1(puzzle_input: list[str] = None) -> int:
    """
    Solve puzzle 1.
    """

    if puzzle_input is None:
        puzzle_input = get_input()

    seeds, conversion_sets = process_input(puzzle_input)
    converted_seeds = execute_conversions_for_seeds(seeds, conversion_sets)

    return min(converted_seeds)


def solve_puzzle_2(puzzle_input: list[str] = None) -> int:
    """
    Solve puzzle 2.
    """

    if puzzle_input is None:
        puzzle_input = get_input()

    seed_pairs, conversion_sets = process_input(puzzle_input, for_seed_pairs=True)
    converted_seed_pairs = execute_conversions_for_seed_pairs(seed_pairs, conversion_sets)

    converted_seed_pairs.sort(key=lambda x: x[0])
    return converted_seed_pairs[0][0]


if __name__ == "__main__":
    solution_1 = solve_puzzle_1()
    print(f"The solution for puzzle 1 is: {solution_1}")

    solution_2 = solve_puzzle_2()
    print(f"The solution for puzzle 2 is: {solution_2}")
