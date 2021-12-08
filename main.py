import time


def discord_to_utc(sf: int) -> str:
    """
    Returns a formatted Discord ID to UTC
    """
    discord_epoch = 1420070400000
    unix_epoch = (sf >> 22) + discord_epoch
    formatted_time = time.strftime(
        r"%m-%d-%Y %H:%M:%S", time.localtime(unix_epoch / 1000)
    )
    
    return formatted_time


if __name__ == "__main__":
    print(discord_to_utc(256806162828099586))
