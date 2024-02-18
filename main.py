from time import sleep

class Library:
    def __init__(self):
        self.file_path = "books.txt"
        self.file = open(self.file_path, "a+",encoding="utf-8")
        
    def __del__(self):
        self.file.close()
    
    def list_books(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()
        print("Searching...")
        sleep(1)
        for line in lines:
            book_info = line.split(',')
            print(f"Title: {book_info[0]}, Author:{book_info[1]}")
        sleep(3)

    def add_book(self):
        title = input("Enter the book title: ").lower()
        author = input("Enter the book author: ").lower()
        try:
            release_year = int(input("Enter the release year: "))
            num_pages = int(input("Enter the number of pages: "))

            book_info = f"{title}, {author}, {release_year}, {num_pages},\n"
            self.file.write(book_info)
            self.file.flush()  
            print("Adding...")
            sleep(1)
            print("Book added successfully!")
            print("")
        except ValueError:
            print("""
                  Please enter numbers only!
                  """)

    def remove_book(self):
        
        title_to_remove = input("Enter the title of the book to remove: ").lower()

        #öncelikle dosyadaki veriler döngüde döndürüp listeye atmak için
        with open(self.file_path, 'a+', encoding='utf-8') as file:
            file.seek(0)
            lines = file.read().splitlines()
            up_list =[]
            for line in lines:
                book_info = line.split(',')
                up_list.append(book_info)
            logic_oparetor= len(up_list)
            

        #Tüm dosyları silip, kullanıcın silinmesini istediği kitap dışındaki kitapları eklemek için
        with open(self.file_path, 'w', encoding='utf-8') as file:
            for i in range(len(up_list)):
                if not up_list[i][0]== title_to_remove:
                    for number in range(4):
                        file.write((up_list[i][number]))
                        file.write(", ")
                    file.write("\n")
        
        #Kullanıcıya durum raporu vermek için
        with open(self.file_path, 'a+', encoding='utf-8') as file:
            file.seek(0)
            set_lines = file.read().splitlines()
            up_listed =[]
            for line in set_lines:
                book_info_updated = line.split(',')
                up_listed.append(book_info_updated)
            logic_Oparetor_last= len(up_listed)
        if logic_Oparetor_last==logic_oparetor:
            print("Searching...")
            sleep(1)
            print("The book was not found.")
        else:
            print("Searching...")
            sleep(1)
            print("Book removed successfully.")    
        

# Create an object named "lib" with "Library" class
lib = Library()

# Menu
while True:
    print("")
    print("----------------------- MENU -----------------------")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("q) Exit")

    choice = input("Enter your choice (1-2-3-q): ")
    print("-----------------------     -----------------------")
    print("")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == 'q':
        print("""
                      Goodbye!
              
        
-----------------------     -----------------------""")
        sleep(1)
        break
    else:
        print("Invalid choice. Please enter a number between 1 or 2 or 3 or q.")
