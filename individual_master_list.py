from diagnosis_extraction import diagnosis_extraction
from drg_code_extraction import drg_code_extraction
from emar_extraction import emar_extraction
from hcpcs_event_extraction import hcpcs_event_extraction
from lab_item_extraction import lab_item_extraction
from microbiology_extraction import microbiology_extraction
from omr_extraction import omr_extraction
from pharmacy_event_extraction import pharmacy_event_extraction
from poe_entry_extraction import poe_entry_extraction
from prescription_extraction import prescription_extraction
from procedure_extraction import procedure_extraction
from transder_data_extraction import transfer_data_extraction
from radiology_report_extraction import radiology_report_extraction
from service_data_extraction import service_data_extraction
from discharge_report_extraction import discharge_report_extraction


def individual_master_list (subject_id):
  transfer_data = transfer_data_extraction(subject_id)
  service_data = service_data_extraction(subject_id)
  procedure_data = procedure_extraction(subject_id)
  prescription_data = prescription_extraction(subject_id)
  poe_entries = poe_entry_extraction(subject_id)
  pharmacy_events = pharmacy_event_extraction(subject_id)
  omr_entries = omr_extraction(subject_id)
  microbiology_events = microbiology_extraction(subject_id)
  lab_items = lab_item_extraction(subject_id)
  hcpcs_events = hcpcs_event_extraction(subject_id)
  emar_list = emar_extraction(subject_id)
  drg_list = drg_code_extraction(subject_id)
  diagnosis_list = diagnosis_extraction(subject_id)
  radiology_reports = radiology_report_extraction(subject_id)
  discharge_reports = discharge_report_extraction(subject_id)

  final_dictionary = {"transfer_data": transfer_data , "service_data": service_data, "procedure_data":procedure_data, "prescription_data":prescription_data, "poe_entries": poe_entries, "pharmacy_events":pharmacy_events, "omr_entries": omr_entries,
                      "microbiology_events":microbiology_events, "lab_items": lab_items, "hcpcs_events": hcpcs_events, "radiology_reports": radiology_reports, "discharge_reports": discharge_reports}

  return final_dictionary