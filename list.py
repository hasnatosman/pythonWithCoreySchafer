# list of courses........................................................................
courses = ['Math', 'CS', 'Physics', 'Chemistry', 'Biology']
print(courses)

# calling by index ......................................................................
print(courses[3])
print(courses[-1])
print(courses[:3])
print(courses[1:])

# add an item ...........................................................................
courses.append('Art')
print(courses)

# add on specific location...............................................................
courses.insert(2, 'Geometry')
print(courses)


# add multiple values....................................................................
new_courses = ['Bengali', 'English']
courses.insert(0, new_courses)
print(courses)
print(courses[0])

# add multiple courses end of the list...................................................
courses.extend(new_courses)
print(courses)
print(courses[1:])
courses.append(new_courses)
print(courses)

# remove some item from the list.........................................................
courses.remove(new_courses)
print(courses)
courses.remove(new_courses)
print(courses)
courses.extend(new_courses)
print(courses)
courses.remove('Bengali')
print(courses)
courses.pop()
print(courses)
popped = courses.pop()
print(popped)
print(courses)

# reverse the list.........................................................................
courses.reverse()
print(courses)

# sort the list..............................................................................
courses.sort()
print(courses)

num = [1, 2, 6, 4, 9, 7]
num.sort()
print(num)
num.reverse()
print(num)

new_num = sorted(num)
print(new_num)
print(min(num))
print(max(num))
print(sum(num))

# search index of any item.....................................................................
print(courses)
print(courses[6])
print(courses.index('Math'))

print('Math' in courses)
print('Mathe' in courses)

# printing each value using loop...............................................................

for item in courses:
    print(item)

for index, course in enumerate(courses):
    print(index, course)

print()

for index, course in enumerate(courses, start= 1):
    print(index, course)

# list to string using join method...........................................................

course_str = ','.join(courses)
print(course_str)


