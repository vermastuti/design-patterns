
class IChannel:
    def __init__(self):
        pass

    def add_subscriber(self):
        pass

    def remove_susbcriber(self):
        pass

    def notify(self):
        pass


class ISubscriber:
    def __init__(self):
        pass

    def update(self):
        pass


class Channel(IChannel):
    def __init__(self, name):
        self.name = name
        self.latest_video = ""
        self.subscribers = set()

    def add_subscriber(self, subscriber:ISubscriber):
        self.subscribers.add(subscriber)

    def remove_susbcriber(self, subscriber:ISubscriber):
        self.subscribers.discard(subscriber)

    def notify(self):
        for subscriber in self.subscribers:
            subscriber.update()

    def get_latest_video(self):
        return self.latest_video
    
    def upload_video(self, new_video_url="new_video"):
        self.latest_video = new_video_url
        self.notify()


class Subscriber(ISubscriber):
    def __init__(self, name, channel):
        self.name = name
        self.channel = channel

    def update(self):
        watch = self.channel.get_latest_video()
        print(f"{self.name} watched the latest video {watch} by {self.channel.name} ")


if __name__ == "__main__":
    channel = Channel(name="RockTheCode")

    subscriber1 = Subscriber(name="Toto", channel=channel)
    subscriber2 = Subscriber(name="Boto", channel=channel)

    channel.add_subscriber(subscriber1)
    channel.add_subscriber(subscriber2)

    channel.upload_video(new_video_url="System Design is Fun!!")

    channel.remove_susbcriber(subscriber2)

    channel.upload_video(new_video_url="Let's Dive into OOPS concepts")
