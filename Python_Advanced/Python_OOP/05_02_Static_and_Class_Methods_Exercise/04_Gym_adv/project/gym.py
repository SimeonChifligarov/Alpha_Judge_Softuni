from typing import List
from project.customer import Customer
from project.trainer import Trainer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription


class Gym:
    """
    This class represents the whole gym with its customers, trainers, equipment, plans, and subscriptions.
    """

    def __init__(self) -> None:
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, new_customer: Customer) -> None:
        if new_customer not in self.customers:
            self.customers.append(new_customer)

    def add_trainer(self, new_trainer: Trainer) -> None:
        if new_trainer not in self.trainers:
            self.trainers.append(new_trainer)

    def add_equipment(self, new_equipment: Equipment) -> None:
        if new_equipment not in self.equipment:
            self.equipment.append(new_equipment)

    def add_plan(self, new_plan: ExercisePlan) -> None:
        if new_plan not in self.plans:
            self.plans.append(new_plan)

    def add_subscription(self, new_subscription: Subscription) -> None:
        if new_subscription not in self.subscriptions:
            self.subscriptions.append(new_subscription)

    def subscription_info(self, subscription_id: int) -> str:
        found_subscription = next((sub for sub in self.subscriptions if sub.id == subscription_id), None)
        if found_subscription is None:
            return ''

        found_customer = next((cust for cust in self.customers if cust.id == found_subscription.customer_id), None)
        found_trainer = next((trn for trn in self.trainers if trn.id == found_subscription.trainer_id), None)
        found_plan = next((pln for pln in self.plans if pln.id == found_subscription.exercise_id), None)
        found_equipment = next((eq for eq in self.equipment if eq.id == found_plan.equipment_id), None) if found_plan else None

        return '\n'.join(
            str(item) for item in [found_subscription, found_customer, found_trainer, found_equipment, found_plan] if item
        )
