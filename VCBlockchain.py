# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 17:39:56 2018

@author: VictorCHC
"""

"""Reference:
    http://ecomunsing.com/build-your-own-blockchain"""

import hashlib, json, sys

"""A hash function is created as a ‘fingerprint’ for each transactions- 
this hash function links each of our blocks to each other"""

def hashMe(msg=""):
    """Helper function that wraps our hashing algorithm"""
    
    if type(msg)!=str:
        msg = json.dumps(msg,sort_keys=True)
        # If keys are unsorted we can't guarantee repeatability
    
    if sys.version_info.major == 2:
        return unicode(hashlib.sha256(msg).hexdigest(),'utf-8')
    else:
        return hashlib.sha256(str(msg).encode('utf-8')).hexdigest()
    
    