print "Welcome to LitList! Use me to keep track of all the books you currently own or wish to own."
new_book = raw_input("Would you like to look at your 'Owned Books' or your 'To Buy' list?: " )
owned_books = {}
buy_books = {}
def add_owned_book(title, author):
	owned_books[author] = title
	add_owned_book(raw_input("Enter the title of the book: \n"),raw_input("Enter the author of the book: \n"))
	print owned_books
def books_to_buy(title, author):
	buy_books[author] = title
	books_to_buy(raw_input("Enter the title of the book: \n"),raw_input("Enter the author of the book: \n"))
	print buy_books
def pick_list():
	if new_book == "Owned Books":
		add_owned_book(new_book)
	elif new_book == "To Buy":
		buy_books(new_book)
	else:
		print "Oops! Try again."
	pick_list(new_book)

raw_input("")