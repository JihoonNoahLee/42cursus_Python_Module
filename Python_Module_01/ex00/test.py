# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/06 16:30:28 by jihoolee          #+#    #+#              #
#    Updated: 2023/06/19 21:21:06 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from book import Book
from recipe import Recipe


def test_recipe() -> None:
    # Test case 1 (Valid recipe)
    recipe1 = Recipe(
        name="Pasta Carbonara",
        cooking_lvl=3,
        cooking_time=30,
        ingredients=["spaghetti", "bacon", "eggs", "parmesan cheese"],
        description="Classic Italian pasta dish",
        recipe_type="lunch"
    )
    print(recipe1)

    # Test case 2 (Invalid type for name)
    try:
        invalid_name_recipe = Recipe(
            name=123,  # Invalid name (not a string)
            cooking_lvl=2,
            cooking_time=40,
            ingredients=["ingredient1", "ingredient2"],
            description="Invalid name recipe",
            recipe_type="starter"
        )
    except TypeError as e:
        print(f"Error: {str(e)}")

    # Test case 3 (Invalid type for cooking_lvl)
    try:
        invalid_cooking_lvl_recipe = Recipe(
            name="Invalid Cooking Level Recipe",
            cooking_lvl="2",  # Invalid cooking_lvl (not an integer)
            cooking_time=40,
            ingredients=["ingredient1", "ingredient2"],
            description="Invalid cooking_lvl recipe",
            recipe_type="starter"
        )
    except TypeError as e:
        print(f"Error: {str(e)}")

    # Test case 4 (Invalid value for cooking_lvl)
    try:
        invalid_value_cooking_lvl_recipe = Recipe(
            name="Invalid Value Cooking Level Recipe",
            cooking_lvl=6,  # Invalid cooking_lvl (out of range)
            cooking_time=40,
            ingredients=["ingredient1", "ingredient2"],
            description="Invalid value cooking_lvl recipe",
            recipe_type="starter"
        )
    except ValueError as e:
        print(f"Error: {str(e)}")

    # Test case 5 (Invalid type for cooking_time)
    try:
        invalid_cooking_time_recipe = Recipe(
            name="Invalid Cooking Time Recipe",
            cooking_lvl=2,
            cooking_time="40",  # Invalid cooking_time (not an integer)
            ingredients=["ingredient1", "ingredient2"],
            description="Invalid cooking_time recipe",
            recipe_type="starter"
        )
    except TypeError as e:
        print(f"Error: {str(e)}")

    # Test case 6 (Invalid value for cooking_time)
    try:
        invalid_value_cooking_time_recipe = Recipe(
            name="Invalid Value Cooking Time Recipe",
            cooking_lvl=2,
            cooking_time=-10,  # Invalid cooking_time (negative value)
            ingredients=["ingredient1", "ingredient2"],
            description="Invalid value cooking_time recipe",
            recipe_type="starter"
        )
    except ValueError as e:
        print(f"Error: {str(e)}")

    # Test case 7 (Invalid type for ingredients)
    try:
        invalid_ingredients_recipe = Recipe(
            name="Invalid Ingredients Recipe",
            cooking_lvl=2,
            cooking_time=40,
            ingredients="ingredient1",  # Invalid ingredients (not a list)
            description="Invalid ingredients recipe",
            recipe_type="starter"
        )
    except TypeError as e:
        print(f"Error: {str(e)}")

    # Test case 8 (Invalid value in ingredients)
    try:
        invalid_value_ingredients_recipe = Recipe(
            name="Invalid Value Ingredients Recipe",
            cooking_lvl=2,
            cooking_time=40,
            ingredients=["ingredient1", 123],
            # Invalid ingredient (not a string)
            description="Invalid value ingredients recipe",
            recipe_type="starter"
        )
    except TypeError as e:
        print(f"Error: {str(e)}")

    # Test case 9 (Invalid type for description)
    try:
        invalid_description_recipe = Recipe(
            name="Invalid Description Recipe",
            cooking_lvl=2,
            cooking_time=40,
            ingredients=["ingredient1", "ingredient2"],
            description=123,  # Invalid description (not a string)
            recipe_type="starter"
        )
    except TypeError as e:
        print(f"Error: {str(e)}")

    # Test case 10 (Valid recipe with empty description)
    recipe2 = Recipe(
        name="Empty Description Recipe",
        cooking_lvl=1,
        cooking_time=20,
        ingredients=["ingredient1", "ingredient2"],
        description="",  # Empty description
        recipe_type="lunch"
    )
    print(recipe2)

    # Test case 11 (Invalid type for recipe_type)
    try:
        invalid_recipe_type_recipe = Recipe(
            name="Invalid Recipe Type Recipe",
            cooking_lvl=2,
            cooking_time=40,
            ingredients=["ingredient1", "ingredient2"],
            description="Invalid recipe_type recipe",
            recipe_type=123  # Invalid recipe_type (not a string)
        )
    except TypeError as e:
        print(f"Error: {str(e)}")

    # Test case 12 (Invalid value for recipe_type)
    try:
        invalid_value_recipe_type_recipe = Recipe(
            name="Invalid Value Recipe Type Recipe",
            cooking_lvl=2,
            cooking_time=40,
            ingredients=["ingredient1", "ingredient2"],
            description="Invalid value recipe_type recipe",
            recipe_type="dinner"
            # Invalid recipe_type (not in ['starter', 'lunch', 'dessert'])
        )
    except ValueError as e:
        print(f"Error: {str(e)}")


def main():
    test_recipe()


if (__name__ == '__main__'):
    main()
