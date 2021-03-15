from chain import Chain


def compute(arg):
    # check argument type
    if type(arg) is not str:
        raise ValueError(f'Argument must be a string, not {type(arg)}')
    lines = arg.splitlines()
    # check lines
    if len(lines) != 2:
        raise ValueError(f'Argument must contains 2 chains in separated lines, arg received : [{arg}] contains [{len(lines)}] lines')
    first = lines[0]
    second = lines[1]
    if len(first) != len(second):
        raise ValueError('Both chains must have the same length')
    # check lines values
    check_chain(first)
    check_chain(second)
    # work
    chain = Chain(first, second)
    return chain.compute()


def check_chain(chain):
    result = True
    i = 0
    while result and i < len(chain):
        result &= (chain[i] == '0') or (chain[i] == '1')
        i += 1
    if not result:
        raise ValueError(f'Argument [{chain}] doesn\'t contain only \'0\' and \'1\' characters')
    return result
