
#Problem 1: Post Format Validator

def is_valid_post_format(posts):
  
##Attempt 1
#   map = {'(': ')',
#          '{' : '}',
#          '[' : ']'}
  
#   brackets = list(posts)

#   removed_brackets = []

#   if posts[0] not in map or posts[-1] in map:
#     return False

#   while len(brackets) > 0:
#     r = brackets.pop()
#     if r not in map: #if you pop a closing bracket
#       removed_brackets.append(r)
#     else: #if you pop an opening bracket
#       if map.get(r) == removed_brackets[0]:
#         removed_brackets.pop(0)        
#       else:
#         return False

#   return True

##Attempt 2
    map = {'(': ')',
         '{' : '}',
         '[' : ']'}

    if len(posts) > 1:
        if posts[0] not in map or posts[-1] in map:
            return False
    else:
        return False
    
    l = list(posts)
    stack = []

    while len(l) > 0:
        removed = l.pop()
        if removed not in map:
            stack.append(removed)
        else:
            if len(stack) > 0:
                if map.get(removed) != stack.pop():
                    return False
            else:
                return False

    return True


#CHAT GPT Counterexamples:
print(is_valid_post_format("(()"))  
# expected: False
# your code returns: True
print(is_valid_post_format("((())"))  
# expected: False
# your code returns: True
print(is_valid_post_format("{[()]}("))  
# expected: False
# your code returns: True





# print(is_valid_post_format("(])"))
# print(is_valid_post_format("([)"))


# print(is_valid_post_format("()"))
# print(is_valid_post_format("()[]{}")) 
# print(is_valid_post_format("(]"))