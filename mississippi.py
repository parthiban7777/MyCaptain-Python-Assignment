def most_frequent():
    string = input("Please enter a string: ")
    freq = {}
    
    for i in string:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    for i in freq:
        print(f"{i[0]} = {i[1]:02}")

most_frequent()

