import sys
import struct
import os
import re
import tempfile
import shutil
#import random

elf_id=b'\x7fELF'

class _ELF:
   def __init__ ( self , file ) : 
      global elf_id
      self.path=None
      self.f = open(file,'rb')
      id=self.f.read(len(elf_id))
      if id !=elf_id:
         print ( "Not ELF file" )
         exit(1)

      ftype = self.get_w16 ( 16 )
      if ftype != 4:
         print ( "Not core file" )
         exit(1)
      self.ph_off=self.get_w32 ( 28 )
      self.ph_size=self.get_w16 ( 42 )
      self.ph_num=self.get_w16 ( 44 )
#      h = self.header (0)
#      print (h)
      for i in range (self.ph_num):
         h = self.header (i)
         if h[0] == 4: break
#      print (h)
      self.f.seek(h[1],0)
      self.note=self.f.read (h[4])
#      print (self.note)
      i=0
      while i<h[4]:
         ns=struct.unpack("=L", self.note[i:i+4])[0]
         ds=struct.unpack("=L", self.note[i+4:i+8])[0]
         t=struct.unpack("=L", self.note[i+8:i+12])[0]
#         print ( ns,ds,t)
         na = str(self.note[i+12:i+11+ns])
         ns = ( ns + 3 ) & 0xfffc
         des = str(self.note[i+12+ns:i+12+ns+ds])
         desx = self.note[i+12+ns:i+12+ns+ds]
         ds = ( ds + 3 ) & 0xfffc
#         print ( na,des)
         i += ns + ds + 12
         if str(na) == str(b'CORE') and t==3:
            v=desx[44:]
            j=v.index('\0')
            self.path=v[:j].strip()
            if ' ' in self.path: self.path=self.path.partition(' ')[0]
#            print (v)
 
   def get_w32 ( self , off ): 
      self.f.seek(off,0)
      return struct.unpack("=L", self.f.read(4))[0]

   def get_w16 ( self , off ): 
      self.f.seek(off,0)
      return struct.unpack("=H", self.f.read(2))[0]

   def header ( self,num):
      if num >= self.ph_num:
         print ( "Large header num" )
         exit(1)
      self.f.seek(self.ph_off+num*self.ph_size,0)
      v=self.f.read(self.ph_size)
      return tuple ( struct.unpack("=L", v[i:i+4])[0] for i in range ( 0 , self.ph_size, 4) )
      
def RunCmd ( cmd ):
    file=os.popen(cmd)
    data=file.read()
    file.close()
    return data

def fff (f ,silent=False):
   if not silent:
      print ("Decoding the core file %s"%(f))
   x=RunCmd ( 'tar -tf %s 2> nul'%(f) )
#   print (x)
   mo=re.match ( '^pss([0-9]+)/' , x )
   if mo == None: 
      if not silent:
         print ("Unable to identify the PID in the file %s"%(f))
      return
   pid = mo.group(1)
#   print (pid)
   corefile=None
   logfile=None
   for l in x.splitlines():
      mo=re.match ( '0x.*_log\.%s$'%(pid) , l )
      if mo != None: logfile = l
      mo=re.match ( '0x.*_core\.%s\.gz$'%(pid) , l )
      if mo != None: corefile = l
#   print (corefile,logfile)
#   if corefile == None or logfile == None: return
   if corefile == None:
      if not silent:
         print ("Unable to locate the core in the file %s"%(f))
      return

   if silent:
      print ("Decoding the core file %s"%(f))

   dir = tempfile.mkdtemp(suffix='coredir', prefix='tmp', dir=tempdir)
#   print (dir)

   x=RunCmd ( 'tar -zxf %s -C %s --overwrite 2> nul'%(f,dir) )
#   print (x)
   RunCmd ( 'gunzip -f %s 2> nul' %(dir + '/' + corefile ))
   corefile=corefile.partition('.gz')[0]
#   f = open(tempdir + '/' + corefile,'r')
#   f.close()
   e=_ELF(dir + '/' + corefile)
   if e.path == None:
      print ('Unable to locate the executable path')
      return
   print ('Executable path is %s'%(e.path))
#   print ('!!!!!')
   x=RunCmd ( "gdb -ex 'bt full' -ex quit %s %s 2> nul" %(e.path,dir + '/' + corefile ))
   print (x)

   shutil.rmtree(dir,ignore_errors=True)
#   os.remove ( tempdir + '/' + corefile )
#   os.remove ( tempdir + '/' + logfile )

#tempdir='/var/volatile/tmp'
tempdir='/var/sysmgr/logs'
#tempdir='/bootflash'

if len(sys.argv)> 1:
   fff ( '/bootflash/' + sys.argv[1] )
   exit(1)
x=RunCmd ( 'ls /var/sysmgr/logs/*.tar.gz 2> nul' )
for l in x.splitlines():
   fff ( l ,silent=True)
   
