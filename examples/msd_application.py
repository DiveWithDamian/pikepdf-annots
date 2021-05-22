from datetime import datetime
from decimal import Decimal
from pathlib import PosixPath
from typing import Optional

from pikepdf_annots import EditableForm, AnnotationMatcher


class MasterScubaDiverForm(EditableForm):

    def _get_source_pdf(self) -> PosixPath:
        return PosixPath("10142_Master_Scuba_Diver_Application_ff.pdf")

    def update_student(self,
                       first_name: str,
                       middle_initial: Optional[str],
                       last_name: str,
                       dob: datetime,
                       is_male: bool,
                       address_line1: str,
                       address_city: str,
                       address_province: str,
                       address_country: str,
                       address_postcode: str,
                       email: str,
                       phone: Optional[str]):
        self.update_annotation(0,
                               AnnotationMatcher("Name"),
                               (f"{first_name} {middle_initial} {last_name}"
                                if middle_initial else
                                f"{first_name} {last_name}"))
        self.update_annotation(0,
                               AnnotationMatcher("Date of Birth"),
                               dob.strftime("%d/%m/%Y"))
        self.update_annotation(0,
                               AnnotationMatcher("Mailing Address"),
                               address_line1)
        self.update_annotation(0,
                               AnnotationMatcher("City"),
                               address_city)
        self.update_annotation(0,
                               AnnotationMatcher("StateProvince", "Province"),
                               address_province)
        self.update_annotation(0,
                               AnnotationMatcher("Country"),
                               address_country)
        self.update_annotation(0,
                               AnnotationMatcher("ZipPostal Code", "Post Code"),
                               address_postcode)
        self.update_annotation(0,
                               AnnotationMatcher("Email"),
                               email)
        self.update_annotation(0,
                               AnnotationMatcher(
                                   [Decimal("484.444"), Decimal("605.258"),
                                    Decimal("493.153"), Decimal("614.086")],
                                   "Return package to diver"
                               ),
                               True)
        self.update_annotation(0,
                               AnnotationMatcher(
                                   [Decimal("325.611"), Decimal("459.248"),
                                    Decimal("334.32"), Decimal("468.189")],
                                   "Male"
                               ),
                               is_male)
        self.update_annotation(0,
                               AnnotationMatcher(
                                   [Decimal("353.111"), Decimal("459.304"),
                                    Decimal("361.82"), Decimal("468.189")],
                                   "Female"
                               ),
                               not is_male)

        if phone:
            self.update_annotation(0,
                                   AnnotationMatcher("Home Phone", "Student Phone Country Code"),
                                   phone[0:4].lstrip("0"))
            self.update_annotation(0,
                                   AnnotationMatcher("undefined", "Student Phone Number"),
                                   phone[4:])

    def update_instructor(self,
                          name: str,
                          number: int,
                          resort_name: Optional[str],
                          resort_number: Optional[int],
                          date: datetime,
                          certificate_date: datetime):
        self.update_annotation(0,
                               AnnotationMatcher("Certifying Instructor"),
                               name)
        self.update_annotation(0,
                               AnnotationMatcher("PADI No"),
                               str(number))

        if resort_name and resort_number:
            self.update_annotation(0,
                                   AnnotationMatcher("Dive CenterResort_2", "Dive Center"),
                                   resort_name)
            self.update_annotation(0,
                                   AnnotationMatcher("Store No  S", "Dive Center No"),
                                   str(resort_number))

        self.update_annotation(0,
                               AnnotationMatcher("Certification Date"),
                               certificate_date.strftime("%d/%m/%Y"))
        self.update_annotation(0,
                               AnnotationMatcher("Date"),
                               date.strftime("%d/%m/%Y"))

    def update_advanced_open_water(self,
                                   certificate_date: datetime,
                                   certificate_number: str,
                                   instructor_name: str,
                                   instructor_number: int):
        self.update_annotation(1,
                               AnnotationMatcher("Instructor Name", "Advanced Instructor"),
                               instructor_name)
        self.update_annotation(1,
                               AnnotationMatcher("Instructor No", "Advanced Instructor Number"),
                               str(instructor_number))
        self.update_annotation(1,
                               AnnotationMatcher("Certification No", "Advanced Certification Number"),
                               certificate_number)
        self.update_annotation(1,
                               AnnotationMatcher("Certification Date_2", "Advanced Certification Date"),
                               certificate_date.strftime("%d/%m/%Y"))

    def update_rescue_diver(self,
                            certificate_date: datetime,
                            certificate_number: str,
                            instructor_name: str,
                            instructor_number: int):
        self.update_annotation(1,
                               AnnotationMatcher("Instructor Name_3", "Rescue Instructor"),
                               instructor_name)
        self.update_annotation(1,
                               AnnotationMatcher("Instructor No_3", "Rescue Instructor Number"),
                               str(instructor_number))
        self.update_annotation(1,
                               AnnotationMatcher("Certification No_2", "Rescue Certification Number"),
                               certificate_number)
        self.update_annotation(1,
                               AnnotationMatcher("Certification Date_4", "Rescue Certification Date"),
                               certificate_date.strftime("%d/%m/%Y"))

    def update_speciality_1(self,
                            certificate_name: str,
                            certificate_date: datetime,
                            certificate_number: str,
                            instructor_name: str,
                            instructor_number: int):
        self.update_annotation(1,
                               AnnotationMatcher("undefined_7", "Speciality 1 Name"),
                               certificate_name)
        self.update_annotation(1,
                               AnnotationMatcher("undefined_8", "Speciality 1 Date"),
                               certificate_date.strftime("%d/%m/%Y"))
        self.update_annotation(1,
                               AnnotationMatcher("undefined_9", "Speciality 1 Instructor"),
                               instructor_name)
        self.update_annotation(1,
                               AnnotationMatcher("undefined_10", "Speciality 1 Instructor Number"),
                               str(instructor_number))
        self.update_annotation(1,
                               AnnotationMatcher("undefined_11", "Speciality 1 Certification Number"),
                               certificate_number)

    def update_speciality_2(self,
                            certificate_name: str,
                            certificate_date: datetime,
                            certificate_number: str,
                            instructor_name: str,
                            instructor_number: int):
        self.update_annotation(1,
                               AnnotationMatcher("undefined_12", "Speciality 2 Name"),
                               certificate_name)
        self.update_annotation(1,
                               AnnotationMatcher("undefined_13", "Speciality 2 Date"),
                               certificate_date.strftime("%d/%m/%Y"))
        self.update_annotation(1,
                               AnnotationMatcher("undefined_14", "Speciality 2 Instructor"),
                               instructor_name)
        self.update_annotation(1,
                               AnnotationMatcher("undefined_15", "Speciality 2 Instructor Number"),
                               str(instructor_number))
        self.update_annotation(1,
                               AnnotationMatcher("undefined_16", "Speciality 2 Certification Number"),
                               certificate_number)

    def update_speciality_3(self,
                            certificate_name: str,
                            certificate_date: datetime,
                            certificate_number: str,
                            instructor_name: str,
                            instructor_number: int):
        self.update_annotation(1,
                               AnnotationMatcher("undefined_17", "Speciality 3 Name"),
                               certificate_name)
        self.update_annotation(1,
                               AnnotationMatcher("undefined_18", "Speciality 3 Date"),
                               certificate_date.strftime("%d/%m/%Y"))
        self.update_annotation(1,
                               AnnotationMatcher("undefined_19", "Speciality 3 Instructor"),
                               instructor_name)
        self.update_annotation(1,
                               AnnotationMatcher("undefined_20", "Speciality 3 Instructor Number"),
                               str(instructor_number))
        self.update_annotation(1,
                               AnnotationMatcher("undefined_21", "Speciality 3 Certification Number"),
                               certificate_number)

    def update_speciality_4(self,
                            certificate_name: str,
                            certificate_date: datetime,
                            certificate_number: str,
                            instructor_name: str,
                            instructor_number: int):
        self.update_annotation(1,
                               AnnotationMatcher("undefined_22", "Speciality 4 Name"),
                               certificate_name)
        self.update_annotation(1,
                               AnnotationMatcher("undefined_23", "Speciality 4 Date"),
                               certificate_date.strftime("%d/%m/%Y"))
        self.update_annotation(1,
                               AnnotationMatcher("undefined_24", "Speciality 4 Instructor"),
                               instructor_name)
        self.update_annotation(1,
                               AnnotationMatcher("undefined_25", "Speciality 4 Instructor Number"),
                               str(instructor_number))
        self.update_annotation(1,
                               AnnotationMatcher("undefined_26", "Speciality 4 Certification Number"),
                               certificate_number)

    def update_speciality_5(self,
                            certificate_name: str,
                            certificate_date: datetime,
                            certificate_number: str,
                            instructor_name: str,
                            instructor_number: int):
        self.update_annotation(1,
                               AnnotationMatcher("undefined_27", "Speciality 5 Name"),
                               certificate_name)
        self.update_annotation(1,
                               AnnotationMatcher("undefined_28", "Speciality 5 Date"),
                               certificate_date.strftime("%d/%m/%Y"))
        self.update_annotation(1,
                               AnnotationMatcher("undefined_29", "Speciality 5 Instructor"),
                               instructor_name)
        self.update_annotation(1,
                               AnnotationMatcher("undefined_30", "Speciality 5 Instructor Number"),
                               str(instructor_number))
        self.update_annotation(1,
                               AnnotationMatcher("undefined_31", "Speciality 5 Certification Number"),
                               certificate_number)


