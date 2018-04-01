import sys
import emailprotectionslib.dmarc as dmarc

from MaltegoTransform import *

mt = MaltegoTransform()
mt.parseArguments(sys.argv)
domain = mt.getValue()
mt = MaltegoTransform()

try:
    dmarc_record = dmarc.DmarcRecord.from_domain(domain)
    #print spf_record
    mt.addEntity("maltego.Phrase","DMARC Record: "+str(dmarc_record))

except:
    mt.addUIMessage("Exception Occured",messageType="PartialError")
mt.returnOutput()
