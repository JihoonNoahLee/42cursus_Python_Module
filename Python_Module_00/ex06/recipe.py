# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/19 11:34:17 by jihoolee          #+#    #+#              #
#    Updated: 2023/04/09 15:13:05 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

cookbook = {
    'Sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10
    },
    'Cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60
    },
    'Salad': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15
    }
}


def print_all_recipe_name(cookbook: dict):
    index = 1

    print('This cookbook containes recipies for:')
    for name in cookbook:
        print(f'  {index}. {name}')
        index += 1


def print_detail(cookbook: dict, recipe_name: str):
    recipe_info = cookbook[recipe_name]

    print(f'Recipe for {recipe_name}:')
    print(f'  Ingredients list: {recipe_info["ingredients"]}')
    print(f'  To be eaten for {recipe_info["meal"]}.')
    print(f'  Takes {recipe_info["prep_time"]} minutes of cookiung.')


def delete_recipe(cookbook: dict, recipe_name: str):
    cookbook.pop(recipe_name)


def add_recipe(cookbook: dict):
    new_recipe_name = input('>>> Enter a name:\n')

    ingredients = []
    print('>>> Enter ingredients:')
    while (True):
        ingredient = input()
        if (ingredient == ''):
            break
        ingredients.append(ingredient)

    meal_type = input('>>> Enter a meal type:\n')
    try:
        prep_time = int(input('>>> Enter a preparation time:\n'))
    except Exception as e:
        raise AssertionError('Time must be provided as an integer')

    new_recipe = {'ingredients': ingredients,
                  'meal': meal_type,
                  'prep_time': prep_time}
    cookbook[new_recipe_name] = new_recipe


def cookbook_exec():
    global cookbook

    print('Welcome to the Python Cookbook !')
    print('''List of available option:
  1: Add a recipe
  2: Delete a recipe
  3: Print a recipe
  4: Print the cookbook
  5: Quit''')
    while (True):
        try:
            option = int(input('\nPlease select an option:\n>> '))
            print('')
            if (option == 1):
                add_recipe(cookbook)
            elif (option == 2):
                recipe_name = input(
                    '\nPlease enter a recipe name to remove:\n>>> ')
                delete_recipe(cookbook, recipe_name)
            elif (option == 3):
                recipe_name = input(
                    '\nPlease enter a recipe name to get its details:\n>>> ')
                print_detail(cookbook, recipe_name)
            elif (option == 4):
                print_all_recipe_name(cookbook)
            elif (option == 5):
                break
            else:
                raise ValueError
        except ValueError:
            print('Sorry, this option does not exist')
        except Exception as e:
            print(f'{type(e).__name__}: {e.args[0]}')
    print('Cookbook closed. Goodbye !')


def main():
    cookbook_exec()


if (__name__ == '__main__'):
    main()
