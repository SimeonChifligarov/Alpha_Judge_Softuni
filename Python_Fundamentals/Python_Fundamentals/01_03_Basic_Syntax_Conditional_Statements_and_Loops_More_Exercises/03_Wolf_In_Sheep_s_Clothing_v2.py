def warn_the_sheep(queue):
    animals = queue.split(', ')
    wolf_index = animals.index('wolf')
    if wolf_index == len(animals) - 1:
        return 'Please go away and stop eating my sheep'
    else:
        sheep_position = len(animals) - wolf_index - 1
        return f'Oi! Sheep number {sheep_position}! You are about to be eaten by a wolf!'


if __name__ == '__main__':
    input_queue = input()
    result = warn_the_sheep(queue=input_queue)
    print(result)
