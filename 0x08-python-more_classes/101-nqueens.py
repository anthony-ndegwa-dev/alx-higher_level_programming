#!/usr/bin/python3

"""An algorithm that resolves the N-Queen puzzle"""


def isSafe(m_queen, nqueen):


    """
    Function to determine if queens can kill each other or not
    
    Args:
    m_queen: array that has the queens positions
    nqueen: queen number
    
    Returns:
    True: when queens can't kill each other
    False: when some of the queens can kill
    """

    for i in range(nqueen):
        if m_queen[i] == m_queen[nqueen]:
            return False

        if abs(m_queen[i] - m_queen[nqueen]) == abs(i - nqueen):
            return False

    return True

def print_result(m_queen, nqueen):
    """Prints the list with the Queens positions"""

    
    res = []
    for i in range(nqueen):
        res.append([i, m_queen[i]])

    print(res)

def Queen(m_queen, nqueen):
    """Function that executes the Backtracking algorithm"""


    if nqueen is len(m_queen):
        print_result(m_queen, nqueen)
        return

    m_queen[nqueen] = -1
    while((m_queen[nqueen] < len(m_queen) - 1)):
        m_queen[nqueen] += 1

        if isSafe(m_queen, nqueen) is True:
            if nqueen is not len(m_queen):
                Queen(m_queen, nqueen + 1)

def solveNQueen(size):
    """Function that invokes the Backtracking algorithm

    Args:
        size: size of the chessboard
    """


    m_queen = [-1 for i in range(size)]
    Queen(m_queen, 0)

if __name__ == '__main__':
    

    import sys

    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solveNQueen(size)
