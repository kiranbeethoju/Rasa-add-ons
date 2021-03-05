new_p = []
intent_list = "yoga_specialist,venereologist,urologist,surgical_gastroenterologist,spine_surgeon,spine_health_specialist,speech_therapist,sleep_medicine_physician,sexologist,rheumatologist,radiation_oncologist,pulmonologist,psychologist_counsellor,psychiatrist,plastic_surgeon,pathologist,paediatrician,paediatric_surgeon,orthopaedician_and_traumatologist,orthodontist,ENT,eye_care_ophthalmologist,obstetrician_and_gynaecologist,nutritionist,neurologist,neuro_surgeon,nephrologist,naturopathy_specialist,microbiologist,medical_gastroenterologist,lactation_counselor,internal_medicine_physician,infertility_specialist,infectious_diseases_specialist,homeopathic_physician,HIV_AIDS_specialist,hematologist,general_surgeon,general_practitioner,general_medicine_physician,fitness_expert,family_physician,endodontist,endocrinologist,dietician,diabetologist,dermatologist,dentist,criticalcare_physician,cosmetologist,community_medicine_physician,chiropractor,child_health_specialist,cardiologist,ayurveda_specialist,bariatric_surgery,audiologist,anesthesiologist,allergy_specialist,andrologist".split(",")
with open("temp_text.txt","a") as f:
    for intent in intent_list:
        one = " \nutter_{}:\n".format(intent)
        two = "  - text: I think you are looking for [{}](https://www.xyz.com/)?\n".format(intent)
        
        three = "  - text: You might be looking for [{}](https://www.xyz.com/)?".format(intent)
        final = one+two+three
        f.writelines(final)
        neww = "- "+one
        new_p.append(neww)

#%%
with open("temp_text.txt","a") as f:
    for intent in intent_list:    
        s = "\n## story 2 {} \n ".format(intent)
    
        a121 = "\n* greet\n".format(intent)
        b231 =  "    - utter_greet".format(intent)
    
        a12 = "\n* {}\n".format(intent)
        b23 =  "  - utter_{}".format(intent)
    
        a1 = "\n* {}\n".format(intent)
        b2 =  "  - utter_{} \n".format(intent)
        c =  "  - utter_did_that_help"
        b =  "\n  - utter_thankyou \n"
        print(s+a1+b2+c)
        final = s+a1+b2+c
        f.writelines(final)
