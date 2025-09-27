def softuni_students(*args, **kwargs):
    students = {}
    for cid, username in args:
        students[username] = cid
    valid = []
    invalid = []
    for username, cid in sorted(students.items()):
        if cid in kwargs:
            valid.append(f"*** A student with the username {username} has successfully finished the course {kwargs[cid]}!")
        else:
            invalid.append(username)
    result = []
    result.extend(valid)
    if invalid:
        result.append("!!! Invalid course students: " + ", ".join(sorted(invalid)))

    return "\n".join(result)
