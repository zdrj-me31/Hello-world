opened_file = open('AppleStore.csv', encoding = 'utf-8')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

# Creating some list to combine ratings
games_ratings = []
non_games_ratings = []
non_free_apps_rating = []
for row in apps_data[1:]:
    rating = float(row[8])
    genre = row[12]
    if genre == 'Games':
        games_ratings.append(rating)
    elif genre != 'Games':
        non_games_ratings.append(rating)
avg_rating_games = round(sum(games_ratings) / len(games_ratings),2)
avg_rating_non_games = round(sum(non_games_ratings) / len(non_games_ratings),2)
for row in apps_data[1:]:
    rating = float(row[8])
    price = float(row[5])
    if price != 0.0:
        non_free_apps_rating.append(rating)
avg_rating_non_free = round(sum(non_free_apps_rating)/ len(non_free_apps_rating))
print('Paid apps rates are better than free ones.' if avg_rating_non_free > 3.38 else 'Free apps are better.')

# create list for free games rating
free_games_ratings = []
for row in apps_data[1:]:
    rating = float(row[8])
    price = float(row[5])
    genre = row[12]
    if genre == 'Games' and price == 0.0:
        free_games_ratings.append(rating)

avg_rating_free_games = round(sum(free_games_ratings) / len(free_games_ratings),2)
print('The average rating of free games is:', avg_rating_free_games)

games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[8])
    genre = row[12]
    if genre == 'Social Networking' or genre == 'Games':
        games_social_ratings.append(rating)
avg_games_social = round(sum(games_social_ratings) / len(games_social_ratings),2)
print('The average rate of games using social network is:', avg_games_social)

# calculate the average of non free games using social network
non_free_games_social_ratings = []
free_games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[8])
    genre  = row[12]
    price = float(row[5])
    if (genre == 'Social Networking' or genre == 'Games') and price != 0.0:
        non_free_games_social_ratings.append(rating)
    else:
        free_games_social_ratings.append(rating)

avg_non_free = round(sum(non_free_games_social_ratings) / len(non_free_games_social_ratings),2)
print('The average rate of non free games using social network is:',avg_non_free)

avg_free = round(sum(free_games_social_ratings)/ len(free_games_social_ratings),2)
print('The average rate of free games using social network is:',avg_free)
if avg_non_free > avg_free:
    print('Paid games using social network are better than free games.  ')
else:
    print('Its better to use free games.')

ratings = []
for row in apps_data[1:]:
    rating = float(row[8])
    price = float(row[5])
    if price > 9:
        ratings.append(rating)

avg_ratings = sum(ratings) /len(ratings)
n_apps_less_9 = len(apps_data[1:]) - len(ratings)
n_apps_more_9 = len(ratings)

# adding new colum with conditional statement if label free on non free 
for app in apps_data[1:]:
    price = float(app[5])
    if price == 0.0:
        app.append('Free')
    else:
        app.append('Non-free')
apps_data[0].append('Free_or_not')

for app in apps_data[1:]:
    price = float(app[5])
    if price == 0.0:
        app.append('free')
    elif price > 0 and price < 20:
        app.append('affordable')
    elif price >= 20 and price < 50:
        app.append('expensive')
    elif price >= 50:
        app.append('very expensive')
apps_data[0].append('price_label')
print(apps_data[:6])


content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}
is_in_dictionary_1 = '9+' in content_ratings
is_in_dictionary_2 = 987 in content_ratings
print(is_in_dictionary_1, is_in_dictionary_2) # giving True and False
if '17+' in content_ratings:
    result = 'it exist'
    print(result)

print('done')