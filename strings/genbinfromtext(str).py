def genbinfromtext(ctx):
    return ''.join([str(bin(ord(c)))[2:].rjust(8,"0") for c in ctx])