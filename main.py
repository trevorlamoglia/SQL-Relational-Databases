import sqlite3


# Connect to database
connection = sqlite3.connect('friends.db')
cursor = connection.cursor()


# Create table (if it does not already exist)
cursor.execute("CREATE TABLE IF NOT EXISTS friends (name TEXT, age INT, birthday DATE)")

def get_name(cursor):
    cursor.execute('SELECT name FROM friends')
    results = cursor.fetchall()
    for index in range(len(results)):
        print(f'{index+1}. {results[index][0]}')
    choice = int(input('Select >'))
    return results[choice-1][0]

choice = None
while choice != "5":
    print("1) Display Friends")
    print("2) Add Friend")
    print("3) Update Friend age")
    print("4) Delete Friend")
    print("5) Quit")
    choice = input("> ")
    print()
    if choice == "1":
        # Display Friends
        cursor.execute('SELECT * FROM friends ORDER BY age DESC')
        print("{:>7}  {:>6}  {:>14}".format("Name", "Age", "Birthday"))
        for record in cursor.fetchall():
            print("{:>7}  {:>6}  {:>14}".format(record[0], record[1], record[2]))
    elif choice == "2":
        # Add New Friend
        name = input("Name: ")
        age = input("Age: ")
        birthday = input("Birthday: ")
        values = (name, age, birthday)
        # Add Friends
        cursor.execute('INSERT INTO friends VALUES (?, ?, ?)', values)
        connection.commit()
    elif choice == "3":
        # Update Friend age
        name = input("Name: ")
        age = int(input("Age: "))
        values = (age, name)
        cursor.execute ('UPDATE friends SET age = ? WHERE name = ?', values)
        connection.commit()
        if cursor.rowcount == 0:
            print('ERROR! Friend does not exist yet.')
    elif choice == "4":
        # Delete Friend
        name = get_name(cursor)
        values = (name,)
        cursor.execute('DELETE FROM friends WHERE name = ?', values)
        connection.commit()
    print()

# Close the database connection before exiting
connection.close()