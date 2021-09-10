from src.classEmoji import Emoji


# Search OS User
def checkOs(useragent):
    if 'Windows' in useragent:
        return Emoji.WINDOWS.value
    elif 'Android' in useragent and 'Linux' in useragent:
        return Emoji.ANDROID.value
    elif 'Linux' in useragent:
        return Emoji.LINUX.value
    elif 'Macintosh' in useragent or 'Mac OS X' in useragent:
        return Emoji.MAC.value
    else:
        return Emoji.DEFAULT.value
