def Clear(text):
    return "\033[0m{}".format(text)


def Fat(text):
    return "\033[1m{}\033[0m".format(text)


def Fading(text):
    return "\033[2m{}\033[0m".format(text)


def Italic(text):
    return "\033[3m{}\033[0m".format(text)


def Underlined(text):
    return "\033[4m{}\033[0m".format(text)


def Rarely_blink(text):
    return "\033[5m{}\033[0m".format(text)


def Often_blink(text):
    return "\033[6m{}\033[0m".format(text)


def Replacement(text):
    return "\033[7m{}\033[0m".format(text)


def Black(text):
    return "\033[30m{}\033[0m".format(text)


def Red(text):
    return "\033[31m{}\033[0m".format(text)


def Green(text):
    return "\033[32m{}\033[0m".format(text)


def Yellow(text):
    return "\033[33m{}\033[0m".format(text)


def Blue(text):
    return "\033[34m{}\033[0m".format(text)


def Violet(text):
    return "\033[35m{}\033[0m".format(text)


def Turquoise(text):
    return "\033[36m{}\033[0m".format(text)


def White(text):
    return "\033[37m{}\033[0m".format(text)


def Black_fon(text):
    return "\033[40m{}\033[0m".format(text)


def Red_fon(text):
    return "\033[41m{}\033[0m".format(text)


def Green_fon(text):
    return "\033[42m{}\033[0m".format(text)


def Yellow_fon(text):
    return "\033[43m{}\033[0m".format(text)


def Blue_fon(text):
    return "\033[44m{}\033[0m".format(text)


def Violet_fon(text):
    return "\033[45m{}\033[0m".format(text)


def Turquoise_fon(text):
    return "\033[46m{}\033[0m".format(text)


def White_fon(text):
    return "\033[47m{}\033[0m".format(text)
