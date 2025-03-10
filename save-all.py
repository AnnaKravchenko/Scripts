from pymol import cmd
import glob
import re

def save_sep(prefix=''):
  """
  save_sep <prefix>

  saves multiple objects into multiple files using an optional prefix name.

  e.g. save_sep prefix
  """
  obj_list = cmd.get_names("all")

  if obj_list:
    for i in range(len(obj_list)):
      obj_name = "%s%s.pdb" % (prefix, obj_list[i])
      cmd.save(obj_name, obj_list[i])
      print "Saving %s" %  obj_name
  else:
    print "No objects found"
    
cmd.extend('save_sep',save_sep)
