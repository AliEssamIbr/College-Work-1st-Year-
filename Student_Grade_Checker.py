class STUDENT:
    def __init__(self,Name,Grade):
        self.Name = Name
        self.Grade = Grade
    def introduce(self):
        print("\n\nHi! My name is "+self.Name+" and my grade is : "+self.Grade)
    def pass_check(self):
        if self.Grade in ("A", "B", "C", "D"):
            return "Passed"
        elif self.Grade == "F":
            return "Failed"
        else:
            return "error"
Ali = STUDENT("Ali","A")
Ahmed = STUDENT("AHmed","B")
Mona = STUDENT("Mona","C")
Ahmed_Mohammed_Mahmood_Saeed_Jasim_Ibrahim_Khdeer_Zaid_Hasan_Haider_Salih_Abbas_Kaka__CoD_MW3_2011_Version__I_RAN_OUT_OF_NAMES = STUDENT("'that guy'","F")
Im_scared_of_the_guy_above_me = STUDENT("Bilal","D")
Ali.introduce()
Ahmed.introduce()
Mona.introduce()
Ahmed_Mohammed_Mahmood_Saeed_Jasim_Ibrahim_Khdeer_Zaid_Hasan_Haider_Salih_Abbas_Kaka__CoD_MW3_2011_Version__I_RAN_OUT_OF_NAMES.introduce()
Im_scared_of_the_guy_above_me.introduce()
if Ali.pass_check() == "Passed":
    print("\n\nThe student "+Ali.Name+" Has Passed with a Grade of : "+Ali.Grade)
elif Ali.pass_check() == "Failed":
    print("\n\nThe student "+Ali.Name+" Has Failed with a Grade of : "+Ali.Grade)
if Ahmed_Mohammed_Mahmood_Saeed_Jasim_Ibrahim_Khdeer_Zaid_Hasan_Haider_Salih_Abbas_Kaka__CoD_MW3_2011_Version__I_RAN_OUT_OF_NAMES.pass_check() == "Passed":
    print("\n\nThe student "+Ahmed_Mohammed_Mahmood_Saeed_Jasim_Ibrahim_Khdeer_Zaid_Hasan_Haider_Salih_Abbas_Kaka__CoD_MW3_2011_Version__I_RAN_OUT_OF_NAMES.Name+" Has Passed with a Grade of : "+Ahmed_Mohammed_Mahmood_Saeed_Jasim_Ibrahim_Khdeer_Zaid_Hasan_Haider_Salih_Abbas_Kaka__CoD_MW3_2011_Version__I_RAN_OUT_OF_NAMES.Grade)
elif Ahmed_Mohammed_Mahmood_Saeed_Jasim_Ibrahim_Khdeer_Zaid_Hasan_Haider_Salih_Abbas_Kaka__CoD_MW3_2011_Version__I_RAN_OUT_OF_NAMES.pass_check() == "Failed":
    print("\n\nThe student "+Ahmed_Mohammed_Mahmood_Saeed_Jasim_Ibrahim_Khdeer_Zaid_Hasan_Haider_Salih_Abbas_Kaka__CoD_MW3_2011_Version__I_RAN_OUT_OF_NAMES.Name+" Has Failed with a Grade of : "+Ahmed_Mohammed_Mahmood_Saeed_Jasim_Ibrahim_Khdeer_Zaid_Hasan_Haider_Salih_Abbas_Kaka__CoD_MW3_2011_Version__I_RAN_OUT_OF_NAMES.Grade)
if Mona.pass_check() == "Passed":
    print("\n\nThe student "+Mona.Name+" Has Passed with a Grade of : "+Mona.Grade)
elif Mona.pass_check() == "Failed":
    print("\n\nThe student "+Mona.Name+" Has Failed with a Grade of : "+Mona.Grade)
