# Define a set that contains tuples. Each tuple should contain two strings:

# The name of an artist
# A song by that artist
# Make sure that some of the songs are from the band Nickelback.
# You can see a list of their greatest hits on Amazon.

# # Example set
# songs = {
#     ('Nickelback', 'How You Remind Me'),
#     ('Will.i.am', 'That Power'),
#     ('Miles Davis', 'Stella by Starlight'),
#     ('Nickelback', 'Animals')
# }
# Using a set comprehension, create a new set that contains all songs
# that were not performed by Nickelback.

hits = {
    ('Nickelback', 'How You Remind Me'),
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Dave Brubeck', 'Take Five'),
    ('Nickelback', 'Animals'),
    ('Fearless Flyers', 'Under the Sea')
}

real_hits = {(artist, title) for artist, title in hits if artist != 'Nickelback'}

print("The Hits:", hits)
print("\nThe REAL HITS:", real_hits)