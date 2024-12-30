def calculate_total_time(seasons, episodes_per_season, episode_length):
    ad_time = episode_length * 0.2
    total_regular_episodes_time = (episode_length + ad_time) * episodes_per_season * seasons
    total_special_episodes_time = seasons * 10
    total_time = int(total_regular_episodes_time + total_special_episodes_time)
    return total_time


series_name = input()
season_count = int(input())
episode_count = int(input())
episode_duration = float(input())

total_time_needed = calculate_total_time(season_count, episode_count, episode_duration)
print(f'Total time needed to watch the {series_name} series is {total_time_needed} minutes.')
