def mosalas(x: list[int]) -> str:
    """
    Baresi mosalas boodan ya naboodan tebgh e zavaya daryafti.
    
    Args:
        x (list) : zaveh ha

    Returns:
        vaziat e mosalas boodan -> str
    """
    if sum(x) == 180 and x[0] > 0 and x[1] > 0 and x[2] > 0:
        return "Yes"
    else:
        return "No"

a = input().split()

b = list(map(int, a))

mosalas(b)

input()