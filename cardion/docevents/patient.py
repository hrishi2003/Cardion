import frappe
from frappe import _
from frappe.model.document import Document
from frappe.model.naming import make_autoname

# Autoname the series According To Branch
def autoname(doc, method):
   	if doc.sex:
   		if doc.sex == 'Male' :
   			doc.user_id = make_autoname("CHN-M-"+".####")
   			return doc.user_id
   		elif doc.sex == 'Female' :
   			doc.user_id = make_autoname("CHN-F-"+".####")
   			return doc.user_id
   		elif doc.sex == 'Non-Conforming' :
   			doc.user_id = make_autoname("CHN-N-"+".####")
   			return doc.user_id
        # elif doc.sex == 'Genderqueer' :
        #     doc.uid = make_autoname("CNQ"+".####")
        #     return doc.uid 
        # elif doc.sex == 'Transgender' :
   		# 	doc.uid = make_autoname("CNT"+".####")
   		# 	return doc.uid              
   		else :
   			return doc.user_id