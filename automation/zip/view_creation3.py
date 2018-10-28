import couchdb
from couchdb.design import ViewDefinition #abc

couch = couchdb.Server('http://admin:password@115.146.85.196:5984/')
database = couch['distance']

view = ViewDefinition('topuser', 'distance', 'function (doc) { emit(doc.user_id, doc.user_id);}')
view.get_doc(database)
view.sync(database)
