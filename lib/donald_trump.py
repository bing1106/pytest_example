from random import randint

import lib.trump_util as tutil

msgTooLongThresh = 20
maxEnemyThresh = 25

class Social_Media(object):
    def __init__(self, time):
        self.timestamp = time
    def publish_msg(self, msg):
        pass
    def platform_followers(self, msg):
        pass
    def __str__(self):
        return self.__class__.__name__


class Twitter(Social_Media):
    def publish_msg(self, msg):
        print("Tweeting: " + msg)
    def platform_followers(self):
        return 1000000

    
class Facebook(Social_Media):
    def publish_msg(self, msg):
        print("Facebooking: " + msg)
    def platform_followers(self):
        return 20000
        
        
class Instagram(Social_Media):
    def publish_msg(self, msg):
        print("Instagramming: " + msg)
    def platform_followers(self):
        return 230
    

class Donald_Trump(object):

    def __init__(self, initTime=0):
        self.platform = Twitter(initTime)
        self.enemies = 0
    
    def check_enemies(self):
        return tutil.add_two_num(self.enemies, randint(0,9))
    
    def switch_platform(self):
        total_enemies = self.check_enemies()
        if total_enemies > 15:
            self.platform = Instagram(time=100)
        elif total_enemies > 10:
            self.platform = Facebook(time=200)
        else:
            pass
    
    def publish_message(self, msg):
        if tutil.msg_len(msg) > msgTooLongThresh:
            self.platform.publish_msg(msg)
            self.platform.publish_msg(msg)
        else:
            self.platform.publish_msg(msg)
        self.enemies += 1    
        self.switch_platform()
    
    def has_too_many_enemies(self):
        return True if self.check_enemies() > maxEnemyThresh else False
    