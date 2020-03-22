def praise(marks):
    if len(marks) < 5:
        return "Bad"
    else:
        checkMin = 5
        for _ in marks:
            if _ > 79:
                checkMin -= 1
        if checkMin <= 0: return ("Good")
        else: return ("Bad")
