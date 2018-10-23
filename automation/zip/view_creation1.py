import couchdb
from couchdb.design import ViewDefinition #abc

couch = couchdb.Server('http://user:password@127.0.0.1:5984/')
database = couch['mostfollowers']

topfollowers = ViewDefinition('topfollowers', 'followers', 'function (doc) { if(doc.user_id) {emit(doc.followers, doc.user_id);}}')
topfollowers.get_doc(database)
topfollowers.sync(database)