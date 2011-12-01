from AccessControl import ClassSecurityInfo
from DateTime import DateTime
from Products.ATExtensions.ateapi import DateTimeField, DateTimeWidget
from Products.Archetypes.public import *
from bika.lims.content.bikaschema import BikaSchema
from bika.lims.config import I18N_DOMAIN, PROJECTNAME
from bika.lims import bikaMessageFactory as _

schema = BikaSchema.copy()

class Reports(BaseContent):
    security = ClassSecurityInfo()
    displayContentsTab = False
    id = 'reports'
    schema = schema

registerType(Reports, PROJECTNAME)
