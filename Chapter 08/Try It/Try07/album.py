# Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name
# and an album title, and it should return a dictionary containing these
# two pieces of information. Use the function to make three dictionaries
# representing different albums. Print each return value to show that
# the dictionaries are storing the album information correctly.

# Add an optional parameter to make_album() that allows you to store the
# number of tracks on an album. If the calling line includes a value for
# the number of tracks, add that value to the album’s dictionary. Make
# at least one new function call that includes the number of tracks on
# an album.


def make_album(artist, title, num_tracks=''):
    """Returns a dictionary with information about an album"""
    album = {'artist': artist, 'title': title}
    if num_tracks:
        album['number of tracks'] = num_tracks

    return album


print(make_album('NIN', 'Fragile'))
print(make_album('Pink Floyd', 'Dark Side of the Moon'))

print(make_album('foo', 'bar', 27))
print(make_album('bizz', 'bazz', 12))
