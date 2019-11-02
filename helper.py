#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Helper():

  def nice_time(self,string):
    value = int(string)
    if value < 10:
      newTime = "0" + str(value)
      return newTime

    return str(value)


  def split_string_stunden(self,string): 
    
      # Split the string based on space delimiter 
    list_string = string.split(',') 
        
    return list_string 

    
  def split_string(self,string): 
    
      # Split the string based on space delimiter 
    list_string = string.split(',), (') 
        
    return list_string 

  def split_string_time(self,string): 
    
      # Split the string based on space delimiter 
    list_string = string.split('datetime.datetime') 
        
    return list_string 

  def split_string_minuten(self,string): 
    
      # Split the string based on space delimiter 
    list_string = string.split(')') 
        
    return list_string