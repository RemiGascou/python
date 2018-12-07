def gentextfrombin(ctx):
    return ''.join([chr(int(ctx[k*8:(k+1)*8],2)) for k in range(len(ctx)//8)])