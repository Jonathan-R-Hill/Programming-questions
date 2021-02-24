"""
You are given a string. Split the string on a " " (space) 
delimiter and join using a - hyphen. 
"""
def split_and_join(line):
    split_string = line.split()
    joined_string = '-'.join(split_string)
    
    return joined_string

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)