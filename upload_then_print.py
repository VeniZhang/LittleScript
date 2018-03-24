#!usr/bin/env python
#coding:utf8
import os
from pyinotify import WatchManager, Notifier, ProcessEvent, IN_DELETE,\
        IN_CREATE, IN_MODIFY, IN_CLOSE_WRITE
import commands
import time

class EventHandler(ProcessEvent):
    def process_IN_CREATE(self, event):
        path_name = os.path.join(event.path, event.name)
        print "Create file: %s" % path_name

    def process_IN_CLOSE_WRITE(self, event):
        print "write over"
        print "add to print"
        path_name = os.path.join(event.path, event.name)
        print "added,printing"
        
def FSMonitor(path='../public/print'):
    wm = WatchManager()
    mask = IN_CLOSE_WRITE | IN_CREATE#IN_DELETE | IN_CREATE | IN_MODIFY
    notifier = Notifier(wm, EventHandler())
    wm.add_watch(path, mask, rec=True)
    print "now starting monitor %s" % (path)
    while True:
        try:
            notifier.process_events()
            if notifier.check_events():
                notifier.read_events()
        except KeyboardInterrupt:
            notifier.stop()
            print KeyboardInterrupt
            break
        
if __name__ == "__main__":
    FSMonitor()
