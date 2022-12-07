def recursiveLength( str ):
    if str == '':
        return 0
    return 1 + recursiveLength( str[1:])