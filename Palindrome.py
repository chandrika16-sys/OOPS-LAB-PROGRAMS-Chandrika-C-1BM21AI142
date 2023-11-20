def is_palindrome(word):
  return word==word[::-1]

def get_palindrome(input_string):
  words=input_string.split()
  palindrome=[word for word  in words if is_palindrome(word)]
  return palindrome

string="Eble was a civic student but he saw a rotor placed on a level which was a good deed"
result=get_palindrome(string)
print(result)
