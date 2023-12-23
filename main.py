import sys
from time import sleep


def write(sentence, duration=0.1):
    for char in sentence:
        sleep(duration)
        sys.stdout.write(char)
        sys.stdout.flush()

write("WELCOME TO NUMBER GUESSER\nPlease choose any number between 1 - 50 and I will answer it in max 10 questions\n Answer the questions in [y/n]\n")
a = input("Is the number greater than 25: ")
if(a == "y"):
  b = input("Is the number greater than 37: ")
  if(b =='y'):
    c = input("Is the number greater than 43: ")
    if(c =='y'):
      d = input('Is the number odd: ')
      if(d == 'y'):
        e = input('Is the number 43: ')
        if(e == 'y'):
          write('The number is 43. I won !!')
        if(e == 'n'):
          f = input('Is the number 45: ')
          if(f == 'y'):
            write('The number is 45. I won!!')
          if(f =='n'):
            g = input('Is the number 47: ')
            if(g == 'y'):
              write('The number is 47. I won!!')
            if(g == 'n'):
              h = input('Is the number 49: ')
              if(h == 'y'):
                write('Is the number 49. I won!!')
      if(d == 'n'):
        e = input('Is the number 44: ')
        if(e == 'y'):
          write('The number is 44. I won !!')
        if(e == 'n'):
          f = input('Is the number 46: ')
          if(f == 'y'):
            write('The number is 46. I won!!')
          if(f =='n'):
            g = input('Is the number 48: ')
            if(g == 'y'):
              write('The number is 48. I won!!')
            if(g == 'n'):
              h = input('Is the number 50: ')
              if(h == 'y'):
                write('The number is 50. I won!!')
    if(c =='n'):
      d = input('Is the number odd: ')
      if(d == 'y'):
        e = input('Is the number 37: ')
        if(e == 'y'):
          write('The number is 37. I won !!')
        if(e == 'n'):
          f = input('Is the number 39: ')
          if(f == 'y'):
            write('The number is 39. I won!!')
          if(f =='n'):
            g = input('Is the number 41: ')
            if(g == 'y'):
              write('The number is 41. I won!!')
            if(g == 'n'):
              h = input('Is the number 43: ')
              if(h == 'y'):
                write('The number is 43. I won!!')
      if(d == 'n'):
        e = input('Is the number 38: ')
        if(e == 'y'):
          write('The number is 38. I won !!')
        if(e == 'n'):
          f = input('Is the number 40: ')
          if(f == 'y'):
            write('The number is 40. I won!!')
          if(f =='n'):
            g = input('Is the number 42: ')
            if(g == 'y'):
              write('The number is 42. I won!!')
  if(b =='n'):
    c = input("Is the number greater than 31: ")
    if(c =='y'):
      d = input('Is the number odd: ')
      if(d == 'y'):
        e = input('Is the number 31: ')
        if(e == 'y'):
          write('The number is 31. I won !!')
        if(e == 'n'):
          f = input('Is the number 33: ')
          if(f == 'y'):
            write('The number is 33. I won!!')
          if(f =='n'):
            g = input(' Is the number 35: ')
            if(g == 'y'):
              write('The number is 35. I won!!')
              if(g == 'y'):
                h = input('Is the number 37: ')
                if(h =='y'):
                  write("The number is 37. I won!!")
      if(d == 'n'):
        e = input('Is the number 32: ')
        if(e == 'y'):
          write('The number is 32. I won !!')
        if(e == 'n'):
          f = input('Is the number 34: ')
          if(f == 'y'):
            write('The number is 34. I won!!')
          if(f =='n'):
            g = input('Is the number 36: ')
            if(g == 'y'):
              write('The number is 36. I won!!')
    if(c =='n'):
      d = input('Is the number odd: ')
      if(d == 'y'):
        e = input('Is the number 25: ')
        if(e == 'y'):
          write('The number is 25. I won !!')
        if(e == 'n'):
          f = input('Is the number 27: ')
          if(f == 'y'):
            write('The number is 27. I won!!')
          if(f =='n'):
            g = input(' Is the number 29: ')
            if(g == 'y'):
              write('The number is 29. I won!!')
            if(g == 'n'):
              h = input('Is the number 31: ')
              if(h == 'y'):
                write('The number is 31. I won!!')
      if(d == 'n'):
        e = input('Is the number 26: ')
        if(e == 'y'):
          write('The number is 26. I won !!')
        if(e == 'n'):
          f = input('Is the number 28: ')
          if(f == 'y'):
            write('The number is 28. I won!!')
          if(f =='n'):
            g = input('Is the number 30: ')
            if(g == 'y'):
              write('The number is 30. I won!!')
