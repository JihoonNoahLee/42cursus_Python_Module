# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/05 01:18:02 by jihoolee          #+#    #+#              #
#    Updated: 2023/06/19 21:22:29 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import datetime


class Book:
    def __init__(self, name: str):
        if (not isinstance(name, str)):
            raise TypeError('name must be string')
        elif (name == ''):
            raise ValueError('name must not be empty')
        self.name = name
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = {'starter': [], 'lunch': [], 'dessert': []}

    def get_recipe_by_name(self, name: str) -> None:
        '''Print a recipe with the name `name` and return the instance'''
        for recipe_type in self.recipes_list:
            for recipe in self.recipes_list[recipe_type]:
                if (recipe.name == name):
                    print(recipe)
                    return recipe
        print(f'No recipe with name "{name}"')
        return None

    def get_recipe_by_types(self, recipe_type: str) -> None:

