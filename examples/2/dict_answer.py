#!/usr/bin/python

# A. use_dict
# Given a small dictionary in list form, convert to dict in use_dict()

# sample dictionary
small_dict = ['a', 'the', 'she', 'he', 'likes', 'CS', 'at', 'lives', 'Harvard', 'HS', 'is', 'students']

# create a dictionary out of the list of words
def use_dict():

  # empty
  d = {}

  # set keys; just set values == None (kind of like OCAML)
  for s in small_dict:
    d[s] = None

  # return dictionary
  return d

# check your answer in the main function
def main():

    # convert list to dict
    d = use_dict()

    # example text
    text = 'I think this might havs mispelled words in it'
    # remove whitespace; turn in to list of strings
    t_list = text.split()

    # example text 2
    text_2 = 'HS students at Harvard'
    t_list_2 = text_2.split()

    error = False

    # check and see if any of the words in texts are in the dict
    for t in t_list_2:
      if t not in d:
        print 'Mispelling!'
        error = True
        break

    for t in t_list:
      if t not in d:
        print 'Mispelling!'
        error = True
        break

    if not error:
      print 'All Looks good!'

    return

if __name__=='__main__':
    main()
