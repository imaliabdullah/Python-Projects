def arithmetic_arranger(problems, show_answers=False):
  if len(problems) > 5:
    return 'Error: Too many problems.'

  arranged_problems = [[], [], [], []]
  for problem in problems:
    operands = problem.split()
    if len(operands) != 3:
      return 'Error: Invalid problem.'
    try:
      num1 = int(operands[0])
      num2 = int(operands[2])
    except ValueError:
      return 'Error: Numbers must only contain digits.'
    operator = operands[1]
    if operator not in ['+', '-']:
      return "Error: Operator must be '+' or '-'."

    # Calculate the result
    if operator == '+':
      result = num1 + num2
    else:
      result = num1 - num2

    #Determine the maximum length

    max_len = max(len(str(num1)), len(str(num2))) + 2
    result_len = len(str(result))
    if result_len > max_len - 2:
      max_len = result_len + 2

    # add the operands and results
    arranged_problems[0].append(str(num1).rjust(max_len))
    arranged_problems[1].append(operator + ' ' + str(num2).rjust(max_len - 2))
    arranged_problems[2].append('-' * max_len)
    arranged_problems[3].append(
      str(result).rjust(max_len) if show_answers else '')

  arranged = '\n'.join(["    ".join(row) for row in arranged_problems])
  return arranged

problems = ['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40']

print(arithmetic_arranger(problems, show_answers=True))