# Write your solution here
def same_chars(a,b,c):
        if((len(a)-1) < b or (len(a)-1) < c):
            return False
        else:
            if(a[b]==a[c]):
                return True
            else:
                return False
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("programmer", 0, 12))