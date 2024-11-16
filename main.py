with open("books/frankenstein.txt") as f:
    file_contents = f.read()


    words = len(file_contents.split())

    contentsLower = file_contents.lower()
    letter_counts = {}
    letters = list(contentsLower)

    for letter in letters:
        if letter.isalpha():
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
            letter_counts = letter_counts


    letter_list = []  # Create empty list first
    for letter, count in letter_counts.items():
        new_dict = {"name": letter, "num": count}
    # Add it to our list
        letter_list.append(new_dict)
    # What should we do in here?
    def sort_on(letter_list):
        return letter_list["num"]
    letter_list.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document\n")  # \n adds a blank line

    for item in letter_list:
    # Each item is a dictionary with 'name' and 'num' keys
        letter = item["name"]
        count = item["num"]
        print(f"The '{letter}' character was found {count} times")

    # Print the footer
    print("--- End report ---")