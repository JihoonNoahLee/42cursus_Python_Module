# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/06 16:28:16 by jihoolee          #+#    #+#              #
#    Updated: 2023/06/19 20:56:40 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Recipe:
    def __init__(self, name: str, cooking_lvl: int, cooking_time: int,
                 ingredients: list, description: str, recipe_type: str):
        '''TODO: description can be empty에 대해서 생각해보자'''
        if (not isinstance(name, str) or
                not isinstance(cooking_lvl, int) or
                not isinstance(cooking_time, int) or
                not isinstance(ingredients, list) or
                not isinstance(description, str) or
                not isinstance(recipe_type, str)):
            raise TypeError('invalid type of attribute')
        elif (cooking_lvl < 1 or cooking_lvl > 5):
            raise ValueError('cooking_lvl must be between 1 and 5')
        elif (cooking_time < 0):
            raise ValueError('cooking_time must be no negative')
        elif (not all(isinstance(ingredient, str)
                      for ingredient in ingredients)):
            raise TypeError('ingredients must be list of strings')
        elif (recipe_type not in ('starter', 'lunch', 'dessert')):
            raise ValueError(
                 'recipe_type must be one of "starter", "lunch", "dessert"'
            )
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients.copy()
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        '''Return the string to print with the recipe info'''
        txt = f'''
Recipe for {self.name}:
    | Cooking level: {self.cooking_lvl}
    | Cooking time: {self.cooking_time}
    | Ingredients: {', '.join(self.ingredients)}
    | Description: {self.description}
    | Recipe type: {self.recipe_type}
'''
        return txt
