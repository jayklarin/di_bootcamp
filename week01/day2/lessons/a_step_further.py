import random
import math
import statistics
import os

# Clear terminal at the start of the program
os.system('cls' if os.name == 'nt' else 'clear')

# -----------------------------
# Original Functions (with clear comments)
# -----------------------------

def replace_values(lst, change_value, to_value):
    """
    Replace every occurrence of `change_value` in lst with `to_value`.
    Prints before/after state and returns (lst, number_of_replacements).

    NOTE: This is the "noisy" version — it prints a lot.
    """
    print('List before running:')
    print(lst)
    print()

    occurrences = 0
    for i, val in enumerate(lst):
        if val == change_value:
            lst[i] = to_value
            occurrences += 1
            print(f'Found it and changed it at index {i}!')

    if occurrences == 0:
        print("It's not here!")

    print()
    print(f"The value {change_value} was changed to {to_value} a total of {occurrences} times")
    print()
    print('List after running:')
    print(lst)
    return lst, occurrences


def create_list(length, num_range, static_num, percentage):
    """
    Create a list of given length.
    Each element has a chance (percentage%) of being `static_num`.
    Otherwise, it is a random number in [1, num_range].

    Trick: If the random number accidentally equals static_num,
    we bump it to avoid inserting more static_nums than we intended.
    """
    p = percentage / 100
    lst = []
    for _ in range(length):
        if random.random() < p:
            # Insert the "special" number (e.g., 20) with probability p
            lst.append(static_num)
        else:
            # Insert a random number
            n = random.randint(1, num_range)
            # If it accidentally equals static_num, bump it to another value
            lst.append(n if n != static_num else (n % num_range) + 1)
    return lst


# -----------------------------
# Silent helper (no prints)
# -----------------------------
def replace_values_silent(lst, change_value, to_value):
    """
    Same as replace_values but without printing.
    Mutates the list in place and returns the count of replacements.
    """
    count = 0
    for i, val in enumerate(lst):
        if val == change_value:
            lst[i] = to_value
            count += 1
    return count


# -----------------------------
# Runs Test Helper
# -----------------------------
def runs_test_z(indicators):
    """
    indicators: a list of 0s and 1s
    - 1 means the element was the special number (static_num)
    - 0 means it was not

    The Runs Test checks whether the 1s are scattered randomly
    or appear in unusual clusters.

    Idea:
    - A "run" is a sequence of consecutive identical values (e.g., 111 or 00).
    - We count how many runs appear in the sequence.
    - Too few runs -> the special numbers are clumped together.
    - Too many runs -> the special numbers are overly spread apart.

    Returns:
        z-score: how unusual the number of runs is compared to randomness.
        (z close to 0 = normal randomness, large |z| = strange pattern)
    """
    if not indicators:
        return 0.0

    n1 = sum(indicators)               # how many 1s (special number)
    n2 = len(indicators) - n1          # how many 0s (not special)
    if n1 == 0 or n2 == 0:
        # If there are no 1s or no 0s, we can’t run this test
        return 0.0

    # Count how many "runs" are in the sequence
    runs = 1
    for i in range(1, len(indicators)):
        if indicators[i] != indicators[i-1]:
            runs += 1

    # Expected runs under random placement
    mu = 1 + (2 * n1 * n2) / (n1 + n2)

    # Variance of runs under randomness (formula from statistics)
    var = (2 * n1 * n2 * (2 * n1 * n2 - n1 - n2)) / (((n1 + n2) ** 2) * (n1 + n2 - 1))
    if var <= 0:
        return 0.0

    # z = (observed - expected) / standard deviation
    z = (runs - mu) / math.sqrt(var)
    return z


