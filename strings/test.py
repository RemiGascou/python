import encodings


#print(''.join(['- ' + e + '\n' for e in sorted(set(encodings.aliases.aliases.values()))]))


cipher = u"zAzMTQ1NDAzNTMzNmUzMDczNGIzMTY0NDQzMTMzNzM=".encode('utf8')

decoded_data = base64.b64decode(cipher)