if __name__ == '__main__':
    with MasterScubaDiverForm() as pdf:
        pdf.update_student('Bob', None, 'Smith',
                           datetime(1900, 1, 1),
                           True,
                           'Paleis Amsterdam',
                           'Amsterdam',
                           'North Holland',
                           'Netherlands',
                           '1012 RJ',
                           'bob.smith@example.com',
                           None)

        pdf.update_instructor('Alice Hargreaves',
                              1234,
                              None,
                              None,
                              datetime(1918, 8, 7),
                              datetime(1918, 8, 1))

        pdf.update_advanced_open_water(datetime(1918, 1, 1),
                                       'XXX',
                                       'Alice Hargreaves',
                                       1234)

        pdf.update_rescue_diver(datetime(1918, 2, 1),
                                'XXX',
                                'Alice Hargreaves',
                                1234)

        pdf.update_speciality_1('Deep Diver',
                                datetime(1918, 3, 1),
                                'XXX',
                                'Alice Hargreaves',
                                1234)

        pdf.update_speciality_2('Drysuit Diver',
                                datetime(1918, 4, 1),
                                'XXX',
                                'Alice Hargreaves',
                                1234)
        pdf.update_speciality_3('Night Diver',
                                datetime(1918, 5, 1),
                                'XXX',
                                'Alice Hargreaves',
                                1234)
        pdf.update_speciality_4('Enriched Air Diver',
                                datetime(1918, 6, 1),
                                'XXX',
                                'Alice Hargreaves',
                                1234)
        pdf.update_speciality_5('Boat Diver',
                                datetime(1918, 7, 1),
                                'XXX',
                                'Alice Hargreaves',
                                1234)

        pdf.export(PosixPath('msd-bob-smith.pdf'))
