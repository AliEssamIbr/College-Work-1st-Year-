class PERSON:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"my name is : {self.name}\nand im {self.age} years old\n"
class PATIENT(PERSON):
    def __init__(self,name,age,patient_id,illness):
        self.__patient_id__ = patient_id
        self.__illness__ = illness
        super().__init__(name,age)
class DOCTOR(PERSON):
    def __init__(self,name,age,specialization):
        self.specialization = specialization
        super().__init__(name,age)
class Appointment:
    def __init__(self,patient_name,doctor_name,date):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.date = date

    def __str__(self):
        return f"\n\nAppointment : Mr/Mrs {self.patient_name} with Doctor {self.doctor_name} on {self.date}"

class Hospital:
    def __init__(self):
        self.__patient_list__ = []
        self.__doctor_list__ = []
        self.__appointment_list__ =[]
    def patient_add(self,patient_id,name,age,illness):
        patient = {
                "patient_id" : patient_id,
                "name": name,
                "age": age,
                "illness": illness
            }
        self.__patient_list__.append(patient)
    def doctor_add(self,name,age,specialization):
        doctor = {
                "name": name,
                "age": age,
                "specialization": specialization
            }
        
        self.__doctor_list__.append(doctor)
    def appointment_add(self,patient_name,doctor_name,specialization,date):
        appointment = {
                "patient_name": patient_name,
                "doctor_name": doctor_name,
                "specialization" : specialization,
                "date":date
            }
        self.__appointment_list__.append(appointment)
    def patient_list_print(self):
        a = self.__patient_list__
        return a
    def doctor_list_print(self):
        a = self.__doctor_list__
        return a
    def appointment_list_print(self):
        a_list = ""
        for i in self.__appointment_list__:
            s = "Appointment : Mr/Mrs "+i["patient_name"]+" with doctor "+i["doctor_name"]+" ("+i["specialization"]+") on"+i["date"]+"\n"
            a_list+=s
        return a_list

            



hos = Hospital()

ali = PATIENT("ali",19,201,"dead asf")

print(ali)

ahmed = DOCTOR("ahmed",600000,"cardiology")

print(ahmed)

appt = Appointment(ali.name,ahmed.name,"2026-4-14")

print(appt)

abbas = PATIENT("abbas",29,301,"dead asf")

print(abbas)

mohammed = DOCTOR("mohammed",6023420,"orthopedics")

print(mohammed)

appt = Appointment(abbas.name,mohammed.name,"2026-7-14")

print(appt)

hos.patient_add(301,"abbas",29,"dead asf")

hos.patient_add(201,"ali",19,"dead asf")

hos.doctor_add("mohammed",6023420,"orthopedics")

hos.doctor_add("ahmed",600000,"cardiology")

hos.appointment_add(ali.name,ahmed.name,"cardiology","2026-4-14")

hos.appointment_add(abbas.name,mohammed.name,"orthopedics","2026-71-4")


print("\n\nPATIENT LIST\n","-"*40,"\n",sep="")
print(hos.patient_list_print())
print("\n\nDOCTOR LIST\n","-"*40,"\n",sep="")
print(hos.doctor_list_print())
print("\n\nAPPOINTMENT LIST\n","-"*40,"\n",sep="")
print(hos.appointment_list_print())