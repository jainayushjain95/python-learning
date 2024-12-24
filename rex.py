import re
text = "The agent's phone number is 875-09191-19"

# pattern = 'phone'
# print(re.search(pattern, text))
#
# pattern2 = 'phone dd'
# print(re.search(pattern2, text))

# pattern = 'phone'
# match = re.search(pattern, text)
# print(type(match))

# text = 'My phone number is 875-09191-29'
# phone = re.search(r'\d\d\d-\d\d\d\d\d-\d\d', text)
# print(phone.group())

# text = 'My phone number is 875-09191-29'
# # phone = re.search(r'\d{3}-\d{5}-\d{2}', text)
# # print(phone.group())
#
# phone_pattern = re.compile(r'(\d{3})-(\d{5})-(\d{2})')
# results = re.search(phone_pattern, text)
# print(results.group())
# print(results.group(1))
# print(results.group(2))
# print(results.group(3))

# result = re.search(r'cat|dog', 'The dog cat is here')
# print(result.group())

# result = re.findall(r'at', 'The cat in the hat sat there...')
# print(result)


result = re.findall(r'.at', 'The cat in the hat sat there...')
# print(result)

result = re.findall(r'..at', 'The cat in the hat sat there and went splat...')
# print(result)

result = re.findall(r'^\d', '1de 23ihuus h 6 dbds ihs6fd')
# print(result)

result = re.findall(r'\d$', '1de 23ihuus h 6 dbds ihs6fd3')
# print(result)

phrase = 'there are 2 numbers 34 inside 5 ciondastains this auidh d22 2d 22'
pattern = r'[^\d]'
# print(re.findall(pattern, phrase))

phrase = 'there are 2 numbers 34 inside 5 ciondastains this auidh d22 2d 22'
pattern = r'[^\d]+'
# print(re.findall(pattern, phrase))

phrase = 'This is a string! with exclamation marks'
pattern = r'[^! ]+'
pattern2 = r'[^!.? ]+'
# print(re.findall(pattern, phrase))
# print(re.findall(pattern2, phrase))

clean = re.findall(pattern, phrase)
# print(' '.join(clean))