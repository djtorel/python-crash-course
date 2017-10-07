# Start with your program from Exercise 8-7. Write a while loop that
# allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the
# dictionary that’s created. Be sure to include a quit value in the
# while loop.


def make_album(artist, title, num_tracks=''):
    """Returns a dictionary with information about an album"""
    album = {'artist': artist, 'title': title}
    if num_tracks:
        album['number of tracks'] = num_tracks

    return album


while True:
    print("\nPlease enter an artist and title for an album" +
          "\n(enter 'q' to quit)")
    artist = input("Artist: ")
    if artist == 'q':
        break
    title = input("Title: ")
    if title == 'q':
        break
    print("\n" + str(make_album(artist, title)))
