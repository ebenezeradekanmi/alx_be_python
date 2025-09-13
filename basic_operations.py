 number1 = 10
>>> number2 = 5
>>> addition = number1 + number2
>>> subtraction = number1 - number2
>>> multiplication = number1 * number2
>>> print(f"Addition of {number1} and \{number2} is {assition}")
Traceback (most recent call last):
  File "<python-input-18>", line 1, in <module>
    print(f"Addition of {number1} and {number2} is {assition}")
                                                    ^^^^^^^^
NameError: name 'assition' is not defined. Did you mean: 'addition'?
>>> print(f"Addition of {number1} and \{number2} is {addition}")
Addition of 10 and 5 is 15
>>> print(f"Subtraction of {number1} a\nd {number2} is {subtraction}")
Subtraction of 10 and 5 is 5
>>> print(f"Multiplication of {number1\} and {number2} is {multiplication}")
Multiplication of 10 and 5 is 50
>>>
