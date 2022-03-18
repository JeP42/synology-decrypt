from __future__ import print_function
import os
import sys
import logging

import syndecrypt.core as core
import syndecrypt.files as sydecryptfiles


LOGGER=logging.getLogger(__name__)

def decrypt_directory(input_dir_name, output_dir, password=None, private_key=None):
        if not os.path.exists(input_dir_name):
                LOGGER.warn('skipping decryption of "%s": input dir does not exist',
                        input_dir_name
                )
                return
       
        for dirpath, dirs, files in os.walk(input_dir_name):	
            for filename in files:
                fname = os.path.join(dirpath,filename)
                outputFile = os.path.join(output_dir, fname)
                sydecryptfiles.decrypt_file(fname, outputFile, password, private_key)