if(a =="n"):
  bb = input('Is the number smaller than 12: ')
  if(bb == 'y'):
    z = input("Is the number smaller than 6: ")
    if(z == 'y'):
      dd = input('Is the number odd: ')
      if(dd == 'y'):
        e = input('Is the number 1: ')
        if(e == 'y'):
          write('The number is 1. I won !!')
        if(e == 'n'):
          f = input('Is the number 3: ')
          if(f == 'y'):
            write('The number is 3. I won!!')
          if(f =='n'):
            g = input('Is the number 5: ')
            if(g == 'y'):
              write('The number is 5. I won!!')
      if(dd == 'n'):
        e = input('Is the number 2: ')
        if(e == 'y'):
          write('The number is 2. I won !!')
        if(e == 'n'):
          f = input('Is the number 4: ')
          if(f == 'y'):
            write('The number is 4. I won!!')
          if(f =='n'):
            g = input('Is the number 6: ')
            if(g == 'y'):
              write('The number is 6. I won!!')
    if(z == 'n'):
      dd = input('Is the number odd: ')
      if(dd == 'y'):
        e = input('Is the number 7: ')
        if(e == 'y'):
          write('The number is 7. I won !!')
        if(e == 'n'):
          f = input('Is the number 9: ')
          if(f == 'y'):
            write('The number is 9. I won!!')
          if(f =='n'):
            g = input(' Is the number 11: ')
            if(g == 'y'):
              write('The number is 11. I won!!')
      if(dd == 'n'):
        e = input('Is the number 6: ')
        if(e == 'y'):
          write('The number is 6. I won !!')
        if(e == 'n'):
          f = input('Is the number 8: ')
          if(f == 'y'):
            write('The number is 8. I won!!')
          if(f =='n'):
            g = input('Is the number 10: ')
            if(g == 'y'):
              write('The number is 10. I won!!')
            if(g == 'n'):
              h = input('Is the number 12: ')
              if(h == 'y'):
                write('The number is 12. I won !!')
  if(bb == 'n'):
    z = input("Is the number smaller than 18: ")
    if( z == 'y'):
      d = input('Is the number odd: ')
      if(d == 'y'):
        e = input('Is the number 13: ')
        if(e == 'y'):
          write('The number is 13. I won !!')
        if(e == 'n'):
          f = input('Is the number 15: ')
          if(f == 'y'):
            write('The number is 15. I won!!')
          if(f =='n'):
            g = input(' Is the number 17: ')
            if(g == 'y'):
              write('The number is 17. I won!!')
      if(d == 'n'):
        e = input('Is the number 12: ')
        if(e == 'y'):
          write('The number is 12. I won !!')
        if(e == 'n'):
          f = input('Is the number 14: ')
          if(f == 'y'):
            write('The number is 14. I won!!')
          if(f =='n'):
            g = input('Is the number 16: ')
            if(g == 'y'):
              write('The number is 16. I won!!')
            if(g == 'n'):
              h = input('Is the number 18: ')
              if(h == 'y'):
                write('The number is 18. I won!!')
    if(z == 'n'):
      d = input('Is the number odd: ')
      if(d == 'y'):
        e = input('Is the number 19: ')
        if(e == 'y'):
          write('The number is 19. I won !!')
        if(e == 'n'):
          f = input('Is the number 21: ')
          if(f == 'y'):
            write('The number is 21. I won!!')
          if(f =='n'):
            g = input(' Is the number 23: ')
            if(g == 'y'):
              write('The number is 23. I won!!')
            if(g == 'n'):
              write('The number is 25, I won!!')
      if(d == 'n'):
        e = input('Is the number 18: ')
        if(e == 'y'):
          write('The number is 18. I won !!')
        if(e == 'n'):
          f = input('Is the number 20')
          if(f == 'y'):
            write('The number is 20. I won!!')
          if(f =='n'):
            g = input('Is the number 22')
            if(g == 'y'):
              write('The number is 24. I won!!')
    
  