# -----------------------------
# Evaluator Function
# -----------------------------
def evaluate_replacements(
    trials,
    list_length,
    number_range,
    number_to_replace,
    number_to_replace_with,
    percentage_to_replace,
    use_noisy_replace=False,
    compute_runs_test=True
):
    """
    Runs the create_list + replace_values cycle multiple times.
    Collects statistics about how close the actual outcomes are
    to the expectations.

    Parameters
    ----------
    trials : int
        How many times to run the experiment.
    list_length : int
        How long each list should be.
    number_range : int
        Range of possible random numbers (1..number_range).
    number_to_replace : int
        The "special" number we are targeting (e.g., 20).
    number_to_replace_with : int
        The replacement value (e.g., 200).
    percentage_to_replace : float
        Desired percentage chance for each element to be number_to_replace.
    use_noisy_replace : bool
        If True, prints details from replace_values (lots of output).
        If False, runs silently.
    compute_runs_test : bool
        If True, runs-test z-scores are also calculated.

    Returns
    -------
    summary : dict
        Aggregated statistics across all trials.
    per_trial : list of dict
        Detailed results for each individual trial.
    """

    # Convert percentage to decimal probability
    p = percentage_to_replace / 100

    # Theoretical expectation:
    expected_mean = list_length * p
    expected_std = math.sqrt(list_length * p * (1 - p)) if 0 < p < 1 else 0.0

    per_trial = []
    for _ in range(trials):
        # Step 1: Make a new semi-random list
        lst = create_list(list_length, number_range, number_to_replace, percentage_to_replace)

        # Step 2: Record where the special number appears BEFORE replacement
        indicators = [1 if x == number_to_replace else 0 for x in lst]

        # Step 3: Replace the values (with noisy or silent function)
        if use_noisy_replace:
            _, actual_count = replace_values(lst, number_to_replace, number_to_replace_with)
        else:
            actual_count = replace_values_silent(lst, number_to_replace, number_to_replace_with)

        # Step 4: Compare actual vs expected
        # z-score = (difference from expectation) / (expected standard deviation)
        z_count = (actual_count - expected_mean) / expected_std if expected_std > 0 else 0.0

        # Step 5: Optional runs test to see if replacements are clustered
        z_runs = runs_test_z(indicators) if compute_runs_test else None

        per_trial.append({
            "actual": actual_count,                                # how many replacements we saw
            "actual_pct": actual_count / list_length,              # as a fraction of list length
            "error": actual_count - expected_mean,                 # signed error
            "abs_error": abs(actual_count - expected_mean),        # absolute error
            "z_count": z_count,                                    # how far count is from expectation
            "z_runs": z_runs                                       # clustering measure
        })

    # -----------------------------
    # Aggregate summary across trials
    # -----------------------------
    actuals = [d["actual"] for d in per_trial]
    abs_errs = [d["abs_error"] for d in per_trial]
    z_counts = [d["z_count"] for d in per_trial]
    z_runs_vals = [d["z_runs"] for d in per_trial if d["z_runs"] is not None]

    summary = {
        "trials": trials,
        "n": list_length,
        "p_expected": p,
        "expected_mean": expected_mean,
        "expected_std": expected_std,
        "mean_actual": statistics.mean(actuals),
        "std_actual": statistics.pstdev(actuals),
        "mean_abs_error": statistics.mean(abs_errs),
        "mean_z_count": statistics.mean(z_counts),
        "std_z_count": statistics.pstdev(z_counts),
    }

    if compute_runs_test and z_runs_vals:
        summary["mean_z_runs"] = statistics.mean(z_runs_vals)
        summary["std_z_runs"] = statistics.pstdev(z_runs_vals)

    return summary, per_trial


# -----------------------------
# Example Usage
# -----------------------------
if __name__ == "__main__":
    list_length = 80
    number_range = 100
    number_to_replace = 20
    number_to_replace_with = 200
    percentage_to_replace = 10

    # Run experiment 200 times
    summary, per_trial = evaluate_replacements(
        trials=200,
        list_length=list_length,
        number_range=number_range,
        number_to_replace=number_to_replace,
        number_to_replace_with=number_to_replace_with,
        percentage_to_replace=percentage_to_replace,
        use_noisy_replace=False,      # set True to see detailed per-trial prints
        compute_runs_test=True        # also measure clustering of replacements
    )

    print("=== Summary ===")
    for k, v in summary.items():
        # Print numbers cleanly
        if isinstance(v, float):
            print(f"{k}: {v:.4f}")
        else:
            print(f"{k}: {v}")

    print("\nFirst 5 trials (out of 200):")
    for row in per_trial[:5]:
        print(row)
