
uniqueLines = set()
with open('/home/kamoche/Desktop/STOP.txt', 'r') as file:
    uniqueLines = set(file.readlines())
    with open('/home/kamoche/Desktop/SendStopTo79079.txt', 'w') as uniqdump:
        uniqdump.writelines(uniqueLines)





