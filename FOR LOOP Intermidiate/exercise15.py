number = [500,13,42,13,52,13,24,53,64,5,24,25,35,65]
for item in number:
    if item > 500:
        break
    elif item > 150 :
        continue
    elif item % 5 == 0 :
        print(item)