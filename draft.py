from apple import Apple


def blabla():
    apple_lst = [Apple(), Apple(), Apple()]
    return list(map((lambda apple: apple.location), apple_lst))
