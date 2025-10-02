def gather_credits(needed, *courses):
    enrolled = {}
    total = 0
    for name, credits in courses:
        if total >= needed:
            break
        if name in enrolled:
            continue
        enrolled[name] = credits
        total += credits

    if total >= needed:
        return f"Enrollment finished! Maximum credits: {total}.\nCourses: {', '.join(sorted(enrolled))}"
    return f"You need to enroll in more courses! You have to gather {needed - total} credits more."
