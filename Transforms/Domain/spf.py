import sys
import emailprotectionslib.spf as spf

from MaltegoTransform import *

mt = MaltegoTransform()
mt.parseArguments(sys.argv)
domain = mt.getValue()
mt = MaltegoTransform()

try:
    spf_record = spf.SpfRecord.from_domain(domain)
    #print spf_record
    mt.addEntity("maltego.Phrase","SPF Record: "+str(spf_record))

except:
    mt.addUIMessage("Exception Occured",messageType="PartialError")
mt.returnOutput()
