from nada_dsl import *


def nada_share_and_compare():
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    x = SecretInteger(Input(name="x", party=party1))
    y = SecretInteger(Input(name="y", party=party2))
    shared_x = party1.share(x, party2)
    shared_y = party2.share(y, party1)

    result1 = party1.compare(x, shared_y)
    result2 = party2.compare(y, shared_x)

    final_result = party1.xor(result1, result2)
    return [Output(final_result, "equal_or_not", party1)]

