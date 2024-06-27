import csv
import random

def writeWordsTofile():
  words_list=['Apple','Banana','Orange','Grapes','Mango','Tiger','Elephant','Zebra','Giraffe',
              'Monkey','Guitar','Piano','Violin','Drums','Flute','House','Castle','Cabin','Apartment',
              'Mansion','Car','Bicycle','Airplane','Helicopter','Boat']

  with open('words.csv', 'w') as words:
    wordswriter=csv.writer(words)
    wordswriter.writerow(['Words'])
    for word in words_list:
      wordswriter.writerow([word])

def load():
  print('='*50)
  print('HANGMAN GAME'.center(50))
  print('='*50)
  print('Guess the missing letters:')
  print('='*50)

def random_word():
  words_list=[]
  with open('words.csv', 'r') as words:
    data=csv.reader(words)
    for row in data:
      words_list.append(row[0])
      random_index=random.randint(0,len(words_list)-1)
    word=words_list[random_index]
    return word.upper()

def init_track(word):
  dash = ' ___ '
  track=dash*len(word)
  return track

def update_track(track, word, letter):
    new_track = ''
    for i in range(len(word)):
        if word[i] == letter:
            new_track += f'  {letter}  '
        else:
            new_track += track[i*5 : i*5 + 5]
    return new_track


word=random_word().upper()
track=init_track(word)
load()
print(f'\n{track.center(50)}\n')

tries=len(word)
while tries > 0:
  guess=input('Enter your a letter or guess the word: ').upper()
  if len(guess) == 1:
    if guess in word:
      print('*'*50)
      print(f'Good guess! The word has {guess}.')
      print('*'*50)
      tries-=1
      print(f'You have {tries} tries left.')
      print('-'*50)
      track=update_track(track, word, guess)
      print(f'\n{track.center(50)}\n')
    else:
      print('-'*50)
      print(f'Nope. No, "{guess}".Try again.')
      tries-=1
      print('-'*50)
      if tries==0:
        print(f'You run out of tries.')
      elif tries==1:
        print(f'ONE MORE TRY.')
      else:
        print(f'You have {tries} tries left.')
  else:
    if guess == word:
      print('*'*50)
      print(f'You got it! The word was "{guess}"')
      print('*'*50)
      break
    else:
      print('-'*50)
      print(f'Nope. The word is not "{guess}".Try again.')
      print('-'*50)
      tries-=1
      if tries==0:
        print(f'You run out of tries.')
      elif tries==1:
        print(f'ONE MORE TRY.')
      else:
        print(f'You have {tries} tries left.')
      print('-'*50)
  if '_' not in ''.join(track):
    print(f'You got it! The word was {word}')
    break
if tries==0 and '_' in ''.join(track):
  print('*'*50)
  print(f'The word was {word}. Better luck next time.')
  print('*'*50)
