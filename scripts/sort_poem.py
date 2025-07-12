
def sort_file_lines(filename):
    with open(filename) as file:
        lines = file.readlines()
    
    
    lines = [line.strip() for line in lines]
    lines.sort(key=str.lower)  
    
    print("\nSorted lines:\n")
    for line in lines:
        print(line)

if __name__ == "__main__":
    sort_file_lines("spider.txt")
