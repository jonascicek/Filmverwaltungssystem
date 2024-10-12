# Import from mysql_connection

from test_connection import create_connection

# Function to add a movie

def add_movie(title, director, genre, releaseyear, rating):
    connection = create_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO Filme (title, director, genre, releaseyear, rating) VALUES (%s, %s, %s, %s, %s)"
    values = (title, director, genre, releaseyear, rating)
    cursor.execute(sql, values)
    connection.commit()
    cursor.close()
    connection.close()

# Function to delete a movie

def delete_movie():
    connection = create_connection()
    cursor = connection.cursor()
    movie_name = input("Which movie do you wanna delete from your list? Please enter the name.\n")
    cursor.execute('''DELETE FROM Filme WHERE title = %s''', (movie_name,))
    connection.commit()
    print(f"The movie {movie_name} removed from your list.")
    cursor.close()
    connection.close()

# Function to show movies

def show_movies():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Filme')
    filmlist = cursor.fetchall()
    for i in filmlist:
        print(f"Id: {i[0]}, Title: {i[1]}, Director: {i[2]}, Genre: {i[3]}, Release Year: {i[4]}, Rating: {i[5]}")
    cursor.close()
    connection.close()

#Function to update movies

def update_movie():
    while True:
        show_movies()
        movie_id =  input("Which movie do you want to update?\nPlease enter the movie number.\n")
        print("----- Update Movies -----")
        print("1. Title")
        print("2. Director")
        print("3. Genre")
        print("4. Release Year")
        print("5. Rating")
        print("6. All")
        print("7. Exit")
        print("-----")

        choice = input("Which would you like to update?")

        if choice == "1":
                connection = create_connection()
                cursor = connection.cursor()
                new_title = input("How you wanna call the movie?\n")
                cursor.execute('''UPDATE Filme SET title = %s WHERE id = %s''', (new_title, movie_id))
                connection.commit()
                print(f"The new title from movie with the  ID {movie_id} is {new_title}.")
                cursor.close()
                connection.close()

        elif choice == "2":
                connection = create_connection()
                cursor = connection.cursor()
                new_director = input("Please type in new director.\n")
                cursor.execute('''UPDATE Filme SET director = %s WHERE id = %s''', (new_director, movie_id))
                connection.commit()
                print(f"The new director with the ID {movie_id} is {new_director}.")
                cursor.close()
                connection.close()

        elif choice == "3":
                connection = create_connection()
                cursor = connection.cursor()
                new_genre = input("Please type in new genre.\n")
                cursor.execute('''UPDATE Filme SET genre = %s WHERE id = %s''', (new_genre, movie_id))
                connection.commit()
                print(f"The new genre with the ID {movie_id} is {new_genre}.")
                cursor.close()
                connection.close()

        elif choice == "4":
                connection = create_connection()
                cursor = connection.cursor()
                new_releaseyear = int(input("Please type in new release year.\n"))
                cursor.execute('''UPDATE Filme SET releaseyear = %s WHERE id = %s''', (new_releaseyear, movie_id))
                connection.commit()
                print(f"The new release year with the ID {movie_id} is {new_releaseyear}.")
                cursor.close()
                connection.close()

        elif choice == "5":
                connection = create_connection()
                cursor = connection.cursor()
                new_rating = float(input("Please type in new rating.\n"))
                cursor.execute('''UPDATE Filme SET rating = %s WHERE id = %s''', (new_rating, movie_id))
                connection.commit()
                print(f"The new rating with the ID {movie_id} is {new_rating}.")
                cursor.close()
                connection.close()

        elif choice == "6":
                connection = create_connection()
                cursor = connection.cursor()
                new_title = input("Please type in new movie title.\n")
                new_director = input("Please type in new director.\n")
                new_genre = input("Please type in new genre \n")
                new_releaseyear = int(input("Please type in new release year.\n"))
                new_rating = float(input("How is your rating?\n"))
                cursor.execute('''UPDATE movies SET title = %s, director = %s, genre = %s, releaseyear = %s, rating = %s WHERE id = %s''', (new_title, new_director, new_genre, new_releaseyear, new_rating, movie_id))
                connection.commit()
                cursor.close()
                connection.close()

        elif choice == "7":
                print(f"Update function closed.")
                break

# Function to search for a movie

def search_movies():
    criteria = input("For wich criteria do you wanna search?\n")
    value = input("For what do you wanna search?\n")
    connection = create_connection()
    cursor = connection.cursor()
    sql = f"SELECT * FROM Filme WHERE {criteria} = %s"
    cursor.execute(sql, (value,))
    result = cursor.fetchall()
    for i in result:
        print(f"Title: {i[1]}, Director: {i[2]}, Genre: {i[3]}, Releaseyear: {i[4]}, Rating: {i[5]}")
    cursor.close()
    connection.close()


# Adding main function

def main():
    while True:
        print("---- Moviemanagementsystem ----")
        print("1. Add movie")
        print("2. Delete movie")
        print("3. Show movies")
        print("4. Update movie")
        print("5. Search for movie")
        print("6. Close program")

        choice = input("Please choose (1,2,3,4,5 or 6): ")

        if choice == "1":
            print("Please write down the new movie")
            title = input("title: ")
            director = input("director: ")
            genre = input("genre: ")
            releaseyear = input("releaseyear: ")
            rating = input("rating: ")
            add_movie(title, director, genre, releaseyear, rating)

        elif choice == "2":
            delete_movie()

        elif choice == "3":
            show_movies()

        elif choice == "4":
            update_movie()

        elif choice == "5":
            search_movies()
        
        elif choice == "6":
            print("Closing program. Have a good day!")
            break
        
        else:
            print("False entry! Please choose 1,2,3,4,5 or 6")

if __name__ == "__main__":
    main()
