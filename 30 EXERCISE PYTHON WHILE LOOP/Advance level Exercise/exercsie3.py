#Database Search: Simulate searching a database of names using a while loop.
def search_database(database,target_name):
    index = 0 
    while index < len(database):
        if database[index] != target_name:
            index += 1
            continue
        return f"{target_name} found at index {index}"
    return f"{target_name} not found in the database"
#Example usage
database= ["Alice","Bob","Charalie","Dinana","Eve"]
target_name = input("Enter a name to search:")
print(search_database(database,target_name))