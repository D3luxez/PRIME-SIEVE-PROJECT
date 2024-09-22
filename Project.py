def is_prime(num):
  """
  Checks if a number is prime.

  Args:
      num: The number to check.

  Returns:
      True if the number is prime, False otherwise.
  """
  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True


for i in range(10, 100):
  if is_prime(i):
    print(i)