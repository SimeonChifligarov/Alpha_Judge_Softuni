def students_credits(*courses):
    course_results = {}
    total_credits = 0
    for course in courses:
        name, credits, max_points, diyan_points = course.split("-")
        credits, max_points, diyan_points = int(credits), int(max_points), int(diyan_points)
        achieved = credits * diyan_points / max_points
        course_results[name] = achieved
        total_credits += achieved
    result = []
    if total_credits >= 240:
        result.append(f"Diyan gets a diploma with {total_credits:.1f} credits.")
    else:
        result.append(f"Diyan needs {240 - total_credits:.1f} credits more for a diploma.")
    for name, cr in sorted(course_results.items(), key=lambda x: -x[1]):
        result.append(f"{name} - {cr:.1f}")

    return "\n".join(result)
