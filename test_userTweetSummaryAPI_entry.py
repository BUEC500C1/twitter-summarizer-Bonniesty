#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 17:06:52 2020

@author: tysun
"""

import pytest
import userTweetSummaryAPI_entry as test

def test_error():
    assert test.entryAPI("AAA") == "No Account!"

def test_case():
    pass
    #enter twitter credential to pass the test
    #assert test.entryAPI("@AnimalPlanet") == "Success!"
    #assert test.entryAPI("@KuoaiBBB") == "Success!"
 
    
if __name__ == "__main__":
    test_error()
    test_case()
    
