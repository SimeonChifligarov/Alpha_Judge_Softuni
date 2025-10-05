def cookbook(*args):
    cuisines = {}
    for recipe, cuisine, ingredients in args:
        cuisines.setdefault(cuisine, []).append((recipe, ingredients))
    sorted_cuisines = sorted(
        cuisines.items(),
        key=lambda x: (-len(x[1]), x[0])
    )
    result = []
    for cuisine, recipes in sorted_cuisines:
        result.append(f"{cuisine} cuisine contains {len(recipes)} recipes:")
        for recipe, ingredients in sorted(recipes, key=lambda x: x[0]):
            result.append(f"  * {recipe} -> Ingredients: {', '.join(ingredients)}")

    return "\n".join(result)
