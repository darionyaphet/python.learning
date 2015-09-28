import os
import imp


source_path = os.getcwd()+'/folder'
source_name = 'exec_source_code'

fp, pathname, description = imp.find_module(source_name,[source_path])
module = imp.load_module(source_name,fp,pathname,description)

module.print_info()


source_name = 'print_thread'
fp, pathname, description = imp.find_module(source_name,[source_path])
module = imp.load_module(source_name,fp,pathname,description)

instance = module.print_threading('Hello Darion.Johannes.Yaphet')
instance.start()
