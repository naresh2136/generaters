def square_numbers(nums):
    for i in nums:
        yield (i * i)


my_nums = square_numbers([1, 2, 3, 4, 5])

print(my_nums)

for i in my_nums:
    print(i)

'====================================='

# import mem_profile
import random
import time

names = ['john', 'corey', 'ajay', 'kiran', 'ramesh', 'vijay']
majors = ['math', 'engineering', 'computer', 'arts', 'business']


# print( 'Memory(before):{}mb'.format(mem_profile.memory_usage_resource()))

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }

        result.append(person)
    return result


def people_genretor(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }

        yield person


t1 = time.clock()
people = people_list(1000000)
t2 = time.clock()