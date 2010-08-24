"""
SQLite implementation of AddFileToFileset
"""
from WMCore.WMBS.MySQL.Files.AddToFileset import AddToFileset as AddFileToFilesetMySQL

class AddToFileset(AddFileToFilesetMySQL):
    sql = """insert into wmbs_fileset_files 
            (file, fileset, insert_time) 
            values ((select id from wmbs_file_details where lfn = :file),
            (select id from wmbs_fileset where name = :fileset), :timestamp)"""
                    
    def getBinds(self, file = None, fileset = None):
        binds = self.dbi.buildbinds(self.dbi.makelist(fileset), 'fileset',
                                self.dbi.buildbinds(
                                            self.dbi.makelist(file), 'file',
                                    self.dbi.buildbinds(
                                        self.dbi.makelist(
                                              self.timestamp()), 'timestamp')))
        return binds

