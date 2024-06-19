# Write your solution here
def histogram(word:int):
    groups={}
    stars=""
    for character in word:
        if character not in groups:
            groups[character]=""
        groups[character]=str(groups[character]) + "*"
    for key, value in groups.items():
        print (f'{key} {value}')
if __name__ == "__main__":  
    histogram("statistically")