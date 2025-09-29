#Develop a python-based Madlib based on a song of your choice. The program should collect at least 8 different pieces of information from the user and incorporate them into the song using names arguments.
def custom_song():
    name1 = input("Enter a name: ")
    name2 = input("Enter a second name: ")
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter a second noun: ")
    adjective1 = input("Enter an adjective: ")
    adjective2 = input("Enter a second adjective: ")
    verb1 = input("Enter a verb: ")
    verb2 = input("Enter a second verb: ")
    place1 = input("Enter a place: ")
    place2 = input("Enter a second place: ")

    song = f"""
    If there's something strange
    In your {place1}
    Who you gonna call? {name1}!
    If there's something weird
    And it don't look good
    Who you gonna call? {name2}!
    I ain't afraid of no {noun1}
    I ain't afraid of no {noun2}
    I ain't afraid of no {adjective1}
    I ain't afraid of no {adjective2}
    Who you gonna call? {name1}!
    If you're seeing things
    Running through your {place2}
    Who you gonna call? {name2}!
    I ain't afraid of no {verb1}
    I ain't afraid of no {verb2}
    Who you gonna call? {name1}!
    """
    print(song)
custom_song()