def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if 9<a<100 and a%2==0:
        return 'ikki xonali juft son'
    if 9<a<100 and a%2!=0:
        return 'ikki xonali toq son'
    if 99<a<1000 and a%2==0:
        return 'uch xonali juft son'
    if 99<a<1000 and a%2!=0:
        return 'uch xonali toq son'
    else:
        return 'bunday sonni bilmayman'
print(main(9638))