#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import urllib2
import time
import winsound  
    
def main():
    while True:
        try:
            global d
            d = raw_input("Please enter the URL of the page (using www.example.com): ")
            global asd
            asd = 'http://' + d
            ret = urllib2.urlopen(asd)
            if ret.code == 200:
                print "Page is valid! If there is any change in the source code of the page your PC will make a sound!"
                s()
                break
            elif ret.code != 200:
                print "There is some type of error or the page may be down!"
                print "Please try again!"
                main()
        except:
            print "Doesn't exist or a typo!"
            print "Please try again!"
            main()
    
def s():
    user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
    headers = { 'User-Agent' : user_agent }
    req = urllib2.Request(asd, None, headers)
    response = urllib2.urlopen(req)
    page = response.read()
    response.close()

    time.sleep(5)

    user_agent2 = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
    headers2 = { 'User-Agent' : user_agent }
    req2 = urllib2.Request(asd, None, headers)
    response2 = urllib2.urlopen(req2)
    page2 = response2.read()
    response2.close()

    if page != page2:
        print "There is a change detected in the source code"
        winsound.Beep(2500,10000)
    elif page == page2:
        s()

if __name__ == "__main__":
    main()
