# Make several dictionaries, where the name of each dictionary is the
# name of a pet. In each dictionary, include the kind of animal and the
# owner’s name. Store these dictionaries in a list called pets. Next,
# loop through your list and as you do print everything you know about
# each pet.

rusty = {'type': 'dog', 'owner': 'dom'}
francis = {'type': 'cat', 'owner': 'richard'}
bhudda = {'type': 'turtle', 'owner': 'fred'}

pets = [{'rusty': rusty}, {'francis': francis}, {'bhudda': bhudda}]

for pet_item in pets:
    for pet_name in pet_item:
        print("\nName: " + pet_name.title())
        print("Type: " + pet_item[pet_name]['type'].title())
        print("Owner: " + pet_item[pet_name]['owner'].title())
