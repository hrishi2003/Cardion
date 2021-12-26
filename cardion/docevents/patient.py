import frappe
from frappe import _
from frappe.model.document import Document
from frappe.model.naming import make_autoname

# Autoname the series According To Branch
def autoname(doc, method):
   	if doc.sex:
   		if doc.sex == 'Male' :
   			doc.uid = make_autoname("CHN-M-"+".####")
   			return doc.uid
   		elif doc.sex == 'Female' :
   			doc.uid = make_autoname("CHN-F-"+".####")
   			return doc.uid
   		elif doc.sex == 'Non-Conforming' :
   			doc.uid = make_autoname("CHN-N-"+".####")
   			return doc.uid        
   		else :
   			return doc.uid