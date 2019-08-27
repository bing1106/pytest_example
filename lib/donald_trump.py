from random import randint

import lib.trump_util as tutil

msgTooLongThresh = 20
maxEnemyThresh = 25

class Social_Media(object):
    def __init__(self, time):
        self.timestamp = time
    def publish_msg(self, msg):
        pass
    def __str__(self):
        return self.__class__.__name__


class Twitter(Social_Media):
    def publish_msg(self, msg):
        print("Tweeting: " + msg)


class Facebook(Social_Media):
    def publish_msg(self, msg):
        print("Facebooking: " + msg)

        
class Instagram(Social_Media):
    def publish_msg(self, msg):
        print("Instagramming: " + msg)


class Donald_Trump(object):

    def __init__(self, initTime=0):
        self.platform = Twitter(initTime)
        self.enemies = 0
    
    def check_enemies(self):
        return tutil.add_two_num(self.enemies, randint(0,9))
    
    def switch_platform(self):
        total_enemies = self.check_enemies()
        if total_enemies > 15:
            self.platform = Instagram(timestamp=100)
        elif total_enemies > 10:
            self.platform = Facebook(timestamp=200)
        else:
            pass
    
    def publish_message(self, msg):
        self.platform.publish_msg(msg)
        if tutil.msg_len(msg) > msgTooLongThresh:
            self.enemies += 2
        else:
            self.enemies += 1
        self.switch_platform()
    
    def has_too_many_enemies(self):
        return True if self.check_enemies > maxEnemyThreshold else False
    