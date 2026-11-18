def get_positive_integer(prompt):
    """Ask for a positive whole number."""
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                return number
            print("Please enter a number greater than zero.")
        except ValueError:
            print("Please enter a valid whole number.")


def get_mark(student_name, subject_number):
    """Ask for a mark from 0 to 100."""
    while True:
        try:
            mark = float(input(
                f"Enter {student_name}'s mark for subject {subject_number} (0-100): "
            ))
            if 0 <= mark <= 100:
                return mark
            print("The mark must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def calculate_average(marks):
    """Return the average of a list of marks."""
    return sum(marks) / len(marks)


def get_grade(average):
    """Return a letter grade based on the average."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def show_results(students):
    """Print each student's results and class summary."""
    print("\nStudent Results")
    print("-" * 40)

    averages = []

    for student in students:
        average = calculate_average(student["marks"])
        grade = get_grade(average)
        averages.append(average)

        print(
            f"{student['name']}: Average = {average:.2f}, Grade = {grade}"
        )

    class_average = sum(averages) / len(averages)
    top_student = students[averages.index(max(averages))]

    print("-" * 40)
    print(f"Class average: {class_average:.2f}")
    print(
        f"Top student: {top_student['name']} "
        f"({max(averages):.2f})"
    )


def main():
    print("Student Marks Analyzer")
    print("Enter marks from 0 to 100.")

    student_count = get_positive_integer("How many students? ")
    subject_count = get_positive_integer("How many subjects? ")

    students = []

    for student_number in range(1, student_count + 1):
        name = input(f"\nEnter the name of student {student_number}: ").strip()

        while not name:
            print("Name cannot be empty.")
            name = input(f"Enter the name of student {student_number}: ").strip()

        marks = []

        for subject_number in range(1, subject_count + 1):
            marks.append(get_mark(name, subject_number))

        students.append({
            "name": name,
            "marks": marks
        })

    show_results(students)


if __name__ == "__main__":
    main()