import sqlite3


# Connect to database
connection = sqlite3.connect('menu.db')
cursor = connection.cursor()


# Create table (if it does not already exist)
cursor.execute("CREATE TABLE IF NOT EXISTS menu (name TEXT, main ingredient TEXT, price INT, calorie INT)")

def get_name(cursor):
    cursor.execute('SELECT name FROM menu')
    results = cursor.fetchall()
    for index in range(len(results)):
        print(f'{index+1}. {results[index][0]}')
    choice = int(input('Select >'))
    return results[choice-1][0]

choice = None
while choice != "5":
    print("1) Display Menu")
    print("2) Add Dish")
    print("3) Update Dish price")
    print("4) Delete Dish")
    print("5) Quit")
    choice = input("> ")
    print()
    if choice == "1":
        # Display Menu
        cursor.execute('SELECT * FROM menu ORDER BY name ASC')
        print("{:>10}  {:>20}  {:>10} {:>10}".format("Name", "Main Ingredient", "Price", "Calories"))
        for record in cursor.fetchall():
            print("{:>10}  {:>20}  {:>10} {:>10}".format(record[0], record[1], record[2], record[3]))
    elif choice == "2":
        # Add New Dish
        name = input("Name: ")
        main_ingredient = input("Main Ingredient: ")
        price = input("Price: ")
        calorie = input('Calories: ')
        values = (name, main_ingredient, price, calorie)
        # Add Dish
        cursor.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', values)
        connection.commit()
    elif choice == "3":
        # Update Dish price
        name = input("Name: ")
        price = int(input("Price: "))
        values = (price, name)
        cursor.execute ('UPDATE menu SET price = ? WHERE name = ?', values)
        connection.commit()
        # if cursor.rowcount == 0:
        #     print('ERROR! Dish does not exist yet.')
    elif choice == "4":
        # Delete Dish
        name = get_name(cursor)
        values = (name,)
        cursor.execute('DELETE FROM menu WHERE name = ?', values)
        connection.commit()
    print()

# Close the database connection before exiting
connection.close()