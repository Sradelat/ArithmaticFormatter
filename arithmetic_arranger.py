def arithmetic_arranger(problems, solutions=False):
    import re
    if problems[5:]:
        return "Error: Too many problems."

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    for problem in problems:

        if re.search("[a-z]", problem):
            return "Error: Numbers must only contain digits."
        if re.search("[/]", problem) or re.search("[*]", problem):
            return "Error: Operator must be '+' or '-'."

        num1 = problem.split(" ")[0]
        op = problem.split(" ")[1]
        num2 = problem.split(" ")[2]
        mlen = max(len(num1), len(num2)) + 2

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        if op == "+":
            solution = int(num1) + int(num2)
        else:
            solution = int(num1) - int(num2)

        line1 = line1 + str(num1).rjust(mlen) + "    "
        line2 = line2 + op + str(num2).rjust(mlen - 1) + "    "
        line3 = line3 + "-".rjust(mlen, "-") + "    "
        line4 = line4 + str(solution).rjust(mlen) + "    "
    if solutions:
        arranged_problems = line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip() + "\n" + line4.rstrip()
    else:
        arranged_problems = line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip()

    return arranged_problems
