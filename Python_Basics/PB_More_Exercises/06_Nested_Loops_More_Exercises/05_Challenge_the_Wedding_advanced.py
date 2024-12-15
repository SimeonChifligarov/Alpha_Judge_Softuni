def dinner_date(men_count, women_count, max_tables):
    table_count = 0
    result = []
    for man in range(1, men_count + 1):
        for woman in range(1, women_count + 1):
            if table_count >= max_tables:
                return result

            result.append(f'({man} <-> {woman})')
            table_count += 1

    return result


m_count = int(input())
w_count = int(input())
maximum_tables = int(input())

dinner = dinner_date(men_count=m_count, women_count=w_count, max_tables=maximum_tables)
print(' '.join(dinner))
