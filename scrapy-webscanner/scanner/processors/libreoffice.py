from processor import Processor
import os
import os.path
import subprocess
import random
import hashlib

base_dir = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), '..', '..', '..'
)

var_dir = Processor.var_dir()
lo_dir = os.path.join(var_dir, "libreoffice")
home_root_dir = os.path.join(lo_dir, "homedirs")


class LibreOfficeProcessor(Processor):
    item_type = "libreoffice"

    def __init__(self):
        super(Processor, self).__init__()
        self.home_dir = None

    def setup_home_dir(self):
        # Make a unique home directory for LibreOffice
        home_dir = ""
        while True:
            self.instance_name = hashlib.md5(str(random.random())).hexdigest()
            home_dir = os.path.join(home_root_dir, self.instance_name)

            if not os.path.exists(home_dir):
                self.set_home_dir(home_dir)
                break

    def set_home_dir(self, home_dir):
        self.home_dir = home_dir
        self.env = os.environ.copy()
        self.env['HOME'] = self.home_dir
        if not os.path.exists(self.home_dir):
            os.makedirs(self.home_dir)

    def setup_queue_processing(self, *args):
        self.set_home_dir(os.path.join(home_root_dir, args[0]))

    def handle_spider_item(self, data, url_object):
        return self.add_to_queue(data, url_object)

    def handle_queue_item(self, item):
        return self.convert_queue_item(item)

    def convert(self, item, tmp_dir):
        if self.home_dir is None:
            self.setup_homedir()
        
        # TODO: Input type to filter mapping?
        return_code = subprocess.call([
                                          "libreoffice", "--headless",
                                          "--convert-to", "htm:HTML",
                                          item.file_path, "--outdir", tmp_dir
                                      ], env=self.env)
        return return_code == 0


Processor.register_processor(LibreOfficeProcessor.item_type,
                             LibreOfficeProcessor)
