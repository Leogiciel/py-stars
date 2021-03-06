from chain import Chain


def compute(arg: str) -> int:
    lines = arg.splitlines()
    # check lines
    if len(lines) != 2:
        raise ValueError(
            f"Argument must contains 2 chains in separated lines,"
            f"arg received : [{arg}]"
            f" contains [{len(lines)}] lines"
        )
    first = lines[0]
    second = lines[1]
    if len(first) != len(second):
        raise ValueError("Both chains must have the same length")
    if len(first) < 1 or len(first) > 25:
        raise ValueError("Chains length must be between 1 and 25")
    # check lines values
    check_chain(first)
    check_chain(second)
    # work
    chain = Chain(first, second)
    return chain.compute()


def check_chain(chain: str) -> bool:
    result = True
    i = 0
    while result and i < len(chain):
        result &= (chain[i] == "0") or (chain[i] == "1")
        i += 1
    if not result:
        raise ValueError(
            f"Argument [{chain}] does not contain only '0' and '1' characters"
        )
    return result
