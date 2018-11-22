def checksum(spreadsheet):
    total = 0
    spreadsheet_array = spreadsheet.split('\n')
    for row in spreadsheet_array:
        elements = [int(n) for n in row.split()]
        elements.sort(reverse=True)
        found = False
        for i in range(len(elements)):
            if found:
                break
            for j in range(i+1, len(elements)):
                if elements[i] % elements[j] == 0:
                    total += elements[i] // elements[j]
                    found = True
                    break
        found = False

    print(total)


spreadsheet = '''5 9 2 8
9 4 7 3
3 8 6 5'''

checksum(spreadsheet)


