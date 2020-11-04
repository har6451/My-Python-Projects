# Mad Libs Story Generator

# Importing required libraries
import random
import copy

story = ("I was {} at the {}. " +
         "The other day when I heard {} come on the radio. " +
         "I was feeling really {} and I'm pretty sure I looked super {} because {} walked in and almost {}. " +
         "Seriously, she {} for close to {}! " + "\n" +
         "This time every year I {}. " +
         "All the time because I get really exciting thinking about holiday {}! " +
         "That's why I was at the {}: I was really hoping {} would come by and "
         "give me at least {} pieces of holiday {}! " + "\n" +
         "That didn't happen, but suddenly {} {} by in a huge {} on wheels dressed up as {}. " +
         "I know {} things happen around the holidays, but his didn't make any sense! " +
         "I picked up the phone call {}, but the phone turned into a big pile of {} " +
         "and dripped all the way down to my {}. " + "\n" +
         "Then my alarm clock went off for about {}. "
         "It was all a dream! I had a ton of {} before I went to sleep. " +
         "Maybe that's what gave me the crazy dream!")

# Creating a dictionary to lookup words by type
word_dict = {'verb_ing': ['eating', 'squatting', 'snoring'],
             'noun_place': ['Pub', 'Restaurant', 'Toilet'],
             'holiday_song': ['Christmas in Hollis', 'Last Christmas', 'Fairytale of New York'],
             'adjective': ['happy', 'excited', 'entertained', 'dumb', 'angry', 'foolish'],
             'friend_name': ['Rajan', 'Bhuwan', 'Oli', 'Trump'],
             'verb_ed': ['frightened', 'dressed', 'floated', 'gone'],
             'time': ['an hour', '2 hours', 'two and half hours'],
             'verb': ['hurl', 'waste', 'eat'],
             'plural_noun': ['penguins', 'parrots', 'peacocks'],
             'place_up_to': ['Kathmandu', 'Delhi', 'Tokyo'],
             'relative': ['dad', 'mom', 'brother', 'sister'],
             'noun': ['ship', 'plane', 'bus'],
             'number': ['12', '50', '25', '45'],
             'food_item': ['Biryani', 'Chicken Lollipop', 'Pizza'],
             'singer': ['Ariana Grande', 'Selena Gomez', 'Arijit Singh', 'Neha Kakkar'],
             'person': ['Hardik', 'Sachin', 'Gayle'],
             'messy_food': ['Dhokla', 'Edli', 'Dhosa'],
             'body_part': ['leg', 'ankle', 'hand', 'eye', 'mouth'],
             }


def get_word(type, local_dict):
    words = local_dict[type]
    count = len(words) - 1
    index = random.randint(0, count)
    return local_dict[type].pop(index)


def create_story():
    local_dict = copy.deepcopy(word_dict)
    return story.format(
        get_word('verb_ing', local_dict),
        get_word('noun_place', local_dict),
        get_word('holiday_song', local_dict),
        get_word('adjective', local_dict),
        get_word('adjective', local_dict),
        get_word('friend_name', local_dict),
        get_word('verb_ed', local_dict),
        get_word('verb_ed', local_dict),
        get_word('time', local_dict),
        get_word('verb', local_dict),
        get_word('plural_noun', local_dict),
        get_word('place_up_to', local_dict),
        get_word('relative', local_dict),
        get_word('number', local_dict),
        get_word('food_item', local_dict),
        get_word('relative', local_dict),
        get_word('verb_ed', local_dict),
        get_word('noun', local_dict),
        get_word('singer', local_dict),
        get_word('adjective', local_dict),
        get_word('person', local_dict),
        get_word('messy_food', local_dict),
        get_word('body_part', local_dict),
        get_word('time', local_dict),
        get_word('food_item', local_dict),
    )


print('Story 1 : ')
print(create_story())

print('Story 2 : ')
print(create_story())
