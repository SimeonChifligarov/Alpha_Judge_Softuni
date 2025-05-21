class PizzaDelivery:
    """
    This class is for pizza delivery orders. It manages ingredients, price, and finalization.

    Args:
        name (str): The name of the pizza
        price (float): The starting price of the pizza
        ingredients (dict): The ingredients with their quantities
    """

    def __init__(self, name: str, price: float, ingredients: dict) -> None:
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float) -> None | str:
        """
        This method adds more of an existing or new ingredient and updates price.

        Args:
            ingredient (str): Name of the ingredient
            quantity (int): How much to add
            price_per_quantity (float): Price per unit
        """
        if self.ordered:
            return f'Pizza {self.name} already prepared, and we can\'t make any changes!'

        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
        else:
            self.ingredients[ingredient] = quantity

        self.price += quantity * price_per_quantity

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float) -> str | None:
        """
        This method removes some quantity of an ingredient and adjusts price.

        Args:
            ingredient (str): Name of the ingredient
            quantity (int): How much to remove
            price_per_quantity (float): Price per unit

        Returns:
            str | None: Message on error or None on success
        """
        if self.ordered:
            return f'Pizza {self.name} already prepared, and we can\'t make any changes!'

        if ingredient not in self.ingredients:
            return f'Wrong ingredient selected! We do not use {ingredient} in {self.name}!'

        if quantity > self.ingredients[ingredient]:
            return f'Please check again the desired quantity of {ingredient}!'

        self.ingredients[ingredient] -= quantity
        self.price -= quantity * price_per_quantity

    def make_order(self) -> str:
        """
        This method finalizes the order.

        Returns:
            str: Final order message
        """
        if self.ordered:
            return f'Pizza {self.name} already prepared, and we can\'t make any changes!'

        self.ordered = True
        ingredient_details = ', '.join([f'{item}: {qty}' for item, qty in self.ingredients.items()])
        return f'You\'ve ordered pizza {self.name} prepared with {ingredient_details} and the price will be {self.price}lv.'

# if __name__ == '__main__':
#     pizza_name = 'Margarita'
#     pizza_price = 10.0
#     pizza_ingredients = {'cheese': 2, 'tomato': 3}
#     pizza_order = PizzaDelivery(name=pizza_name, price=pizza_price, ingredients=pizza_ingredients)
#     print(pizza_order.add_extra(ingredient='cheese', quantity=1, price_per_quantity=1.5))
#     print(pizza_order.add_extra(ingredient='basil', quantity=2, price_per_quantity=0.5))
#     print(pizza_order.remove_ingredient(ingredient='tomato', quantity=1, price_per_quantity=0.8))
#     print(pizza_order.make_order())
#     print(pizza_order.add_extra(ingredient='olives', quantity=2, price_per_quantity=0.7))
#     print(pizza_order.remove_ingredient(ingredient='basil', quantity=1, price_per_quantity=0.5))
