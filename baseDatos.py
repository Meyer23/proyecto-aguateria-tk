import os
import ZODB
	
__root_zodb = None 

def get_root_zodb():
	
	'''Conexion a la base de datos con ZODB'''

	global __root_zodb
	if not __root_zodb:
		db = ZODB.DB('data/mydata.fs')
		connection = db.open()
		__root_zodb = connection.root
	return __root_zodb
		
		
