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
        if self.ordered:
            return f'Pizza {self.name} already prepared, and we can\'t make any changes!'
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
        else:
            self.ingredients[ingredient] = quantity
        self.price += quantity * price_per_quantity

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float) -> str | None:
        if self.ordered:
            return f'Pizza {self.name} already prepared, and we can\'t make any changes!'
        if ingredient not in self.ingredients:
            return f'Wrong ingredient selected! We do not use {ingredient} in {self.name}!'
        if quantity > self.ingredients[ingredient]:
            return f'Please check again the desired quantity of {ingredient}!'
        self.ingredients[ingredient] -= quantity
        self.price -= quantity * price_per_quantity

    def make_order(self) -> str:
        if self.ordered:
            return f'Pizza {self.name} already prepared, and we can\'t make any changes!'
        self.ordered = True
        ingredient_details = ', '.join([f'{item}: {qty}' for item, qty in self.ingredients.items()])
        return (
            f'You\'ve ordered pizza {self.name} prepared with {ingredient_details} and the price will be {self.price}lv.'  # noqa: E501
        )

    def __str__(self) -> str:
        return f'{self.name} pizza with ingredients: {self.ingredients}'

    def __repr__(self) -> str:
        return f'PizzaDelivery(name={self.name!r}, price={self.price!r}, ingredients={self.ingredients!r}, ordered={self.ordered!r})'  # noqa: E501

    # def __repr__(self) -> str:
    #     cls_name = self.__class__.__name__
    #     attrs = ', '.join(f'{k}={v!r}' for k, v in self.__dict__.items())
    #     return f'{cls_name}({attrs})'

    def __eq__(self, other: object) -> bool:
        if isinstance(other, PizzaDelivery):
            return self.name == other.name and self.ingredients == other.ingredients
        return NotImplemented

    def __gt__(self, other: object) -> bool:
        if isinstance(other, PizzaDelivery):
            return self.price > other.price
        return NotImplemented

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
#     print(str(pizza_order))
#     print(repr(pizza_order))
#     another_pizza = PizzaDelivery(name='Pepperoni', price=12.5, ingredients={'pepperoni': 3, 'cheese': 2})
#     print(pizza_order == another_pizza)
#     print(pizza_order > another_pizza)
