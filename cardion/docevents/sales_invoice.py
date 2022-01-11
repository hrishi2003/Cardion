import frappe

@frappe.whitelist()
def get_item(inpatient):
	k=[]
	a=inpatient
	m={}
	n={}
	# i = frappe.db.get_value("Inpatient Record",{'name':a},'status')
	# if i!='Discharged':
	encounters = frappe.get_all('Patient Encounter', filters={'inpatient_record': a}, fields=['name'])
	for encounter in encounters:
		drugs = frappe.get_list('Drug Prescription', filters={'parent': encounter.name}, fields=['drug_code', 'drug_name','qty'])
		if len(drugs)>0:
			for j in drugs:
				if j.drug_code not in m:
					m[j.drug_code]=int(j.qty)
				else:
					n[j.drug_code]=int(j.qty)

	for key in m:
		if key in n:
			m[key] = m[key] + n[key]
		else:
			pass
     
	return m

				
@frappe.whitelist()
def get_procedure(inpatient):
	l=[]
	m={}
	n={}
	a=inpatient
	# i = frappe.db.get_value("Inpatient Record",{'name':a},'status')
	# if i!='Discharged':
	pe = frappe.get_all('Patient Encounter', fields=['name'], filters={'inpatient_record': a})
	for i in pe:
		y=frappe.db.get_all("Procedure Prescription",{'parent':i.name},['procedure','procedure_name','qty'])
		if len(y)>0:
			for j in y:
				if j.procedure not in m:
					m[j.procedure]=int(j.qty)
				else:
					n[j.procedure]=int(j.qty)
	for key in m:
		if key in n:
			m[key] = m[key] + n[key]
		else:
			pass

	return m			

@frappe.whitelist()
def get_consumables(inpatient):
	consumable=[]
	m={}
	n={}
	a=inpatient
	# i = frappe.db.get_value("Inpatient Record",{'name':a},'status')
	# if i!='Discharged':
	c = frappe.get_all('Patient Encounter', fields=['name'], filters={'inpatient_record': a})
	for i in c:
		w=frappe.db.get_all("Consumables",{'parent':i.name},['item_code','item_name','quantity'])
		if len(w)>0:
			for j in w:
				if j.item_code not in m:
					m[j.item_code]=int(j.quantity)
				else:
					n[j.item_code]=int(j.quantity)
	for key in m:
		if key in n:
			m[key] = m[key] + n[key]
		else:
			pass

	return m		
# @frappe.whitelist()
# def get_occupancy(inpatient):
	
# 	a=inpatient
# 	w=frappe.db.get_all("Consumables",{'parent':a},['item_code','item_name','quantity'])
# 	return w
		

# @frappe.whitelist()
# def get_item1(inpatient):
# 	lab_tests_to_invoice = []
# 	a=inpatient
# 	lab_tests = frappe.get_list(
# 		'Lab Test',
# 		fields=['name', 'template'],
# 		filters={'patient': 'Chandler', 'company': 'Cardion Hospital', 'invoiced': False, 'docstatus': 1}
# 	)
# 	for lab_test in lab_tests:
# 		item, is_billable = frappe.get_cached_value('Lab Test Template', lab_test.template, ['item', 'is_billable'])
# 		if is_billable:
# 			lab_tests_to_invoice.append({
# 				'reference_type': 'Lab Test',
# 				'reference_name': lab_test.name,
# 				'service': item
# 			})

# 	lab_prescriptions = frappe.db.sql(
# 		'''
# 			SELECT
# 				lp.name, lp.lab_test_code
# 			FROM
# 				`tabPatient Encounter` et, `tabLab Prescription` lp
# 			WHERE
# 				et.patient=%s
# 				and lp.parent=et.name
# 				and lp.lab_test_created=0
# 				and lp.invoiced=0
# 		''', ('Chandler'), as_dict=1)

# 	for prescription in lab_prescriptions:
# 		item, is_billable = frappe.get_cached_value('Lab Test Template', prescription.lab_test_code, ['item', 'is_billable'])
# 		if prescription.lab_test_code and is_billable:
# 			lab_tests_to_invoice.append({
# 				'reference_type': 'Lab Prescription',
# 				'reference_name': prescription.name,
# 				'service': item
# 			})

# 	return lab_tests_to_invoice

@frappe.whitelist()
def get_item1(inpatient):
	lab=[]
	m={}
	n={}
	a=inpatient
	# i = frappe.db.get_value("Inpatient Record",{'name':a},'status')
	# if i!='Discharged':
	z = frappe.get_all('Patient Encounter', fields=['name'], filters={'inpatient_record': a})
	for i in z:
		l=frappe.db.get_all("Lab Prescription",{'parent':i.name},['lab_test_code','lab_test_name','qty'])
		if len(l)>0:
			for j in l:
				if j.lab_test_code not in m:
					m[j.lab_test_code]=int(j.qty)
				else:
					n[j.lab_test_code]=int(j.qty)
	for key in m:
		if key in n:
			m[key] = m[key] + n[key]
		else:
			pass

	return m	
	

def get_item(doc,method):
	validate_item(doc)
	# for i in doc.items:
	# 	a = frappe.get_doc('Item Price',{'item_code':i.item_code})
	# 	i.rate = a.price_list_rate


def validate_item(doc): 
	dict1 = {}
	docitems = []
	for items in doc.items:
		dict1[items.item_code]=items
		
	indexed = 1
	for d_item in sorted(dict1):
		dict1[d_item].idx = indexed
		docitems.append(dict1[d_item])
		indexed+=1
	
	doc.items=docitems		
	
	
	