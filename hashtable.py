hashtable = {
  1: "red",
  2: "blue",
  3: "green"
}
print("\nINITIAL HASH TABLE")
print(hashtable)

# INSERT ELEMENT INTO HASH TABLE
print("\nINSERT ELEMENT INTO HASH TABLE")
hashtable[4] = "orange"
print(hashtable)

# GET ELEMENT FROM HASH TABLE
print("\nGET ELEMENT FROM HASH TABLE")
element = hashtable.get(2, "purple")
print(element)

# UPDATE ELEMENT IN HASH TABLE
print("\nUPDATE ELEMENT IN HASH TABLE")
hashtable[1] = "yellow"
print(hashtable)

# DELETE ELEMENT FROM HASH TABLE
print("\nDELETE ELEMENT FROM HASH TABLE")
del hashtable[1]
print(hashtable)