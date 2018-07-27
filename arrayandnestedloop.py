def main():
    grid=[['S', 'F', 'F', 'F'], ['F', 'H', 'F', 'H'], ['F', 'F', 'F', 'H'], ['H', 'F', 'F', 'G']]
    for eachlist in grid:
        list1 = ""
        for eachletter in eachlist:
            list1 += eachletter
        print(list1)
main()
