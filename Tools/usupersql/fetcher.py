import os, sys, re
from customexceptions import ArgsException

class Fetcher(object):
    """
        this class is used to create a MySql dump command
        based on the connection string in your web.config
    """

    def CommandAndArguments(self, webconfig, command):
        """
            return MySql dump command and arguments
        """
        constr = self.findConStr(webconfig)
        constrsettings = self.buildConSettings(constr)
        return self.buildCommand(constrsettings, command)

    def findConStr(self, webConfig ):
        w = open( webConfig, 'r' )
        constr = ''
        for l in w.readlines():
            if self.matchConStr(l):
                constr = self.matchConStr(l)
    
        return constr
    
    def matchConStr(self, xmlline):
        regex = r'<add.*key=\"umbracoDbDSN\".*value=\"(.*)\".*/>'
        m = re.search(regex, xmlline)
        if m:
            return m.group(1) 
    
    def buildConSettings(self, constr):
        return dict( [ tuple( s.lower().split('=') ) for s in constr.split(';') if
        '=' in s ] )
    
    def buildCommand(self, conSettings, command):
        if conSettings['datalayer'] == 'mysql':
            return self.buildMySqlCommand(conSettings, command) 
        else:
            raise Exception, 'Sorry but we only support MySql. Might change in the future'
    
    def buildMySqlCommand(self, cs, command):
        return '{0} -u{1} -p{2} -h{3} {4}'.format(
                                                   command,
                                                   cs['user id'], 
                                                   cs['password'], 
                                                   cs['server'], 
                                                   cs['database'])
