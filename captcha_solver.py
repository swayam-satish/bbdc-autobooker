class CaptchaSolver:
    def __init__(self, string):
        self.mylist = []
        self.string = string
        self.new_string = ""

    def two_captcha(self):
        self.mylist.append(self.string)

    def all_caps(self):
        for char in self.string:
            if char.isalpha():
                char = char.upper()
            self.new_string += char

        self.mylist.append(self.new_string)

    def one_letter(self):
        for n in range(0, 4):
            test = ""
            if self.string[n].isalpha():
                new_char = self.string[n].upper()
            else:
                new_char = None
            for char in self.string:
                if char.isalpha():
                    if char.upper() == new_char:
                        char = new_char

                test += char
            self.mylist.append(test)

    def consecutive_letters(self):
        for n in range(0, 3):
            test = ""
            if self.string[n].isalpha():
                first_new_character = self.string[n].upper()
            else:
                first_new_character = None
            if self.string[n + 1].isalpha():
                second_new_character = self.string[n + 1].upper()
            else:
                second_new_character = None
            for char in self.string:
                if char.isalpha():
                    if char.upper() == first_new_character:
                        char = first_new_character
                    elif char.upper() == second_new_character:
                        char = second_new_character

                test += char
            self.mylist.append(test)

    def alternate_letters(self):
        for n in range(0, 2):
            test = ""
            if self.string[n].isalpha():
                first_new_char = self.string[n].upper()
            else:
                first_new_char = None
            if self.string[n + 2].isalpha():
                second_new_char = self.string[n + 2].upper()
            else:
                second_new_char = None
            for char in self.string:
                if char.isalpha():
                    if char.upper() == first_new_char:
                        char = first_new_char
                    elif char.upper() == second_new_char:
                        char = second_new_char

                test += char
            self.mylist.append(test)

    def two_in_between(self):
        for n in range(0, 2):
            test = ""
            if self.string[n].isalpha():
                first_new_char = self.string[n].upper()
            else:
                first_new_char = None
            if self.string[n + 3].isalpha():
                second_new_char = self.string[n + 3].upper()
            else:
                second_new_char = None
            for char in self.string:
                if char.isalpha():
                    if char.upper() == first_new_char:
                        char = first_new_char
                    elif char.upper() == second_new_char:
                        char = second_new_char

                test += char
            self.mylist.append(test)

    def triplets(self):
        for n in range(0, 3):
            test = ""
            if self.string[n].isalpha():
                first_new_char = self.string[n].upper()
            else:
                first_new_char = None
            if self.string[n + 1].isalpha():
                second_new_char = self.string[n + 1].upper()
            else:
                second_new_char = None
            if self.string[n + 2].isalpha():
                third_new_char = self.string[n + 2].upper()
            else:
                third_new_char = None
            for char in self.string:
                if char.isalpha():
                    if char.upper() == first_new_char:
                        char = first_new_char
                    elif char.upper() == second_new_char:
                        char = second_new_char
                    elif char.upper() == third_new_char:
                        char = third_new_char

                test += char
            self.mylist.append(test)

    def two_same_letters(self):
        initial_list = [char for char in self.string]
        duplicates = []
        for letter in self.string:
            if self.string.count(letter) > 1 and letter not in duplicates:
                duplicates.append(letter)
        try:
            for char in duplicates:
                position_1 = initial_list.index(char)
                initial_list.remove(initial_list[position_1])
                position_2 = initial_list.index(char) + 1

                print(f"{char} index is {position_1} and {position_2}")
                first_half, second_half = self.string.split(self.string[position_2 - 1])
                print(first_half)
                print(second_half)
                modified_first_half = first_half.replace(first_half[position_1], first_half[position_1].upper())
                modified_second_half = second_half.replace(second_half[0], second_half[0].upper())
                answer_1 = modified_first_half + self.string[position_2 - 1] + second_half
                answer_2 = first_half + self.string[position_2 - 1] + modified_second_half
                self.mylist.append(answer_1)
                self.mylist.append(answer_2)
        except ValueError:
            pass

    def final_list(self):
        mylist = list(dict.fromkeys(self.mylist))
        return mylist
