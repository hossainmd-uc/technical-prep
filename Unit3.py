
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
# print(is_valid_post_format("(()"))  
# expected: False
# your code returns: True
# print(is_valid_post_format("((())"))  
# expected: False
# your code returns: True
# print(is_valid_post_format("{[()]}("))  
# expected: False
# your code returns: True


# print(is_valid_post_format("(])"))
# print(is_valid_post_format("([)"))

# print(is_valid_post_format("()"))
# print(is_valid_post_format("()[]{}")) 
# print(is_valid_post_format("(]"))

#Problem 2: Reverse User Comments Queue
'''
On your platform, comments on posts are displayed in the order they are received. 
However, for a special feature, you need to reverse the order of comments before 
displaying them. Given a queue of comments represented as a list of strings, 
reverse the order using a stack.
'''
from collections import deque

def reverse_comments_queue(comments):
    comments_q = deque(comments)
    stack = []

    while comments_q:
        stack.append(comments_q.popleft())

    res = []
    while stack:
        res.append(stack.pop())
    
    return res

# print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))
# print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))


#Problem 3: Check Symmetry in Post Titles
'''
As part of a new feature on your social media platform, you want to 
highlight post titles that are symmetrical, meaning they read the 
same forwards and backwards when ignoring spaces, punctuation, and 
case. Given a post title as a string, use a new algorithmic technique
the two-pointer method to determine if the title is symmetrical.
'''
import string
def is_symmetrical_title(title):
    '''
    Docstring for is_symmetrical_title
    
    :param title: str
    '''
    title = title.strip() #Edge

    start = 0
    end = len(title)-1
    
    omit = [' '] + list(string.punctuation)

    while start < end:
        if (title[start] in omit or title[end] in omit ):
            if title[start] in omit:
                start+=1
            else:
                end-=1
            continue

        if (title[start].lower() != title[end].lower()):
            print(f"diff: '{title[start]}' '{title[end]}'")
            return False
        
        print('the same: ', title[start], title[end])    
      
        start+=1
        end -=1

    return True

# print(is_symmetrical_title("A Santa at NASA"))
# print(is_symmetrical_title("Social Media")) 

'''
You track your daily engagement rates as a list of integers, sorted in 
non-decreasing order. To analyze the impact of certain strategies, 
you decide to square each engagement rate and then sort the results 
in non-decreasing order.

Given an integer array engagements sorted in non-decreasing order, return
an array of the squares of each number sorted in non-decreasing order.

Your Task:

    Read through the existing solution and add comments so that everyone 
    in your pod understands how it works.
    Modify the solution below to use the two-pointer technique.

'''

def engagement_boost(engagements):
    '''
    Docstring for engagement_boost
    
    :param engagements: list[int]
    '''
    squared_engagements = []
    
    for i in range(len(engagements)):
        squared_engagement = engagements[i] * engagements[i]
        squared_engagements.append((squared_engagement, i))
    
    squared_engagements.sort(reverse=True) #descending order sort
     
    print(squared_engagements)
    
    result = [0] * len(engagements)
    position = len(engagements) - 1
    
    for square, _ in squared_engagements:
        result[position] = square
        position -= 1
    
    return result


def engagement_boost_2(engagements):
    '''
    Docstring for engagement_boost
    
    :param engagements: list[int]
    '''
    res = [0] * len(engagements)
    pos = len(engagements)-1
    
    start = 0
    end = len(engagements)-1
    
    while start <= end:
        t1 = (engagements[start])**2
        t2 = (engagements[end])**2
        if t1 > t2:
            res[pos] = t1
            start+=1
        else:
            res[pos] = t2
            end-=1
        pos-=1

    
    return res
        
        
        
    
print(engagement_boost_2([-4, -1, 0, 3, 10]))
print(engagement_boost_2([-7, -3, 2, 3, 11]))




