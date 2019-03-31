"""Making a class for recipe input.
Also a GUI integration for recipe class to fit into.Later**"""

# import webbrowser, pyautogui --> Just for other peoples sanity. imported in Recipe._nutrients()


# The idea for pyautogui is to allow automatic input to the url site to calculate for nutrient

# The idea for webbrowser is to allow for the insertion of the ingredients list into a nutrient calculator
# after each recipe is made. Allowing the _nutrient to return recipe nutrient values.
class Recipe(object):
    """Allows for a new recipe to be made and bundled neatly into its own file."""
    def __init__(self):
        """Starts the stuff. With __new__()"""
        self.author = input("Who created this dish?\n")
        print(f"Hello, {self.author}!")
        name = str(input('Please type the name of your dish:\n'))
        self.name = name
        self.ingredients = []
        self.prep = []
        self.y_amount = 0
        self.nutrient = {}
        self.instructions = []

    def __str__(self):
        """Will tie into the layout method and conversion table as well."""




    def opt_conver(self):
        """Will convert ingredient list measurments in all possible ways. Letting
        the user change the type of measurment if wanting to."""
        # See ConversionTable or Convers.py



    def recipe_file(self):
        """Creates the actual recipe in a file."""
        lists = [self.prep, self.ingredients, self.instructions]

        with open(self.name + '.txt', 'w') as file:
            file.write('Redneck Keto Kookin by ' + self.author + '\n')
            file.write(self.name + ' by ' + self.author)
            for p in lists:
                if p == []:
                    p = print(file=file)
                elif p == lists[0]:
                    for i in p:
                        prep = print('\n>' + i, file=file, sep='\n')
                elif p == lists[1]:
                    for i in p:
                        ingred = print('\n-' + i, file=file, sep='\n')
                elif p == lists[2]:
                    for i in p:
                        instruct = print('\n@' + i, file=file, sep='\n')


    def _prep(self):
        """Prompts user to input post-cooking items and methods to be used."""
        print("Is there any preparation needed for this recipe?")
        prep = input()
        if prep.lower() in 'yes':
            print("How many prep items will the recipe call for?(#'s Only)")
            pitem = int(input())
            while pitem != 0:
                pitem -= 1
                item = input("Prep Item: ")
                self.prep.append(item)
            return self.prep
        else:
            return self.prep

    def _ingredients(self):
        """All items needed for the meal along with calculations of quantity, and any conversions.
        Still needs functionality to seperate measurements and names."""
        print("How many ingredients total for the recipe?(Only #'s Accepted)")
        count = int(input())
        print("Type the amount and name of each ingredient, then press enter.")
        while count != 0:
            count -= 1
            print('Ingredient:')
            ingredient = input()
            self.ingredients.append(ingredient)

        return self.ingredients



    def _nutrients(self):
        """Going to use an online nutrient calculator via webbrowser and pyautogui."""
        # This method is going to take some time to learn pyautogui
        import webbrowser
        import pyautogui
        print("Do you want the recipe nutrients?")
        nutri = input()
        if nutri.lower() in 'yes':
            url = 'https://www.completefoods.co/diy/nutrient-profiles/calculator'
            webbrowser.open(url, new=1, autoraise=False)
            # Next, pyautogui will insert the correct information into the browser
        else:
            return print("You decided not to evaluate the nutrients of your dish.")
        return self.nutrient



    def _instruct(self):
        """Lets user input steps to create dish for recipe. As well as yield amount in int(people)."""
        print("How many people will this recipe feed? Or how many does it make?(#'s Only)")
        self.y_amount = int(input())
        print("Do you want the instructions to be in one paragraph or seperated?")
        form = input("Type PARA or SEP: ")
        if form.upper() == 'PARA':
            para = input('If you hit the enter key, no more items can be put in...\n')
            self.instructions.append(para)
        elif form.upper() == 'SEP':
            print("Hit the enter key without an instruction to exit instructions.")
            while True:
                print("Instruction:")
                bullet = input()
                self.instructions.append(bullet)
                if bullet == '':
                    self.instructions.remove(bullet)
                    break
        return self.instructions

def main():
    """Instance creation and method calls."""
    new = Recipe()
    new._prep()
    new._ingredients()
    new._instruct()
    print("The nutrient system is still in beta stages, but you can have a look.")
    new._nutrients()
    new.recipe_file()

main()
