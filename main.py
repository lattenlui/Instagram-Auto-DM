from instagramScraper import start
from multiprocessing import Process

def flask():
    import instagramReply

if __name__ == "__main__":
    p1 = Process(target=start)
    p1.start()
    p2 = Process(target=flask)
    p2.start()
    p1.join()
    p2.join()