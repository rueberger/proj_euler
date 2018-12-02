""" Main entrypoint into python euler solvers
"""

import argparse
import time
import importlib


def main():
    """ Parse args, dispatch to solver, print timing
    """
    parser = argparse.ArgumentParser(description='Dispatch for python euler solvers')

    problem_num_help = "number of problem to solve, int"
    parser.add_argument('problem_num', help=problem_num_help)

    args = parser.parse_args()

    problem_number = int(args.problem_num)

    importlib.import_module('euler.problem_{}.solver'.format(problem_number))

    start_time = time.time()

    print(solve())

    print('Elapsed time: {}'.format(time.time() - start_time))


if __name__ == "__main__":
    main()
