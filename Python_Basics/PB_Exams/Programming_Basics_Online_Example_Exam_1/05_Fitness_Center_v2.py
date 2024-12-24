def calculate_activity_stats(visitors):
    activity_counts = {
        'Back': 0,
        'Chest': 0,
        'Legs': 0,
        'Abs': 0,
        'Protein shake': 0,
        'Protein bar': 0,
    }

    for _ in range(visitors):
        activity = input()
        if activity in activity_counts:
            activity_counts[activity] += 1

    work_out_count = sum(activity_counts[activity] for activity in ['Back', 'Chest', 'Legs', 'Abs'])
    protein_count = sum(activity_counts[activity] for activity in ['Protein shake', 'Protein bar'])

    for activity, count in activity_counts.items():
        print(f'{count} - {activity.lower()}')

    print(f'{(work_out_count / visitors):.2%} - work out')
    print(f'{(protein_count / visitors):.2%} - protein')


c_visitors = int(input())

calculate_activity_stats(visitors=c_visitors)
