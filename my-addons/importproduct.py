import xmlrpclib
import csv


server ='http://localhost:8069'
db ='DB1'
username ='Admin'
password ='admin'


common = xmlrpclib.ServerProxy('%s/xmlrpc/2/common' % server)
print common.version()


uid = common.authenticate(db, username, password, {})
print uid

OdooApi = xmlrpclib.ServerProxy('%s/xmlrpc/2/object' % server)
product=OdooApi.execute_kw(db, uid, password,'product.template','search_read',[[['available_quantity', '=', True]]])
print product

