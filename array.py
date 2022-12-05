arr = [2, 5, 3, 10, 8]
print("\nINITIAL ARRAY")
print(arr)

# Append to array
print("\nAPPEND TO ARRAY")
arr.append(100)
print(arr)

# Get an array element
print("\nGET AN ARRAY ELEMENT")
print(arr[2])

# Set an array element
print("\nSET AN ARRAY ELEMENT")
arr[2] = 50
print(arr)

# Insert value: 38 at array 2
print("\nINSERT INTO ARRAY")
arr.insert(2, 38)
print(arr)

# Delete from array
print("\nDELETE FROM ARRAY")
arr.pop(2)      # delete by index
print(arr)

# Get array slice
print("\nGET ARRAY SLICE")
print(arr[2:5])