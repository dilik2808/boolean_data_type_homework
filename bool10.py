import  math
def main(a):
    """check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    s=math.sqrt(a)//1
    return s*s==a
    

print (main(15))