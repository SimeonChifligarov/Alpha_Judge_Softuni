def accommodate_new_pets(capacity, max_weight, *pets_data):
    accommodated_pets = {}
    result = []

    for pet_type, pet_weight in pets_data:
        if capacity <= 0:
            result.append("You did not manage to accommodate all pets!")
            break

        if pet_weight > max_weight:
            continue

        accommodated_pets[pet_type] = accommodated_pets.get(pet_type, 0) + 1
        capacity -= 1

    else:
        result.append(f"All pets are accommodated! Available capacity: {capacity}.")

    result.append("Accommodated pets:")
    for pet_type, count in sorted(accommodated_pets.items()):
        result.append(f"{pet_type}: {count}")

    return "\n".join(result)
