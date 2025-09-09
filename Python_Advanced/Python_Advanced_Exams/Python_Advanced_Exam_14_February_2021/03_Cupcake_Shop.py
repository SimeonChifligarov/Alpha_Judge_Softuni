def stock_availability(inventory, action, *args):
    if action == "delivery":
        inventory.extend(args)
    elif action == "sell":
        if not args:
            if inventory:
                inventory.pop(0)
        elif isinstance(args[0], int):
            n = args[0]
            del inventory[:n]
        else:
            to_remove = set(args)
            inventory = [x for x in inventory if x not in to_remove]

    return inventory
