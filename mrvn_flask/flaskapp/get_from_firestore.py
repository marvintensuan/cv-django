from google.cloud import firestore
try:
    import google.auth
    from google.cloud import secretmanager_v1beta1 as sm
except ImportError:
    print("Import Error raised.")
    pass

def my_reddit_comments():
    db = firestore.Client()
    coll = db.collection('tagapagtuos_submissions').stream()
    db = None

    return [doc.to_dict() for doc in coll]