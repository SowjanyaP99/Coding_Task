s = 'aabcccccaaa'

def compress_string(s: str) -> str:
    # Initialize variables
    compressed = []
    count_consecutive = 0

    # Iterate through the string
    for i in range(len(s)):
        count_consecutive += 1
        
        # If next char is different or it's the end of the string, append the count
        if i + 1 >= len(s) or s[i] != s[i + 1]:
            compressed.append(s[i])
            compressed.append(str(count_consecutive))
            count_consecutive = 0
            

    # Convert the list to a string
    compressed_string = ''.join(compressed)
    print("after condition join", compressed_string)
    
    return compressed_string
# Example usage
input_string = "aabcccccaaa"
compressed_string = compress_string(input_string)
print(compressed_string)  # Output: "a2b1c5a3"
