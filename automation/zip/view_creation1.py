import couchdb
from couchdb.design import ViewDefinition #abc

couch = couchdb.Server('http://admin:password@115.146.85.196:5984/')
database = couch['mostfollowers']

topfollowers = ViewDefinition('topfollowers', 'followers', 'function (doc) { if(doc.user_id) {emit(doc.followers, doc.user_id);}}')
topfollowers.get_doc(database)
topfollowers.sync(database)
