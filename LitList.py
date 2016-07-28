print "Welcome to LitList! Use me to keep track of all the books you currently own or wish to own."
which_lst = raw_input("Do you want to see your 'Owned Books' list or your 'To Buy' list? ")
owned_books = {}
buy_books = {}
def add_book(listName):
	author=raw_input("Enter the author of the book: \n")
	title=raw_input("Enter the title of the book: \n")
	if which_lst == "Owned Books":
		owned_books[author] = title
		print owned_books
	elif which_lst == "To Buy":
		buy_books[author] = title
		print buy_books
def order_books(listName, alpha_by):
	listName = raw_input("Do you want to see the complete list of your To Buy books or your Owned books? \n")
	if listName == "Owned Books":
		alpha_by = raw_input("And do you want to see the list alphebetized by author or by title? \n")
		if alpha_by == "title" or alpha_by == "Title":
			for key in sorted(owned_books):
				print "%s: %s" %(title, owned_books[author])
		elif alpha_by == "author" or alpha_by == "Author":
			for key in sorted(owned_books):
				print "%s: %s" %(author, owned_books[title])
	elif listName == "To Buy":
		alpha_by = raw_input("And do you want to see the list alphebetized by author or by title? \n")
		if alpha_by == "title" or alpha_by == "Title":
			for key in sorted(buy_books):
				print "%s: %s" %(title, buy_books[author])
		elif alpha_by == "author" or alpha_by == "Author":
			for key in sorted(buy_books):
				print "%s: %s" %(author, buy_books[title])


raw_input("")